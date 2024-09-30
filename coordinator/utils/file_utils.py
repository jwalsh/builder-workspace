import json
import os
import logging
from datetime import datetime
from typing import List
from ..models import Task  # Adjust this import based on your actual project structure


def create_project_directory(project_name: str, description: str, tasks: List[Task]):
    project_dir = os.path.abspath(os.path.join("projects", project_name, "config"))
    os.makedirs(project_dir, exist_ok=True)

    project_info = {
        "name": project_name,
        "description": description,
        "created_at": datetime.now().isoformat(),
    }

    project_info_path = os.path.join(project_dir, "project_info.json")
    tasks_path = os.path.join(project_dir, "tasks.json")

    with open(project_info_path, "w") as f:
        json.dump(project_info, f, indent=2)
    logging.info(f"Updated project_info.json: {os.path.abspath(project_info_path)}")

    with open(tasks_path, "w") as f:
        json.dump([task.dict() for task in tasks], f, indent=2)
    logging.info(f"Updated tasks.json: {os.path.abspath(tasks_path)}")

    logging.info(f"Project directory created/updated: {project_dir}")


def sanitize_filename(filename: str) -> str:
    # Remove invalid characters and replace spaces with underscores
    sanitized = re.sub(r"[^\w\-_\. ]", "", filename)
    sanitized = sanitized.replace(" ", "_")
    return sanitized[:255]  # Truncate to 255 characters
