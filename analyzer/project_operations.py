# File: analyzer/project_operations.py

import logging
from difflib import get_close_matches
from typing import List
import json

from coordinator.models import RFCState, Task, ProjectDefinition, TaskType
from coordinator.llm import llm_manager
from coordinator.utils import generate_cache_key
from coordinator.db import add_task


async def decompose_project(project_definition: ProjectDefinition) -> List[Task]:
    prompt = f"""
    Decompose the following project into a list of tasks:
    Project Name: {project_definition.name}
    Project Description: {project_definition.description}

    Please provide a list of tasks required to complete this project. 
    Each task should include a title, description, status (default to "TODO"), 
    assigned_to (leave empty for now), priority (1-5, with 5 being highest), 
    and any dependencies (list of task titles).

    Return the tasks as a JSON array of task objects.
    """

    cache_key = generate_cache_key(prompt, "project_decomposer")
    response = await llm_manager.run_llm_command(
        prompt, cache_key, "project_decomposer"
    )

    tasks = []
    try:
        task_list = json.loads(response)
        for task_data in task_list:
            task = Task(
                id=0,  # This will be set when added to the database
                project_id=project_definition.name,
                title=task_data["title"],
                description=task_data["description"],
                status=task_data.get("status", "TODO"),
                assigned_to=task_data.get("assigned_to", ""),
                priority=task_data.get("priority", 3),
                dependencies=task_data.get("dependencies", []),
                task_type=(
                    TaskType.RFC
                    if task_data.get("is_rfc", False)
                    else TaskType.IMPLEMENTATION
                ),
                rfc_state=RFCState.DRAFT if task_data.get("is_rfc", False) else None,
            )
            tasks.append(task)
    except json.JSONDecodeError:
        logging.error(
            f"Failed to parse JSON response for project decomposition: {response}"
        )
    except KeyError as e:
        logging.error(f"Missing key in task data: {e}")

    return tasks


def fuzzy_match_rfc_state(state_str):
    state_str = state_str.upper().replace(" ", "_")
    valid_states = [s.name for s in RFCState]
    matches = get_close_matches(state_str, valid_states, n=1, cutoff=0.6)
    return matches[0] if matches else None


async def process_rfc(task: Task, project_definition: ProjectDefinition) -> Task:
    prompt = f"""
    Review and update the following RFC task for the project {project_definition.name}:
    {task.title}
    {task.description}
    Current status: {task.status}
    Current RFC state: {task.rfc_state}
    
    Please provide any necessary updates, changes, or next steps for this RFC.
    Return the full updated task information in a Python dictionary format.
    """

    cache_key = generate_cache_key(prompt, "rfc_processor")
    response = await llm_manager.run_llm_command(prompt, cache_key, "rfc_processor")

    try:
        # Assume the response is already a Python dictionary
        updated_task_dict = response

        # Update the task with the new information
        for key, value in updated_task_dict.items():
            if key == "rfc_state":
                continue  # We'll handle this separately
            if hasattr(task, key):
                setattr(task, key, value)

        # Handle the RFCState separately with fuzzy matching and default
        new_state = updated_task_dict.get("rfc_state")
        if new_state:
            matched_state = fuzzy_match_rfc_state(new_state)
            if matched_state:
                task.rfc_state = RFCState[matched_state]
                if matched_state != new_state:
                    logging.info(f"Mapped RFC state '{new_state}' to '{matched_state}'")
            else:
                logging.warning(
                    f"Invalid RFCState value: {new_state}. Setting to UNKNOWN."
                )
                task.rfc_state = RFCState.UNKNOWN
        else:
            logging.warning(f"No RFCState provided. Setting to UNKNOWN.")
            task.rfc_state = RFCState.UNKNOWN

        logging.info(
            f"Processed RFC task: {task.title} for {task.project_id} (New state: {task.rfc_state})"
        )
    except Exception as e:
        logging.error(f"Error processing RFC task {task.id}: {str(e)}")
        logging.warning(f"Setting RFCState to UNKNOWN due to processing error.")
        task.rfc_state = RFCState.UNKNOWN

    return task


async def implement_task(task: Task, project_definition: ProjectDefinition) -> Task:
    prompt = f"""
    Implement the following task for the project {project_definition.name}:
    {task.title}
    {task.description}
    Current status: {task.status}
    
    Please provide the implementation details or next steps for this task.
    Return the updated task information in a Python dictionary format.
    """

    cache_key = generate_cache_key(prompt, "task_implementer")
    response = await llm_manager.run_llm_command(prompt, cache_key, "task_implementer")

    try:
        updated_task_dict = response

        for key, value in updated_task_dict.items():
            if hasattr(task, key):
                setattr(task, key, value)

        logging.info(f"Implemented task: {task.title} for {task.project_id}")
    except Exception as e:
        logging.error(f"Error implementing task {task.id}: {str(e)}")

    return task


async def review_implementation(
    task: Task, project_definition: ProjectDefinition
) -> Task:
    prompt = f"""
    Review the implementation of the following task for the project {project_definition.name}:
    {task.title}
    {task.description}
    Current status: {task.status}
    
    Please review the implementation and provide feedback or approval.
    Return the updated task information in a Python dictionary format.
    """

    cache_key = generate_cache_key(prompt, "implementation_reviewer")
    response = await llm_manager.run_llm_command(
        prompt, cache_key, "implementation_reviewer"
    )

    try:
        updated_task_dict = response

        for key, value in updated_task_dict.items():
            if hasattr(task, key):
                setattr(task, key, value)

        logging.info(
            f"Reviewed implementation of task: {task.title} for {task.project_id}"
        )
    except Exception as e:
        logging.error(f"Error reviewing implementation of task {task.id}: {str(e)}")

    return task


# Add any other project operation functions here as needed
