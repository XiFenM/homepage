"""
T2 · Generate SVG masks for paper-curl and edge-wear.

Outputs to ../generated/masks/:
  - paper-curl.svg     : triangular curl-up corner mask (top-right by default)
  - edge-wear.svg      : irregular torn-edge mask for parchment-style cards

These are vector shapes meant to be used as CSS clip-path or as
<mask>/<clipPath> elements. The shapes are slightly randomized per generation
so re-running gives variants — pin a --seed to reproduce.

Usage:
    uv run python tools/make_masks.py
    uv run python tools/make_masks.py --seed 42 --variants 3
"""

from __future__ import annotations

import argparse
from pathlib import Path
import math
import random


OUT_DIR = Path(__file__).resolve().parent.parent.parent / "generated" / "masks"


# ────────────────────────────────────────────────────────────────────
# paper-curl: a triangular tongue at the top-right corner of a card
# ────────────────────────────────────────────────────────────────────
def paper_curl_svg(width: int = 100, height: int = 100, curl_size: float = 0.18, rng: random.Random | None = None) -> str:
    """
    SVG with viewBox (0 0 width height). Path describes a card with the top-right
    corner curled away — i.e., a chamfered corner where the chamfer is a curve
    suggesting paper bending.

    The mask is the *opaque card* (everything that should remain visible).
    """
    rng = rng or random.Random()
    cx = width * (1.0 - curl_size)        # curl starts here on top edge
    cy = height * curl_size               # curl ends here on right edge
    # Bezier control point bowing outward to suggest paper rounding
    bow = curl_size * width * 0.35 * (0.85 + rng.random() * 0.3)

    # Path: start top-left, top edge to curl-start, bezier curl down,
    # right edge down to bottom-right, bottom-left, close.
    path = (
        f"M 0 0 "                                              # top-left
        f"L {cx:.2f} 0 "                                       # top edge to curl
        f"C {cx + bow:.2f} {bow * 0.4:.2f}, "                  # control 1 (outside corner)
        f"{width - bow * 0.4:.2f} {cy + bow:.2f}, "            # control 2 (outside corner)
        f"{width:.2f} {cy:.2f} "                               # curl-end on right edge
        f"L {width} {height} "                                 # right edge down
        f"L 0 {height} "                                       # bottom edge
        f"Z"
    )

    # Also generate the *flap* (the curled-up triangle), useful as a separate
    # element painted with darker shade to suggest paper underside.
    flap = (
        f"M {cx:.2f} 0 "
        f"L {width:.2f} 0 "
        f"L {width:.2f} {cy:.2f} "
        f"C {width - bow * 0.4:.2f} {cy + bow:.2f}, "
        f"{cx + bow:.2f} {bow * 0.4:.2f}, "
        f"{cx:.2f} 0 "
        f"Z"
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <!-- paper-curl mask: opaque card body (use as clip-path) -->
  <path id="card-body" d="{path}" fill="oklch(95% 0.005 85)" />
  <!-- the curled-up flap (slightly darker, simulates paper underside) -->
  <path id="curl-flap" d="{flap}" fill="oklch(85% 0.01 80)" opacity="0.35" />
</svg>
"""


# ────────────────────────────────────────────────────────────────────
# edge-wear: a torn / deckled edge mask for parchment-style cards
# ────────────────────────────────────────────────────────────────────
def edge_wear_svg(width: int = 100, height: int = 100, jitter: float = 0.03, segments: int = 60, rng: random.Random | None = None) -> str:
    """
    A rectangular mask whose 4 edges are slightly jittered to suggest torn
    parchment edges. `jitter` is the max inward offset as a fraction of the
    short edge.
    """
    rng = rng or random.Random()
    short = min(width, height)
    j = jitter * short

    points: list[tuple[float, float]] = []

    def add_edge(x0, y0, x1, y1, normal_x, normal_y):
        # normal points INTO the rectangle (so jitter pushes toward inside)
        for i in range(segments + 1):
            t = i / segments
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            # Skip endpoint (handled by next edge's start)
            if i == segments:
                continue
            # Random inward jitter, biased so most jitter is small but some peaks
            r = rng.random() ** 2.0  # quadratic falloff — most points stay close to edge
            offset = r * j
            points.append((x + normal_x * offset, y + normal_y * offset))

    # Top edge L→R, normal points down (+y)
    add_edge(0, 0, width, 0, 0, 1)
    # Right edge T→B, normal points left (-x)
    add_edge(width, 0, width, height, -1, 0)
    # Bottom edge R→L, normal points up (-y)
    add_edge(width, height, 0, height, 0, -1)
    # Left edge B→T, normal points right (+x)
    add_edge(0, height, 0, 0, 1, 0)

    path_d = "M " + f"{points[0][0]:.2f} {points[0][1]:.2f}"
    for x, y in points[1:]:
        path_d += f" L {x:.2f} {y:.2f}"
    path_d += " Z"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <!-- edge-wear mask: parchment with deckled / torn edges -->
  <path d="{path_d}" fill="oklch(89% 0.04 80)" />
</svg>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None, help="reproduce specific variant")
    parser.add_argument("--variants", type=int, default=3, help="how many of each shape to emit")
    parser.add_argument("--width", type=int, default=400)
    parser.add_argument("--height", type=int, default=300)
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    base_seed = args.seed if args.seed is not None else 0

    # Always produce a canonical "paper-curl.svg" + a few variants
    canonical_curl = OUT_DIR / "paper-curl.svg"
    canonical_curl.write_text(paper_curl_svg(args.width, args.height, rng=random.Random(base_seed + 1)))
    print(f"  ✓ {canonical_curl.relative_to(OUT_DIR.parent.parent)}")

    canonical_wear = OUT_DIR / "edge-wear.svg"
    canonical_wear.write_text(edge_wear_svg(args.width, args.height, rng=random.Random(base_seed + 100)))
    print(f"  ✓ {canonical_wear.relative_to(OUT_DIR.parent.parent)}")

    # Numbered variants for picking
    for i in range(2, args.variants + 1):
        p = OUT_DIR / f"paper-curl-v{i}.svg"
        p.write_text(paper_curl_svg(args.width, args.height, rng=random.Random(base_seed + i)))
        print(f"  ✓ {p.relative_to(OUT_DIR.parent.parent)}")

        p = OUT_DIR / f"edge-wear-v{i}.svg"
        p.write_text(edge_wear_svg(args.width, args.height, rng=random.Random(base_seed + 100 + i)))
        print(f"  ✓ {p.relative_to(OUT_DIR.parent.parent)}")

    print(f"\nDone. Use as CSS clip-path: clip-path: url('#card-body');")
    print(f"Or as SVG <mask> by referencing the path id.")


if __name__ == "__main__":
    main()
