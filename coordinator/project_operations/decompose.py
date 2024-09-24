import logging
from typing import List
from ..models import ProjectDefinition, Task, TaskType, RFCState
from ..llm import llm_manager
from ..prompts import AVAILABLE_AGENTS
from ..utils import extract_json_from_response

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
