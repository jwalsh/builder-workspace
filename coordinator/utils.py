import hashlib
import json
import logging
import os
import re
from datetime import datetime
from typing import Any, Dict, List

from .models import Task


def extract_json_from_response(text: str) -> dict:
    try:
        # First, try to parse the entire text as JSON
        return json.loads(text)
    except json.JSONDecodeError:
        # If that fails, look for JSON-like content
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                logging.error(f"Failed to extract valid JSON from the response: {text}")
                return {}
        else:
            logging.error(f"No JSON-like content found in the response: {text}")
            return {}


def create_project_directory(project_name: str, description: str, tasks: List[Task]):
    projects_dir = os.path.join(os.getcwd(), "projects")
    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)

    project_path = os.path.join(projects_dir, project_name)

    try:
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            logging.info(f"Project directory created at: {project_path}")

        # Create a project info file
        with open(os.path.join(project_path, "project_info.json"), "w") as f:
            json.dump(
                {
                    "name": project_name,
                    "description": description,
                    "created_at": datetime.now().isoformat(),
                },
                f,
                indent=2,
            )

        # Create a tasks file
        with open(os.path.join(project_path, "tasks.json"), "w") as f:
            json.dump([task.dict() for task in tasks], f, indent=2)

        logging.info(f"Project info and tasks added at {project_path}")

    except OSError as e:
        logging.error(f"Error creating project directory: {e}")


def generate_cache_key(prompt: str, role: str) -> str:
    """Generate a unique cache key based on the prompt and role."""
    combined = f"{prompt}|{role}"
    return hashlib.md5(combined.encode()).hexdigest()


def sanitize_filename(filename: str) -> str:
    """
    Sanitize a string to be used as a filename.
    """
    # Remove invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', "", filename)
    # Replace spaces with underscores
    sanitized = sanitized.replace(" ", "_")
    # Limit length to 255 characters
    return sanitized[:255]


def format_time_estimate(hours: float) -> str:
    """Format a time estimate in hours to a human-readable string."""
    if hours < 1:
        return f"{int(hours * 60)} minutes"
    elif hours < 24:
        return f"{hours:.1f} hours"
    else:
        days = hours / 24
        return f"{days:.1f} days"


def parse_dependencies(dependencies_str: str) -> List[str]:
    """Parse a comma-separated string of dependencies into a list."""
    return [dep.strip() for dep in dependencies_str.split(",") if dep.strip()]


def generate_task_id(project_name: str, task_title: str) -> str:
    """Generate a unique task ID based on project name and task title."""
    combined = f"{project_name}|{task_title}"
    return hashlib.md5(combined.encode()).hexdigest()[:8]


def calculate_project_progress(tasks: List[Task]) -> float:
    """Calculate the overall progress of a project based on completed tasks."""
    if not tasks:
        return 0.0
    completed_tasks = sum(1 for task in tasks if task.status.lower() == "completed")
    return (completed_tasks / len(tasks)) * 100


def format_org_mode_task(task: Task) -> str:
    """Format a task in Org-mode syntax."""
    status = "DONE" if task.status.lower() == "completed" else "TODO"
    return f"""* {status} {task.title}
  :PROPERTIES:
  :ID: {task.id}
  :PRIORITY: {task.priority}
  :ASSIGNED: {task.assigned_to}
  :END:
  {task.description}
  
  Dependencies: {', '.join(task.dependencies)}
"""


def generate_project_summary(
    project_name: str, description: str, tasks: List[Task]
) -> str:
    """Generate a project summary in Org-mode format."""
    progress = calculate_project_progress(tasks)
    summary = f"""* Project: {project_name}
  :PROPERTIES:
  :PROGRESS: {progress:.1f}%
  :END:
  {description}

** Tasks
"""
    for task in tasks:
        summary += format_org_mode_task(task)

    return summary


def validate_email(email: str) -> bool:
    """Validate an email address."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_url(url: str) -> bool:
    """Check if a given string is a valid URL."""
    pattern = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(pattern, url) is not None


def truncate_string(s: str, max_length: int) -> str:
    """Truncate a string to a maximum length, adding an ellipsis if truncated."""
    return (s[: max_length - 3] + "...") if len(s) > max_length else s


def format_file_size(size_in_bytes: int) -> str:
    """Format a file size in bytes to a human-readable string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.1f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f} PB"
