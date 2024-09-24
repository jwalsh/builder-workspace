# File: coordinator/project_operations/decompose.py

import logging
from typing import List
from ..models import ProjectDefinition, Task, TaskType, RFCState
from ..llm import llm_manager
from ..prompts import AVAILABLE_AGENTS
from ..utils import extract_json_from_response


async def decompose_project(project_definition: ProjectDefinition) -> List[Task]:
    prompt = f"""Decompose the following project into initial high-level tasks:

Project Name: {project_definition.name}
Description: {project_definition.description}

Please provide a JSON array of tasks, where each task has the following structure:
{{
  "title": "Task title",
  "description": "Task description",
  "status": "TODO",
  "assigned_to": "Agent type (must be one of: {', '.join(AVAILABLE_AGENTS)})",
  "priority": 1-5 (1 being highest priority),
  "dependencies": ["Dependency task title", "Another dependency"],
  "task_type": "One of: rfc, decompose, rfc_review, code_review, audit",
  "rfc_state": "DRAFT (only if task_type is rfc, otherwise null)"
}}"""

    cache_key = f"decompose_project_{project_definition.name}"

    tasks_response = await llm_manager.run_llm_command(
        prompt, cache_key, "task-decomposer"
    )

    if not tasks_response:
        logging.error("No response received from LLM")
        return []

    logging.info(f"LLM Response: {tasks_response}")  # Log the full response

    tasks_data = extract_json_from_response(tasks_response)

    if not isinstance(tasks_data, list):
        logging.error(
            f"Invalid response format: expected a list of tasks, got {type(tasks_data)}"
        )
        logging.error(f"Response content: {tasks_data}")
        return []

    tasks = []
    for task in tasks_data:
        try:
            task_type = TaskType(task.get("task_type", "unknown").lower())
        except ValueError:
            task_type = TaskType.UNKNOWN

        rfc_state = None
        if task_type == TaskType.RFC:
            try:
                rfc_state = RFCState(task.get("rfc_state", "UNKNOWN").upper())
            except ValueError:
                rfc_state = RFCState.UNKNOWN

        if task["assigned_to"] not in AVAILABLE_AGENTS:
            task["assigned_to"] = (
                "project-manager"  # Default to project manager if invalid
            )

        tasks.append(
            Task(
                id=0,
                project_id=project_definition.name,
                title=task["title"],
                description=task["description"],
                status=task["status"],
                assigned_to=task["assigned_to"],
                priority=task["priority"],
                dependencies=task["dependencies"],
                task_type=task_type,
                rfc_state=rfc_state,
            )
        )

    logging.info(f"Created {len(tasks)} tasks")
    return tasks
