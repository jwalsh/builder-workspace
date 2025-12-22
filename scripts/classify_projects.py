#!/usr/bin/env python3
"""
Classify projects based on name and description using keyword matching.

This provides a fast first-pass classification for the projects directory.
AI-based refinement can be applied afterward.
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Keyword patterns for category matching (case-insensitive)
CATEGORY_KEYWORDS = {
    "SECURITY": [
        r"security", r"cyber", r"threat", r"vulnerability", r"intrusion",
        r"firewall", r"encryption", r"auth", r"fraud", r"malware", r"pentest",
        r"soc\b", r"siem", r"zero.?trust", r"deception"
    ],
    "HEALTHCARE": [
        r"health", r"medical", r"patient", r"clinic", r"hospital", r"diagnosis",
        r"therapy", r"pharma", r"drug", r"symptom", r"wellness", r"fitness",
        r"santé", r"salud", r"medic"
    ],
    "AI_ML": [
        r"\bai\b", r"machine.?learn", r"deep.?learn", r"neural", r"nlp",
        r"language.?model", r"llm", r"gpt", r"transformer", r"embedding",
        r"intelligence.?artificielle", r"inteligencia.?artificial"
    ],
    "EDUCATION": [
        r"learn", r"education", r"training", r"tutor", r"course", r"student",
        r"teach", r"school", r"university", r"curriculum", r"éducation",
        r"educación", r"formation"
    ],
    "FINANCE": [
        r"financ", r"bank", r"trading", r"invest", r"stock", r"crypto",
        r"payment", r"transaction", r"audit", r"accounting", r"finanz"
    ],
    "ENERGY": [
        r"energy", r"power", r"grid", r"solar", r"wind", r"renewable",
        r"electric", r"battery", r"énergie", r"energía"
    ],
    "ENVIRONMENTAL": [
        r"environment", r"climate", r"carbon", r"emission", r"pollution",
        r"recycl", r"sustain", r"eco", r"green"
    ],
    "AUTONOMOUS_SYSTEMS": [
        r"autonomous", r"self.?driving", r"robot", r"drone", r"uav",
        r"autónom", r"autonome"
    ],
    "QUANTUM": [
        r"quantum", r"qubit", r"quantique", r"cuántico"
    ],
    "BLOCKCHAIN": [
        r"blockchain", r"smart.?contract", r"defi", r"nft", r"ledger",
        r"ethereum", r"bitcoin"
    ],
    "IOT": [
        r"\biot\b", r"sensor", r"embedded", r"smart.?device", r"wearable"
    ],
    "XR": [
        r"\bvr\b", r"\bar\b", r"\bxr\b", r"virtual.?reality", r"augmented",
        r"holograph", r"immersive", r"metaverse"
    ],
    "BCI": [
        r"brain", r"neuro", r"neural.?interface", r"bci", r"eeg",
        r"neurofeedback", r"cognitive"
    ],
    "INFRASTRUCTURE": [
        r"infrastructure", r"devops", r"kubernetes", r"docker", r"cloud",
        r"deploy", r"orchestrat", r"container"
    ],
    "SOFTWARE_ENGINEERING": [
        r"code", r"developer", r"programming", r"compiler", r"debug",
        r"refactor", r"testing", r"ide", r"git"
    ],
    "LOGISTICS": [
        r"logistics", r"supply.?chain", r"warehouse", r"shipping", r"fleet",
        r"transport", r"delivery"
    ],
    "HR": [
        r"\bhr\b", r"human.?resource", r"recruit", r"talent", r"employee",
        r"workforce", r"hiring", r"onboard"
    ],
    "MARKETING": [
        r"marketing", r"campaign", r"advertis", r"brand", r"customer",
        r"engagement", r"analytics"
    ],
    "LEGAL": [
        r"legal", r"contract", r"compliance", r"regulation", r"law",
        r"patent", r"intellectual.?property"
    ],
    "GAMING": [
        r"game", r"gaming", r"player", r"esport", r"quest", r"level"
    ],
    "ENTERTAINMENT": [
        r"entertainment", r"media", r"stream", r"music", r"video", r"content"
    ],
    "REAL_ESTATE": [
        r"real.?estate", r"property", r"housing", r"building", r"construction"
    ],
    "SPACE": [
        r"space", r"satellite", r"astro", r"rocket", r"orbit", r"mars",
        r"cosmic", r"exoplanet"
    ],
    "MILITARY": [
        r"military", r"defense", r"battlefield", r"combat", r"weapon"
    ],
    "PETS": [
        r"pet", r"animal", r"veterinar", r"mascota"
    ],
    "RETAIL": [
        r"retail", r"shop", r"store", r"ecommerce", r"checkout", r"inventory"
    ],
    "SIMULATION": [
        r"simulat", r"digital.?twin", r"model", r"virtual.?test"
    ],
    "PRODUCTIVITY": [
        r"productiv", r"workflow", r"task", r"automat", r"efficienc"
    ],
    "DOCUMENTATION": [
        r"document", r"rfc", r"spec", r"api.?doc", r"readme"
    ],
    "PHILOSOPHY": [
        r"ethic", r"philosoph", r"moral", r"bias"
    ],
    "BIOTECH": [
        r"biotech", r"genetic", r"dna", r"protein", r"cell", r"bio"
    ],
    "HCI": [
        r"interface", r"ux", r"ui", r"accessibility", r"interaction"
    ],
    "SOCIAL_MEDIA": [
        r"social", r"community", r"network", r"chat", r"messaging"
    ],
    "TRAVEL": [
        r"travel", r"tourism", r"hotel", r"flight", r"booking"
    ],
    "AGRICULTURAL": [
        r"agricult", r"farm", r"crop", r"soil", r"irrigation", r"agri"
    ],
    "URBAN": [
        r"urban", r"city", r"smart.?city", r"traffic", r"parking"
    ],
    "CLOUD": [
        r"cloud", r"saas", r"paas", r"serverless", r"aws", r"azure", r"gcp"
    ],
    "COMMUNICATIONS": [
        r"communi", r"telecom", r"5g", r"network", r"protocol"
    ],
    "MANUFACTURING": [
        r"manufactur", r"factory", r"3d.?print", r"industrial", r"assembly"
    ],
}


def classify_by_keywords(name: str, description: str = "") -> str:
    """
    Classify a project based on name and description using keyword matching.

    Args:
        name: Project name
        description: Project description (optional)

    Returns:
        Category name or UNKNOWN
    """
    text = f"{name} {description}".lower()

    scores = {}
    for category, patterns in CATEGORY_KEYWORDS.items():
        score = 0
        for pattern in patterns:
            matches = len(re.findall(pattern, text, re.IGNORECASE))
            score += matches
        if score > 0:
            scores[category] = score

    if scores:
        # Return category with highest score
        return max(scores.items(), key=lambda x: x[1])[0]

    return "UNKNOWN"


def classify_projects_directory(
    projects_dir: str = "projects",
    dry_run: bool = False,
    limit: int = None,
) -> dict:
    """
    Classify all projects in the projects directory.

    Args:
        projects_dir: Path to projects directory
        dry_run: If True, only report changes
        limit: Maximum number of projects to process

    Returns:
        Statistics dictionary
    """
    projects_path = Path(projects_dir)
    if not projects_path.exists():
        raise FileNotFoundError(f"Directory not found: {projects_dir}")

    stats = {
        "total": 0,
        "classified": 0,
        "already_classified": 0,
        "still_unknown": 0,
        "by_category": {},
    }

    project_dirs = sorted(projects_path.iterdir())
    if limit:
        project_dirs = project_dirs[:limit]

    for project_dir in project_dirs:
        if not project_dir.is_dir():
            continue

        stats["total"] += 1
        info_file = project_dir / "project_info.json"

        # Load or create project info
        info = {}
        if info_file.exists():
            try:
                with open(info_file) as f:
                    info = json.load(f)
            except:
                pass

        current_category = info.get("category", "")

        # Skip if already classified
        if current_category and current_category != "UNKNOWN":
            stats["already_classified"] += 1
            continue

        # Classify based on name and description
        description = info.get("description", "")
        new_category = classify_by_keywords(project_dir.name, description)

        if new_category != "UNKNOWN":
            stats["classified"] += 1
            stats["by_category"][new_category] = (
                stats["by_category"].get(new_category, 0) + 1
            )

            if not dry_run:
                info["category"] = new_category
                info["category_method"] = "keyword_match"
                info["category_updated"] = datetime.now().isoformat()

                with open(info_file, "w") as f:
                    json.dump(info, f, indent=2)

            if stats["total"] <= 20 or stats["classified"] <= 10:
                print(f"  {project_dir.name} -> {new_category}")
        else:
            stats["still_unknown"] += 1

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Classify projects using keyword matching"
    )
    parser.add_argument(
        "--dir",
        default="projects",
        help="Projects directory (default: projects)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show classifications without modifying files",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of projects to process",
    )
    args = parser.parse_args()

    print("Classifying Projects with Keyword Matching")
    print("=" * 50)

    stats = classify_projects_directory(
        args.dir,
        dry_run=args.dry_run,
        limit=args.limit,
    )

    print("\n" + "=" * 50)
    print(f"{'[DRY RUN] ' if args.dry_run else ''}Results:")
    print("-" * 40)
    print(f"Total projects: {stats['total']}")
    print(f"Already classified: {stats['already_classified']}")
    print(f"Newly classified: {stats['classified']}")
    print(f"Still UNKNOWN: {stats['still_unknown']}")

    if stats["by_category"]:
        print("\nClassification breakdown (top 20):")
        for cat, count in sorted(
            stats["by_category"].items(), key=lambda x: -x[1]
        )[:20]:
            print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
