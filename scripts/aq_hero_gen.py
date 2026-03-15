#!/usr/bin/env python3
"""
aq hero image generator — runs on mini via ollama
Usage: python3 aq_hero_gen.py [--model z-image|flux] [--prompt N]

Models available on mini:
  x/z-image-turbo:latest  (12GB, higher quality)
  x/flux2-klein:4b        (5.7GB, faster)
"""

import argparse
import base64
import json
import sys
import time
import urllib.request
from pathlib import Path
from subprocess import run as subprocess_run

OLLAMA_URL = "http://localhost:11434"

# Prompts calibrated to aq's actual semantics:
# - L1.5 gossip layer, NDJSON/TTL, Seven Concerns stack
# - Three-primitive interlock (sb/cprr/aq)
# - CPRR phases, conflict detection, Boston/FreeBSD context
PROMPTS = [
    {
        "id": "p1_gossip_network",
        "title": "Gossip Network / TTL Decay",
        "model_hint": "z-image",
        "prompt": (
            "network of glowing terminal nodes connected by translucent light filaments "
            "in a void, each node pulsing with soft amber TTL countdown rings, "
            "NDJSON text fragments drifting between nodes like luminous smoke, "
            "some filaments fading mid-transmission, monochrome blue-green palette "
            "with warm amber highlights, cinematic depth of field, 8k, ultra-detailed, "
            "technical diagram meets generative art, no text labels"
        ),
        "negative": "cluttered, busy, colorful, logos, text, watermark",
    },
    {
        "id": "p2_ouroboros_queue",
        "title": "Ouroboros / The Wheel Turns",
        "model_hint": "z-image",
        "prompt": (
            "serpent made entirely of scrolling amber JSON log lines consuming its own tail, "
            "coiled around a vintage 1990s server rack in a dark data center, "
            "neon amber terminal glow on black background, dramatic chiaroscuro, "
            "watercolor wash suggesting ancient manuscript illumination, "
            "moody atmospheric lighting, cinematic composition, no text"
        ),
        "negative": "text labels, logos, bright colors, daytime",
    },
    {
        "id": "p3_filesystem_ghost",
        "title": "Filesystem Ghost / Unix Tree",
        "model_hint": "flux",
        "prompt": (
            "ethereal translucent hand reaching from darkness into a glowing Unix directory tree, "
            "touching a hidden dot-directory node that radiates soft presence signals outward "
            "as expanding concentric rings, pure black background, chalk-white line art "
            "with single amber accent, flat vector aesthetic, 1980s hacker zine illustration style, "
            "negative space hero composition, minimalist"
        ),
        "negative": "colorful, photorealistic, busy, logos, text",
    },
    {
        "id": "p4_harbor_agents",
        "title": "Multi-Agent Swarm / Boston Harbor",
        "model_hint": "z-image",
        "prompt": (
            "five translucent AI agent silhouettes standing in a foggy harbor at night, "
            "Boston container ships visible in background, each agent broadcasting "
            "circular sonar-like presence rings that overlap and interfere, "
            "one ring visibly fading and expiring at low TTL, "
            "cold blue atmospheric fog, long exposure photographic aesthetic, "
            "no faces, abstract geometric agents, cinematic"
        ),
        "negative": "text, logos, people faces, bright colors, daytime",
    },
    {
        "id": "p5_seven_concerns",
        "title": "Seven Concerns Stack / Layer 1.5",
        "model_hint": "flux",
        "prompt": (
            "technical cutaway cross-section of a seven-layer stack like OSI model but organic, "
            "layer 1.5 glowing warm amber labeled with gossip particles flowing laterally, "
            "other layers pulsing vertically in cool blue, "
            "style of 1970s Bell Labs scientific illustration, "
            "muted color palette, serif typography integrated as art, "
            "ink on cream paper texture, clean margins, no clutter"
        ),
        "negative": "digital, neon, busy, logos, photographs",
    },
]

MODEL_MAP = {
    "z-image": "x/z-image-turbo:latest",
    "flux": "x/flux2-klein:4b",
}

# Standard hero/banner sizes
HERO_SIZES = {
    "github":   (1280, 640),   # GitHub social preview
    "twitter":  (1500, 500),   # Twitter/X header
    "og":       (1200, 630),   # Open Graph
    "banner":   (1920, 480),   # Wide banner
}


def resize_image(input_path: Path, output_dir: Path):
    """Resize a generated image to standard hero/banner sizes, preserving the original."""
    try:
        from PIL import Image
    except ImportError:
        print("  [WARN] Pillow not installed, skipping resize. Install: pip install Pillow", file=sys.stderr)
        return

    img = Image.open(input_path)
    stem = input_path.stem
    ext = input_path.suffix

    for name, (w, h) in HERO_SIZES.items():
        # Center-crop to target aspect ratio, then resize
        target_ratio = w / h
        img_ratio = img.width / img.height

        if img_ratio > target_ratio:
            # Image is wider — crop width
            new_w = int(img.height * target_ratio)
            left = (img.width - new_w) // 2
            cropped = img.crop((left, 0, left + new_w, img.height))
        else:
            # Image is taller — crop height
            new_h = int(img.width / target_ratio)
            top = (img.height - new_h) // 2
            cropped = img.crop((0, top, img.width, top + new_h))

        resized = cropped.resize((w, h), Image.LANCZOS)
        out_path = output_dir / f"{stem}-{name}-{w}x{h}{ext}"
        resized.save(out_path, quality=95)
        print(f"  -> {out_path} ({w}x{h})")


def ollama_generate_image(model: str, prompt: str, negative: str = "") -> bytes | None:
    """Call ollama /api/generate for an image model. Returns raw PNG bytes or None."""
    full_prompt = prompt
    if negative:
        full_prompt = f"{prompt} ### negative: {negative}"

    payload = json.dumps({
        "model": model,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "num_predict": 1,
        },
    }).encode()

    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read())
            if "images" in data and data["images"]:
                return base64.b64decode(data["images"][0])
            if "response" in data:
                r = data["response"].strip()
                if r.startswith("data:image"):
                    r = r.split(",", 1)[1]
                try:
                    return base64.b64decode(r)
                except Exception:
                    pass
            print(f"  [WARN] Unexpected response keys: {list(data.keys())}", file=sys.stderr)
            return None
    except urllib.error.HTTPError as e:
        print(f"  [ERROR] HTTP {e.code}: {e.read().decode()}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  [ERROR] {e}", file=sys.stderr)
        return None


def check_ollama() -> bool:
    """Verify ollama is reachable."""
    try:
        with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags", timeout=5) as r:
            data = json.loads(r.read())
            models = [m["name"] for m in data.get("models", [])]
            available = [m for m in MODEL_MAP.values() if any(m in n for n in models)]
            print(f"Ollama reachable. Image models available: {available or 'none found'}")
            return True
    except Exception as e:
        print(f"[ERROR] Cannot reach ollama at {OLLAMA_URL}: {e}", file=sys.stderr)
        return False


def generate_all(model_key: str | None, prompt_idx: int | None, out_dir: Path, do_resize: bool = True):
    out_dir.mkdir(parents=True, exist_ok=True)

    targets = PROMPTS if prompt_idx is None else [PROMPTS[prompt_idx]]

    for p in targets:
        if model_key:
            model = MODEL_MAP[model_key]
        else:
            model = MODEL_MAP.get(p["model_hint"], MODEL_MAP["z-image"])

        print(f"\n{'='*60}")
        print(f"  Prompt: {p['id']} -- {p['title']}")
        print(f"  Model:  {model}")
        print(f"  Text:   {p['prompt'][:80]}...")

        t0 = time.time()
        img_bytes = ollama_generate_image(model, p["prompt"], p["negative"])
        elapsed = time.time() - t0

        if img_bytes:
            ext = "png" if img_bytes[:4] == b'\x89PNG' else "jpg"
            out_path = out_dir / f"aq-hero-{p['id']}.{ext}"
            out_path.write_bytes(img_bytes)
            print(f"  Saved {out_path} ({len(img_bytes)//1024}KB, {elapsed:.1f}s)")

            if do_resize:
                resize_image(out_path, out_dir)
        else:
            prompt_path = out_dir / f"aq-hero-{p['id']}.prompt.txt"
            prompt_path.write_text(
                f"Model: {model}\n\nPrompt:\n{p['prompt']}\n\nNegative:\n{p['negative']}\n"
            )
            print(f"  Generation failed ({elapsed:.1f}s). Prompt saved to {prompt_path}")


def main():
    ap = argparse.ArgumentParser(description="Generate aq hero images via ollama")
    ap.add_argument(
        "--model", choices=["z-image", "flux"],
        help="Override model (default: per-prompt hint)"
    )
    ap.add_argument(
        "--prompt", type=int, choices=range(len(PROMPTS)),
        help=f"Run single prompt 0-{len(PROMPTS)-1} (default: all)"
    )
    ap.add_argument(
        "--out", default="aq-heroes",
        help="Output directory (default: ./aq-heroes)"
    )
    ap.add_argument(
        "--list", action="store_true",
        help="List prompts and exit"
    )
    ap.add_argument(
        "--no-resize", action="store_true",
        help="Skip resizing to standard hero/banner sizes"
    )
    args = ap.parse_args()

    if args.list:
        for i, p in enumerate(PROMPTS):
            print(f"  [{i}] {p['id']} -- {p['title']} (hint: {p['model_hint']})")
            print(f"      {p['prompt'][:100]}...")
        return

    if not check_ollama():
        sys.exit(1)

    generate_all(args.model, args.prompt, Path(args.out), not args.no_resize)
    print(f"\nDone. Images in ./{args.out}/")


if __name__ == "__main__":
    main()
