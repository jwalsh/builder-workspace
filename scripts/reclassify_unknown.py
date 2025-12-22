#!/usr/bin/env python3
"""
Reclassify UNKNOWN projects in the training CSV using Gemini AI.

This script reads the CSV, identifies UNKNOWN entries, and uses
Gemini to classify them into appropriate categories.
"""

import argparse
import csv
import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import google.generativeai as genai

from analyzer.models.category import CategoryEnum


def get_valid_categories():
    """Return list of valid category names (excluding UNKNOWN)."""
    return [c.name for c in CategoryEnum if c.name != "UNKNOWN"]


def classify_with_gemini(model, description: str, project_name: str) -> str:
    """
    Use Gemini to classify a project description.

    Args:
        model: Gemini model instance
        description: Project description
        project_name: Project name for context

    Returns:
        Category name or UNKNOWN if classification fails
    """
    categories = get_valid_categories()
    categories_str = ", ".join(categories)

    prompt = f"""Classify this software project into exactly ONE of these categories:
{categories_str}

Project Name: {project_name}
Description: {description}

Respond with ONLY the category name in uppercase, nothing else."""

    try:
        response = model.generate_content(prompt)
        category = response.text.strip().upper().replace(" ", "_")

        # Validate the category
        if category in CategoryEnum.__members__:
            return category
        else:
            # Try to find partial match
            for valid_cat in categories:
                if valid_cat in category or category in valid_cat:
                    return valid_cat
            return "UNKNOWN"
    except Exception as e:
        print(f"  Error classifying: {e}")
        return "UNKNOWN"


def reclassify_unknown(
    input_file: str = "output/category_projects_for_test_training.csv",
    output_file: str = None,
    dry_run: bool = False,
    limit: int = None,
) -> dict:
    """
    Reclassify UNKNOWN projects using Gemini AI.

    Args:
        input_file: Path to the input CSV file
        output_file: Path to output file (defaults to overwriting input)
        dry_run: If True, only report changes without modifying
        limit: Maximum number of UNKNOWN projects to process

    Returns:
        Dictionary with reclassification statistics
    """
    filepath = Path(input_file)
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {input_file}")

    if output_file is None:
        output_file = input_file

    # Initialize Gemini
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY or GEMINI_API_KEY environment variable required")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    stats = {
        "total_projects": 0,
        "unknown_found": 0,
        "reclassified": 0,
        "still_unknown": 0,
        "by_new_category": {},
    }

    rows = []
    unknown_rows = []

    # First pass: collect all rows and identify UNKNOWN
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            stats["total_projects"] += 1
            if row["Category"] == "UNKNOWN":
                stats["unknown_found"] += 1
                unknown_rows.append((len(rows), row))
            rows.append(row)

    print(f"Found {stats['unknown_found']} UNKNOWN projects to reclassify")

    # Limit processing if specified
    if limit and len(unknown_rows) > limit:
        print(f"Limiting to first {limit} projects")
        unknown_rows = unknown_rows[:limit]

    # Process UNKNOWN rows
    for idx, (row_idx, row) in enumerate(unknown_rows):
        project_name = row["Project Name"]
        description = row["Description"]

        print(f"[{idx+1}/{len(unknown_rows)}] Classifying: {project_name[:50]}...")

        new_category = classify_with_gemini(model, description, project_name)

        if new_category != "UNKNOWN":
            stats["reclassified"] += 1
            stats["by_new_category"][new_category] = (
                stats["by_new_category"].get(new_category, 0) + 1
            )
            print(f"  -> {new_category}")

            if not dry_run:
                rows[row_idx]["Category"] = new_category
        else:
            stats["still_unknown"] += 1
            print(f"  -> Still UNKNOWN")

    # Write output
    if not dry_run and stats["reclassified"] > 0:
        with open(output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Reclassify UNKNOWN projects using Gemini AI"
    )
    parser.add_argument(
        "--file",
        default="output/category_projects_for_test_training.csv",
        help="Path to CSV file",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file path (default: overwrite input file)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show classifications without modifying the file",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of UNKNOWN projects to process",
    )
    args = parser.parse_args()

    print("Reclassifying UNKNOWN Projects with Gemini AI")
    print("=" * 50)

    stats = reclassify_unknown(
        args.file,
        output_file=args.output,
        dry_run=args.dry_run,
        limit=args.limit,
    )

    print("\n" + "=" * 50)
    print(f"{'[DRY RUN] ' if args.dry_run else ''}Results:")
    print("-" * 40)
    print(f"Total projects: {stats['total_projects']}")
    print(f"UNKNOWN found: {stats['unknown_found']}")
    print(f"Reclassified: {stats['reclassified']}")
    print(f"Still UNKNOWN: {stats['still_unknown']}")

    if stats["by_new_category"]:
        print("\nReclassification breakdown:")
        for cat, count in sorted(
            stats["by_new_category"].items(), key=lambda x: -x[1]
        ):
            print(f"  {cat}: {count}")

    if not args.dry_run and stats["reclassified"] > 0:
        print(f"\nFile updated: {args.output or args.file}")


if __name__ == "__main__":
    main()
