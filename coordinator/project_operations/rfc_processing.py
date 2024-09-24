# File: coordinator/project_operations/rfc_processing.py

import logging
from typing import Optional
from ..models import Task, ProjectDefinition, TaskType, RFCState, ImplementationState
from ..db import update_task
from ..llm import llm_manager
from ..utils import extract_json_from_response


async def process_rfc(task: Task, project_definition: ProjectDefinition) -> Task:
    logging.info(f"Processing RFC task: {task.id} - {task.title}")

    prompt = f"""Review and update the following RFC task:

Project Name: {project_definition.name}
Description: {project_definition.description}

Task:
{task.model_dump_json(indent=2)}

Please review the RFC and suggest any necessary changes or improvements. If the RFC is ready for the next state, update the rfc_state field accordingly. Provide your response as a JSON object with the updated task fields. Ensure that the 'assigned_to' field is one of the following: task-decomposer, project-manager, code-architect, frontend-developer, backend-developer, database-specialist, devops-engineer, qa-tester, security-specialist, technical-writer"""

    cache_key = (
        f"process_rfc_{task.id}_{task.rfc_state.value if task.rfc_state else 'UNKNOWN'}"
    )

    try:
        updated_task_response = await llm_manager.run_llm_command(
            prompt, cache_key, "code-architect"
        )
    except Exception as e:
        logging.error(f"Error getting LLM response for task {task.id}: {str(e)}")
        return task

    if not updated_task_response:
        logging.error(f"No response received from LLM for task {task.id}")
        return task

    updated_task_data = extract_json_from_response(updated_task_response)

    if not updated_task_data:
        logging.error(f"Failed to extract valid JSON for task {task.id}")
        return task

    try:
        # Ensure we're only updating fields that exist in the Task model
        valid_fields = task.model_fields.keys()
        filtered_data = {
            k: v for k, v in updated_task_data.items() if k in valid_fields
        }

        # Handle enum fields
        if "task_type" in filtered_data:
            filtered_data["task_type"] = parse_enum(
                TaskType, filtered_data["task_type"], task.task_type
            )

        if "rfc_state" in filtered_data:
            filtered_data["rfc_state"] = parse_enum(
                RFCState, filtered_data["rfc_state"], task.rfc_state
            )

        if "implementation_state" in filtered_data:
            filtered_data["implementation_state"] = parse_enum(
                ImplementationState,
                filtered_data["implementation_state"],
                task.implementation_state,
            )

        # Validate assigned_to field
        valid_agents = [
            "task-decomposer",
            "project-manager",
            "code-architect",
            "frontend-developer",
            "backend-developer",
            "database-specialist",
            "devops-engineer",
            "qa-tester",
            "security-specialist",
            "technical-writer",
        ]
        if (
            "assigned_to" in filtered_data
            and filtered_data["assigned_to"] not in valid_agents
        ):
            logging.warning(
                f"Invalid assigned_to value for task {task.id}. Keeping original value."
            )
            filtered_data.pop("assigned_to")

        # Update the task with the filtered data
        updated_task = task.model_copy(update=filtered_data)
        update_task(updated_task)

        logging.info(
            f"Processed RFC task: {updated_task.title} (New state: {updated_task.rfc_state})"
        )
        return updated_task

    except Exception as e:
        logging.error(f"Error processing RFC task {task.id}: {str(e)}")
        return task


def parse_enum(enum_class, value: Optional[str], default):
    if value is None:
        return default
    try:
        return enum_class(value)
    except ValueError:
        logging.warning(
            f"Invalid {enum_class.__name__} value: {value}. Keeping original value."
        )
        return default
