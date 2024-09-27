import difflib
from typing import List


def generate_commit_message(old_state: str, new_state: str) -> str:
    diff = list(
        difflib.unified_diff(
            old_state.splitlines(), new_state.splitlines(), lineterm=""
        )
    )

    changes = []
    current_file = None
    for line in diff:
        if line.startswith("+++"):
            current_file = line[4:].strip()
        elif line.startswith("+") and current_file:
            changes.append(f"Added in {current_file}: {line[1:].strip()}")
        elif line.startswith("-") and current_file:
            changes.append(f"Removed from {current_file}: {line[1:].strip()}")

    if not changes:
        return "No significant changes detected"

    summary = "Update project:\n" + "\n".join(changes[:5])  # Limit to 5 changes
    if len(changes) > 5:
        summary += f"\n... and {len(changes) - 5} more changes"

    return summary


def get_project_state(project_id: str) -> str:
    # This function should return a string representation of the current project state
    # You'll need to implement this based on how you store project data
    pass


def save_commit_message(project_id: str, commit_message: str):
    # This function should save or use the commit message as needed in your system
    # You'll need to implement this based on your requirements
    pass
