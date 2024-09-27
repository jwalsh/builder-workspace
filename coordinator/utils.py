import json
import os
import re
import hashlib
from datetime import datetime
from typing import List

from .models import RFCState, Task, TaskType

import json
import re


def extract_json_from_response(text: str) -> dict:
    start = text.find("{")
    if start != -1:
        end_match = re.search(r"^}", text[start:], re.MULTILINE)
        if end_match:
            end = start + end_match.end()
            json_text = text[start:end]
            try:
                return json.loads(json_text)
            except json.JSONDecodeError:
                return {}
    return {}


def create_project_directory(project_name: str, description: str, tasks: List[Task]):
    project_dir = os.path.join("projects", project_name)
    os.makedirs(project_dir, exist_ok=True)

    with open(os.path.join(project_dir, "project_info.json"), "w") as f:
        json.dump({"name": project_name, "description": description}, f, indent=2)

    with open(os.path.join(project_dir, "tasks.json"), "w") as f:
        json.dump([task.dict() for task in tasks], f, indent=2)


def generate_cache_key(prompt: str, role: str) -> str:
    return hashlib.md5(f"{prompt}:{role}".encode()).hexdigest()


def sanitize_filename(filename: str) -> str:
    # Remove invalid characters and replace spaces with underscores
    sanitized = re.sub(r"[^\w\-_\. ]", "", filename)
    sanitized = sanitized.replace(" ", "_")
    return sanitized[:255]  # Truncate to 255 characters


def format_time_estimate(hours: float) -> str:
    if hours < 1:
        return f"{int(hours * 60)} minutes"
    elif hours < 24:
        return f"{hours:.1f} hours"
    else:
        days = hours / 24
        return f"{days:.1f} days"


def parse_dependencies(dependencies_str: str) -> List[str]:
    return [dep.strip() for dep in dependencies_str.split(",") if dep.strip()]


def generate_task_id(project_id: str, title: str) -> str:
    return hashlib.md5(f"{project_id}:{title}".encode()).hexdigest()[:8]


def calculate_project_progress(tasks: List[Task]) -> float:
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.status == "COMPLETED")
    return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0


def format_org_mode_task(task: Task) -> str:
    status = "DONE" if task.status == "COMPLETED" else "TODO"
    org_task = f"* {status} {task.title}\n"
    org_task += f"  :PROPERTIES:\n"
    org_task += f"  :ID: {task.id}\n"
    org_task += f"  :PRIORITY: {task.priority}\n"
    org_task += f"  :ASSIGNED: {task.assigned_to}\n"
    org_task += f"  :END:\n\n"
    org_task += f"  {task.description}\n\n"
    if task.dependencies:
        org_task += f"  Dependencies: {', '.join(task.dependencies)}\n"
    return org_task


def generate_project_summary(
    project_name: str, description: str, tasks: List[Task]
) -> str:
    progress = calculate_project_progress(tasks)
    summary = f"* Project: {project_name}\n"
    summary += f"  :PROPERTIES:\n"
    summary += f"  :PROGRESS: {progress:.1f}%\n"
    summary += f"  :END:\n\n"
    summary += f"  {description}\n\n"
    summary += "** Tasks\n"
    for task in tasks:
        summary += format_org_mode_task(task)
    return summary


def validate_email(email: str) -> bool:
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))


def is_valid_url(url: str) -> bool:
    url_regex = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
    return bool(re.match(url_regex, url))


def truncate_string(string: str, max_length: int) -> str:
    return string[: max_length - 3] + "..." if len(string) > max_length else string


def format_file_size(size_in_bytes: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.1f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f} PB"
