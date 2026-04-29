"""
Generate static assets via ZenMux's gpt-image-2 endpoint.

Usage:
    uv run python generate.py S1
    uv run python generate.py S2A S2B
    uv run python generate.py --all       # everything in CATALOG

Output layout:
    ../generated/static/{code}/attempt-{NN}/
        01.png  02.png  03.png  04.png   ← raw model outputs
        prompt-used.txt                  ← exact prompt used this run
        meta.json                        ← params + timing
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

from google import genai
from google.genai import types

from prompts import CATALOG, AssetSpec


GENERATED_ROOT = Path(__file__).resolve().parent.parent / "generated" / "static"
ZENMUX_BASE_URL = "https://zenmux.ai/api/vertex-ai"
MODEL = "openai/gpt-image-2"


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
    asset_dir = GENERATED_ROOT / code
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


def generate_one(client: genai.Client, spec: AssetSpec) -> Path:
    print(f"\n=== {spec.code} · {spec.label} ===")
    print(f"  size={spec.image_size}  n={spec.n}  model={MODEL}")

    out_dir = next_attempt_dir(spec.code)
    print(f"  → {out_dir.relative_to(Path.cwd().parent)}")

    t0 = time.time()
    try:
        response = client.models.generate_images(
            model=MODEL,
            prompt=spec.prompt,
            config=types.GenerateImagesConfig(
                number_of_images=spec.n,
                image_size=spec.image_size,
                output_mime_type=spec.output_mime,
            ),
        )
    except Exception as e:
        elapsed = time.time() - t0
        print(f"  ✗ failed after {elapsed:.1f}s: {e}")
        (out_dir / "ERROR.txt").write_text(f"{type(e).__name__}: {e}\n")
        raise

    elapsed = time.time() - t0

    images = response.generated_images or []
    print(f"  ✓ {len(images)} image(s) in {elapsed:.1f}s")

    ext = spec.output_mime.split("/")[-1]
    for i, img in enumerate(images, start=1):
        path = out_dir / f"{i:02d}.{ext}"
        img.image.save(str(path))
        print(f"    saved {path.name}  ({path.stat().st_size // 1024} KB)")

    (out_dir / "prompt-used.txt").write_text(spec.prompt, encoding="utf-8")
    (out_dir / "meta.json").write_text(
        json.dumps(
            {
                "code": spec.code,
                "label": spec.label,
                "model": MODEL,
                "image_size": spec.image_size,
                "n_requested": spec.n,
                "n_returned": len(images),
                "output_mime": spec.output_mime,
                "elapsed_seconds": round(elapsed, 2),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return out_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Wave-N static assets.")
    parser.add_argument("codes", nargs="*", help="Asset codes to generate (e.g. S1 S2A)")
    parser.add_argument("--all", action="store_true", help="Generate every asset in CATALOG")
    args = parser.parse_args()

    if args.all:
        codes = list(CATALOG.keys())
    elif args.codes:
        codes = args.codes
    else:
        parser.error("specify asset codes or --all")

    unknown = [c for c in codes if c not in CATALOG]
    if unknown:
        sys.exit(f"unknown asset codes: {unknown}. Known: {list(CATALOG.keys())}")

    client = get_client()
    failures: list[str] = []
    for code in codes:
        try:
            generate_one(client, CATALOG[code])
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
