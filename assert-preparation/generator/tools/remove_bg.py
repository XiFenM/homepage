"""
Remove white backgrounds from S1/S4/S5C assets.

Strategy: flood-fill from each corner. Only "exterior white" (white pixels
connected to the canvas edge) becomes transparent — interior light pixels
(e.g. the cream-colored cards, the warm parchment) are preserved because they
are not connected to the corners.

A 1-pixel Gaussian blur on the resulting alpha channel feathers the cut edge
to avoid jaggies.

Overwrites web/public/art/signatures/*.png and web/public/art/homepage/*.png
in place. The originals (with white background) remain in
assert-preparation/generated/static/{S1,S4,S5C}/final.png.

Usage:
    uv run python tools/remove_bg.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import label


ROOT = Path(__file__).resolve().parent.parent.parent.parent
SOURCE_ROOT = ROOT / "assert-preparation" / "generated" / "static"
WEB_ART = ROOT / "web" / "public" / "art"

TARGETS = [
    # (source-final, web-output, white-threshold)
    # threshold = pixels with min-channel >= this are candidate-white
    (SOURCE_ROOT / "S1"  / "final.png", WEB_ART / "signatures" / "wordmark-zh.png",     240),
    (SOURCE_ROOT / "S4"  / "final.png", WEB_ART / "homepage"   / "parchment-scroll.png", 240),
    (SOURCE_ROOT / "S5C" / "final.png", WEB_ART / "homepage"   / "card-stack.png",      245),
]


def remove_white_bg(src: Path, dest: Path, threshold: int) -> None:
    img = Image.open(src).convert("RGBA")
    arr = np.array(img)
    h, w = arr.shape[:2]

    # "Whiteness" = how close to pure white via min-channel.
    rgb_min = arr[..., :3].min(axis=-1)
    is_white = rgb_min >= threshold

    # Connected-components label all white regions.
    labeled, n = label(is_white)

    # Find labels touching the canvas border — those are "exterior white".
    border_labels = set()
    border_labels.update(labeled[0, :].tolist())
    border_labels.update(labeled[-1, :].tolist())
    border_labels.update(labeled[:, 0].tolist())
    border_labels.update(labeled[:, -1].tolist())
    border_labels.discard(0)  # 0 = "not in any white region"

    if not border_labels:
        # Nothing connected to the border — image already has transparent edges
        # or no white at corners. Save as-is.
        dest.parent.mkdir(parents=True, exist_ok=True)
        img.save(dest, optimize=True)
        print(f"  ⚠ {dest.relative_to(ROOT)}  (no exterior white found)")
        return

    exterior = np.isin(labeled, list(border_labels))

    # Set alpha=0 for exterior white pixels.
    alpha_arr = arr[..., 3].copy()
    alpha_arr[exterior] = 0

    # Soft edge: Gaussian-blur the alpha channel by ~1px to feather.
    alpha_img = Image.fromarray(alpha_arr, mode="L").filter(
        ImageFilter.GaussianBlur(radius=1.2)
    )
    arr[..., 3] = np.array(alpha_img)

    dest.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(arr).save(dest, optimize=True)

    pct_removed = 100 * exterior.sum() / exterior.size
    size_kb = dest.stat().st_size // 1024
    rel = dest.relative_to(ROOT)
    print(f"  ✓ {rel}  ({size_kb} KB, removed {pct_removed:.1f}% as exterior bg)")


def main() -> None:
    for src, dest, threshold in TARGETS:
        if not src.exists():
            print(f"  ✗ source missing: {src}")
            continue
        remove_white_bg(src, dest, threshold)


if __name__ == "__main__":
    main()
