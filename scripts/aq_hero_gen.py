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

# Prompts reflecting the builder-workspace ecosystem:
# - 973 projects bootstrapped via meta-meta prompt
# - Five-tool interlock: bd (issues), cprr (conjectures), aq (gossip),
#   sb (worktrees), spec.org -> CLAUDE.md pipeline
# - Team structure: ALPHA/BRAVO/CHARLIE/DELTA/ECHO
# - Dependency chains, conjecture prosecution, conflict detection
PROMPTS = [
    {
        "id": "p1_thousand_projects",
        "title": "A Thousand Spec Files / The Bootstrap",
        "model_hint": "z-image",
        "prompt": (
            "aerial view of a vast grid of one thousand glowing blueprint documents "
            "arranged on a dark surface, each blueprint connected to its neighbors by "
            "thin dependency lines forming a directed acyclic graph, "
            "five colored team zones radiate outward from the center in concentric rings, "
            "amber for ALPHA, green for BRAVO, blue for CHARLIE, red for DELTA, violet for ECHO, "
            "spec.org files transforming into CLAUDE.md through a luminous pipeline in the center, "
            "monochrome background with warm amber highlights, 8k, ultra-detailed, "
            "technical diagram meets cartography, cinematic overhead shot, no text labels"
        ),
        "negative": "cluttered, busy, logos, text, watermark, people",
    },
    {
        "id": "p2_five_tool_interlock",
        "title": "Five-Tool Interlock / bd-cprr-aq-sb-spec",
        "model_hint": "z-image",
        "prompt": (
            "five interlocking mechanical gears of different sizes floating in darkness, "
            "each gear made of a different glowing material: "
            "amber crystalline gear for issue tracking, "
            "green phosphorescent gear for conjecture prosecution, "
            "blue electric gear for gossip broadcasts, "
            "silver metallic gear for worktree isolation, "
            "gold filigree gear for spec-to-agent pipeline, "
            "gears meshing perfectly with visible teeth engaging, "
            "sparks at contact points where tools exchange data, "
            "dramatic chiaroscuro lighting, clockwork mechanism aesthetic, "
            "dark background, cinematic composition, no text"
        ),
        "negative": "text labels, logos, bright colors, flat, cartoon",
    },
    {
        "id": "p3_conjecture_wall",
        "title": "Three Thousand Conjectures / The Evidence Wall",
        "model_hint": "flux",
        "prompt": (
            "massive evidence wall in a dimly lit detective office, "
            "three thousand index cards pinned to a cork board stretching to infinity, "
            "red string connecting cards in clusters by project, "
            "some cards glowing green for confirmed, most neutral for open, "
            "a few marked with red X for refuted, "
            "magnifying glass hovering over one cluster showing falsification criteria, "
            "noir detective aesthetic meets scientific method, "
            "warm amber desk lamp, chalk-white card text, "
            "1940s film noir meets modern data visualization, minimalist"
        ),
        "negative": "colorful, digital, neon, busy, logos, modern",
    },
    {
        "id": "p4_team_sprint",
        "title": "Five Teams in Parallel / Worktree Isolation",
        "model_hint": "z-image",
        "prompt": (
            "five parallel railroad tracks stretching into foggy distance, "
            "each track a different color representing a team, "
            "translucent train cars on each track carrying glowing cargo of different types: "
            "AI models, biosensors, solar panels, security shields, social graphs, "
            "tracks occasionally crossing at junction switches where conflict sparks fly, "
            "a central signal tower broadcasting amber presence rings to all tracks, "
            "cold blue atmospheric fog, long exposure photographic aesthetic, "
            "industrial infrastructure meets neural network diagram, cinematic"
        ),
        "negative": "text, logos, people faces, bright daylight, cartoon",
    },
    {
        "id": "p5_dependency_cascade",
        "title": "Dependency Cascade / Step 1 Closes",
        "model_hint": "flux",
        "prompt": (
            "chain of dominoes arranged in a spiral viewed from above, "
            "the first domino falling and triggering a cascade, "
            "each domino is a translucent card showing a build step, "
            "fallen dominoes glow green, standing dominoes pulse amber waiting, "
            "blocked dominoes have visible chains to their prerequisites, "
            "the spiral contains thousands of dominoes in concentric rings, "
            "style of 1970s Bell Labs scientific illustration, "
            "muted color palette, ink on cream paper texture, "
            "clean margins, architectural precision, no clutter"
        ),
        "negative": "digital, neon, busy, logos, photographs, 3D render",
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
