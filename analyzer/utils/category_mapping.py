"""Category consolidation mapping for cleaning up duplicate/redundant categories."""

from typing import Dict

# Conservative consolidation: only exact duplicates
CATEGORY_CONSOLIDATION: Dict[str, str] = {
    "EDUCATION_AND_TRAINING": "EDUCATION",
    "FINANCE_AND_BANKING": "FINANCE",
    "RENEWABLE_ENERGY": "ENERGY",
}


def get_canonical_category(category: str) -> str:
    """Return the canonical category name, applying consolidation mapping.

    Args:
        category: The original category name

    Returns:
        The canonical category name (consolidated if applicable)
    """
    return CATEGORY_CONSOLIDATION.get(category, category)


def get_all_mappings() -> Dict[str, str]:
    """Return the full consolidation mapping dictionary."""
    return CATEGORY_CONSOLIDATION.copy()


def is_deprecated_category(category: str) -> bool:
    """Check if a category has been deprecated/consolidated."""
    return category in CATEGORY_CONSOLIDATION
