"""
Generate Wave 5 video assets via ZenMux's seedance2 endpoint (image-to-video).

Usage:
    uv run python video_gen.py V1
    uv run python video_gen.py V1 V2 V3
    uv run python video_gen.py --all

Output layout:
    ../generated/video/{code}/attempt-{NN}/
        01.mp4               ← raw model output
        prompt-used.txt      ← exact prompt used
        starting-frame.png   ← copy of the input image
        meta.json            ← params + timing
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path

from google import genai
from google.genai import types

from prompts import VIDEO_CATALOG, VideoSpec


GENERATED_ROOT = Path(__file__).resolve().parent.parent / "generated"
VIDEO_OUT_ROOT = GENERATED_ROOT / "video"
ZENMUX_BASE_URL = "https://zenmux.ai/api/vertex-ai"
DEFAULT_MODEL = "bytedance/doubao-seedance-2.0"
KNOWN_MODELS = (
    "bytedance/doubao-seedance-2.0",
    "bytedance/doubao-seedance-1.5-pro",
    "google/veo-3.1-generate-001",
)
POLL_INTERVAL = 15  # seconds, per zenmux best-practice tip


def get_client() -> genai.Client:
    api_key = os.environ.get("ZENMUX_API_KEY")
    if not api_key:
        sys.exit("ZENMUX_API_KEY env var is not set.")
    return genai.Client(
        api_key=api_key,
        vertexai=True,
        http_options=types.HttpOptions(api_version="v1", base_url=ZENMUX_BASE_URL),
    )


def next_attempt_dir(code: str) -> Path:
    asset_dir = VIDEO_OUT_ROOT / code
    asset_dir.mkdir(parents=True, exist_ok=True)
    existing = [
        int(m.group(1))
        for p in asset_dir.iterdir()
        if p.is_dir() and (m := re.match(r"attempt-(\d+)$", p.name))
    ]
    n = (max(existing) + 1) if existing else 1
    out = asset_dir / f"attempt-{n:02d}"
    out.mkdir()
    return out


def load_starting_frame(rel_path: str) -> tuple[bytes, str]:
    abs_path = GENERATED_ROOT / rel_path
    if not abs_path.exists():
        sys.exit(f"Starting frame not found: {abs_path}")
    suffix = abs_path.suffix.lower()
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(suffix, "image/png")
    return abs_path.read_bytes(), mime


def save_video(vid_obj, dest: Path) -> int:
    """Defensive save: handle a few possible shapes of the response Video object."""
    candidate = vid_obj
    # Some SDK versions wrap: GeneratedVideo(video=Video(video_bytes=...))
    if hasattr(candidate, "video") and not hasattr(candidate, "video_bytes"):
        candidate = candidate.video

    if hasattr(candidate, "save"):
        candidate.save(str(dest))
    elif hasattr(candidate, "video_bytes") and candidate.video_bytes is not None:
        dest.write_bytes(candidate.video_bytes)
    elif hasattr(candidate, "uri") and candidate.uri:
        # Fallback: download from URI
        import urllib.request
        urllib.request.urlretrieve(candidate.uri, str(dest))
    else:
        attrs = [a for a in dir(candidate) if not a.startswith("_")]
        raise RuntimeError(
            f"Cannot save video: object has no recognizable save method. attrs={attrs}"
        )
    return dest.stat().st_size


def generate_one(client: genai.Client, spec: VideoSpec, model: str) -> Path:
    print(f"\n=== {spec.code} · {spec.label} ===")
    print(f"  starting_frame={spec.starting_frame}")
    print(f"  ar={spec.aspect_ratio}  res={spec.resolution}  duration={spec.duration_seconds}s")
    print(f"  model={model}")

    out_dir = next_attempt_dir(spec.code)
    print(f"  → {out_dir.relative_to(GENERATED_ROOT.parent)}")

    image_bytes, mime = load_starting_frame(spec.starting_frame)
    starting_copy = out_dir / "starting-frame.png"
    shutil.copyfile(GENERATED_ROOT / spec.starting_frame, starting_copy)

    image = types.Image(image_bytes=image_bytes, mime_type=mime)

    t0 = time.time()
    try:
        operation = client.models.generate_videos(
            model=model,
            image=image,
            prompt=spec.prompt,
            config=types.GenerateVideosConfig(
                aspectRatio=spec.aspect_ratio,
                resolution=spec.resolution,
                durationSeconds=spec.duration_seconds,
                generateAudio=spec.generate_audio,
            ),
        )
        print(f"  ↳ submitted, polling every {POLL_INTERVAL}s ...")

        while not operation.done:
            time.sleep(POLL_INTERVAL)
            operation = client.operations.get(operation)
            elapsed = int(time.time() - t0)
            print(f"    [{elapsed}s] still running...")

    except Exception as e:
        elapsed = time.time() - t0
        (out_dir / "ERROR.txt").write_text(f"{type(e).__name__}: {e}\n")
        print(f"  ✗ failed after {elapsed:.1f}s: {e}")
        raise

    elapsed = time.time() - t0
    videos = (operation.response and operation.response.generated_videos) or []
    print(f"  ✓ {len(videos)} video(s) returned in {elapsed:.1f}s")

    for i, v in enumerate(videos, start=1):
        path = out_dir / f"{i:02d}.mp4"
        try:
            size_kb = save_video(v, path) // 1024
            print(f"    saved {path.name}  ({size_kb} KB)")
        except Exception as e:
            print(f"    ✗ save failed: {e}")
            (out_dir / f"ERROR-save-{i:02d}.txt").write_text(str(e))

    (out_dir / "prompt-used.txt").write_text(spec.prompt, encoding="utf-8")
    (out_dir / "meta.json").write_text(
        json.dumps(
            {
                "code": spec.code,
                "label": spec.label,
                "model": model,
                "starting_frame": spec.starting_frame,
                "aspect_ratio": spec.aspect_ratio,
                "resolution": spec.resolution,
                "duration_seconds": spec.duration_seconds,
                "generate_audio": spec.generate_audio,
                "n_returned": len(videos),
                "elapsed_seconds": round(elapsed, 2),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return out_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Wave 5 video assets.")
    parser.add_argument("codes", nargs="*", help="Video codes (e.g. V1 V2 V3)")
    parser.add_argument("--all", action="store_true")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Model id (default: {DEFAULT_MODEL}; known: {', '.join(KNOWN_MODELS)})",
    )
    args = parser.parse_args()

    if args.all:
        codes = list(VIDEO_CATALOG.keys())
    elif args.codes:
        codes = args.codes
    else:
        parser.error("specify codes or --all")

    unknown = [c for c in codes if c not in VIDEO_CATALOG]
    if unknown:
        sys.exit(f"unknown codes: {unknown}. Known: {list(VIDEO_CATALOG.keys())}")

    client = get_client()
    failures: list[str] = []
    for code in codes:
        try:
            generate_one(client, VIDEO_CATALOG[code], args.model)
        except Exception as e:
            failures.append(f"{code}: {type(e).__name__}: {e}")

    if failures:
        print("\nFailures:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("\nAll done.")


if __name__ == "__main__":
    main()
