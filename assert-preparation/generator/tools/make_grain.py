"""
T1 · Generate paper grain textures procedurally.

Outputs three variants to ../generated/textures/:
  - grain-paper.png       : medium-roughness, for general "warm cream paper"
  - grain-parchment.png   : coarser, for羊皮卷 (Map Mode)
  - grain-cosmos.png      : very fine, for starfield film-grain feel

Each is a 512×512 tileable PNG with transparency — meant to be used as a
mix-blend-mode: multiply overlay at low opacity (8–15%) on top of any surface.

Usage:
    uv run python tools/make_grain.py
    uv run python tools/make_grain.py --size 1024  # bigger
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image


OUT_DIR = Path(__file__).resolve().parent.parent.parent / "generated" / "textures"


def make_seamless_noise(size: int, scale: float, seed: int) -> np.ndarray:
    """
    Generate a tileable grayscale noise array in [0, 1].

    `scale` controls grain coarseness: smaller = finer grain.
    Tileability is achieved via the wrapping trick — generate at 2× and crop
    after smoothing, but here we just generate a periodic noise via FFT.
    """
    rng = np.random.default_rng(seed)
    # Generate white noise
    noise = rng.random((size, size))

    # FFT to get frequency space
    spectrum = np.fft.fft2(noise)

    # Create radial frequency mask — keep only mid-frequencies (the "grain")
    yy, xx = np.meshgrid(
        np.fft.fftfreq(size), np.fft.fftfreq(size), indexing="ij"
    )
    radius = np.sqrt(xx**2 + yy**2)

    # Bandpass: emphasize frequencies around 1/scale
    band = np.exp(-((radius - 1.0 / scale) ** 2) / (2 * (0.3 / scale) ** 2))
    spectrum *= band

    # Inverse FFT — the result is automatically periodic (tileable)
    out = np.fft.ifft2(spectrum).real

    # Normalize to [0, 1]
    out -= out.min()
    out /= out.max() if out.max() > 0 else 1.0
    return out


def grain_to_rgba(noise: np.ndarray, ink_strength: float = 0.4) -> Image.Image:
    """
    Convert grayscale noise into a transparent PNG suitable for multiply-blend
    overlay. Dark grain pixels are opaque dark; light pixels are transparent.
    """
    size = noise.shape[0]
    # Bias darker — we want grain to "darken" surfaces beneath
    grain = 1.0 - noise  # invert: light noise = high alpha
    # Apply gentle gamma to control distribution
    grain = grain**1.6

    rgba = np.zeros((size, size, 4), dtype=np.uint8)
    # Dark gray tone; alpha proportional to grain strength
    rgba[..., 0:3] = 28  # near-black with very slight cool tint applied via PNG color profile
    rgba[..., 3] = (grain * 255 * ink_strength).clip(0, 255).astype(np.uint8)
    return Image.fromarray(rgba, mode="RGBA")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=512, help="texture edge size (default 512)")
    args = parser.parse_args()
    size = args.size
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    variants = [
        # (name, scale (smaller=finer grain), ink_strength, seed)
        ("grain-paper",     0.012, 0.40, 7),    # medium grain for现代纸感
        ("grain-parchment", 0.020, 0.55, 13),   # coarser grain for羊皮卷
        ("grain-cosmos",    0.006, 0.20, 23),   # very fine grain for film-grain夜空
    ]

    for name, scale, ink, seed in variants:
        noise = make_seamless_noise(size, scale, seed)
        img = grain_to_rgba(noise, ink_strength=ink)
        out_path = OUT_DIR / f"{name}.png"
        img.save(out_path, optimize=True)
        print(f"  ✓ {out_path.relative_to(OUT_DIR.parent.parent)}  ({out_path.stat().st_size // 1024} KB, {size}×{size})")

    print(f"\nDone. Use as: background-image: url('grain-*.png'); mix-blend-mode: multiply; opacity: 0.08–0.15;")


if __name__ == "__main__":
    main()
