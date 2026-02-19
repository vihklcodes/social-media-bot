"""
Nano Banana Pro Image Generator
Generates 1030x1350 Instagram poster images from Agent 3 prompts using Google's Gemini API.

Usage:
    python generate_image.py "Your prompt here" --output output.png
    python generate_image.py --merchant "Los Ocampos" --occasion 1
"""

import argparse
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-3-pro-image-preview"
CANVAS_WIDTH = 1030
CANVAS_HEIGHT = 1350


def generate_image(prompt: str, output_path: str) -> str:
    """Generate an image from a Nano Banana Pro prompt and save it."""
    if not API_KEY or API_KEY == "your-api-key-here":
        print("ERROR: Set your GEMINI_API_KEY in .env")
        print("Get one at: https://aistudio.google.com/apikey")
        sys.exit(1)

    client = genai.Client(api_key=API_KEY)

    full_prompt = (
        f"Generate a professional promotional food flyer poster at exactly "
        f"{CANVAS_WIDTH}x{CANVAS_HEIGHT} pixels, portrait orientation. "
        f"{prompt}"
    )

    print(f"Generating image with Nano Banana Pro ({MODEL})...")
    response = client.models.generate_content(
        model=MODEL,
        contents=full_prompt,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio="3:4",
            ),
        ),
    )

    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            image.save(output_path)
            print(f"Image saved to: {output_path}")
            return output_path

    print("ERROR: No image was generated. Response text:")
    for part in response.parts:
        if part.text:
            print(part.text)
    sys.exit(1)


def extract_prompts_from_agent3(merchant_name: str) -> list[dict]:
    """Parse agent3_content.md and extract Nano Banana Pro prompts."""
    agent3_path = Path(f"merchants/{merchant_name}/agent3_content.md")
    if not agent3_path.exists():
        print(f"ERROR: {agent3_path} not found. Run Agent 3 first.")
        sys.exit(1)

    content = agent3_path.read_text()

    # Split by occasion headers (## Occasion, ### Occasion, or numbered occasions)
    occasion_blocks = re.split(r"\n(?=##\s+(?:Occasion|Campaign|Post)\s*\d)", content)
    if len(occasion_blocks) <= 1:
        # Try splitting by horizontal rules or major headers
        occasion_blocks = re.split(r"\n(?=---\n##)", content)

    prompts = []
    for i, block in enumerate(occasion_blocks):
        # Look for the image prompt section
        prompt_match = re.search(
            r"(?:Nano Banana Pro|Image Generation|Image Prompt)[^\n]*\n(.*?)(?=\n##|\n---|\nInstagram Caption|\nCaption|\Z)",
            block,
            re.DOTALL | re.IGNORECASE,
        )
        if prompt_match:
            prompt_text = prompt_match.group(1).strip()
            # Clean up markdown formatting
            prompt_text = re.sub(r"\*\*([^*]+)\*\*", r"\1", prompt_text)
            prompt_text = re.sub(r"^[-*]\s+", "", prompt_text, flags=re.MULTILINE)
            prompts.append({"occasion_index": i, "prompt": prompt_text})

    return prompts


def main():
    parser = argparse.ArgumentParser(description="Generate images with Nano Banana Pro")
    parser.add_argument("prompt", nargs="?", help="Direct image generation prompt")
    parser.add_argument("--output", "-o", default="generated_image.png", help="Output file path")
    parser.add_argument("--merchant", "-m", help="Merchant name to read prompts from agent3_content.md")
    parser.add_argument("--occasion", "-n", type=int, help="Occasion number (1-based) from agent3_content.md")
    args = parser.parse_args()

    if args.merchant:
        prompts = extract_prompts_from_agent3(args.merchant)
        if not prompts:
            print(f"No Nano Banana Pro prompts found in merchants/{args.merchant}/agent3_content.md")
            sys.exit(1)

        if args.occasion:
            idx = args.occasion - 1
            if idx < 0 or idx >= len(prompts):
                print(f"Occasion {args.occasion} not found. Found {len(prompts)} occasions.")
                sys.exit(1)
            prompts = [prompts[idx]]

        output_dir = Path(f"merchants/{args.merchant}/images")
        output_dir.mkdir(parents=True, exist_ok=True)

        for i, p in enumerate(prompts):
            occasion_num = args.occasion or (i + 1)
            output_path = str(output_dir / f"occasion_{occasion_num}.png")
            generate_image(p["prompt"], output_path)
    elif args.prompt:
        generate_image(args.prompt, args.output)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
