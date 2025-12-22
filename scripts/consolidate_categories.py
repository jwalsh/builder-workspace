#!/usr/bin/env python3
"""
Consolidate duplicate/redundant categories in project CSV files.

This script applies the conservative category consolidation mapping
to update Category column in the training data CSV.
"""

import argparse
import csv
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from analyzer.utils.category_mapping import (
    CATEGORY_CONSOLIDATION,
    get_canonical_category,
    is_deprecated_category,
)


def consolidate_csv_categories(
    input_file: str = "output/category_projects_for_test_training.csv",
    output_file: str = None,
    dry_run: bool = False,
) -> dict:
    """
    Apply category consolidation mapping to a CSV file.

    Args:
        input_file: Path to the input CSV file
        output_file: Path to output file (defaults to overwriting input)
        dry_run: If True, only report changes without modifying the file

    Returns:
        Dictionary with consolidation statistics
    """
    filepath = Path(input_file)
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {input_file}")

    if output_file is None:
        output_file = input_file

    stats = {
        "total_projects": 0,
        "consolidated": 0,
        "by_category": {},
    }

    rows = []
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            stats["total_projects"] += 1
            old_category = row["Category"]

            if is_deprecated_category(old_category):
                new_category = get_canonical_category(old_category)
                stats["consolidated"] += 1

                key = f"{old_category} -> {new_category}"
                stats["by_category"][key] = stats["by_category"].get(key, 0) + 1

                row["Category"] = new_category

            rows.append(row)

    if not dry_run and stats["consolidated"] > 0:
        with open(output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Consolidate duplicate categories in project CSV"
    )
    parser.add_argument(
        "--file",
        default="output/category_projects_for_test_training.csv",
        help="Path to CSV file (default: output/category_projects_for_test_training.csv)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file path (default: overwrite input file)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying the file",
    )
    args = parser.parse_args()

    print("Category Consolidation Mapping:")
    print("-" * 40)
    for old, new in CATEGORY_CONSOLIDATION.items():
        print(f"  {old} -> {new}")
    print()

    stats = consolidate_csv_categories(
        args.file, output_file=args.output, dry_run=args.dry_run
    )

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Results:")
    print("-" * 40)
    print(f"Total projects scanned: {stats['total_projects']}")
    print(f"Projects consolidated: {stats['consolidated']}")

    if stats["by_category"]:
        print("\nConsolidation breakdown:")
        for mapping, count in stats["by_category"].items():
            print(f"  {mapping}: {count}")

    if not args.dry_run and stats["consolidated"] > 0:
        print(f"\nFile updated: {args.output or args.file}")
    elif args.dry_run and stats["consolidated"] > 0:
        print("\nRun without --dry-run to apply changes")


if __name__ == "__main__":
    main()
