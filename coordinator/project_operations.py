import asyncio
import json
import logging
import sqlite3
from typing import List

import logging
from typing import Optional

from .models import Task, ProjectDefinition, TaskType, RFCState, ImplementationState
from .llm import llm_manager
from .db import add_project_version, add_task, get_db_path, get_tasks, update_task
from .prompts import AVAILABLE_AGENTS
from .utils import create_project_directory, extract_json_from_response


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


def show_project_summary():
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """
            SELECT project_id, COUNT(*) as task_count
            FROM tasks
            GROUP BY project_id
            ORDER BY project_id
        """
        )
        projects = c.fetchall()
        print("Projects and task counts:")
        for project, count in projects:
            print(f"{project}: {count} tasks")
    except sqlite3.Error as e:
        logging.error(f"Error showing project summary: {e}")
    finally:
        conn.close()


def show_project_tasks(project_name: str):
    tasks = get_tasks(project_name)

    if not tasks:
        print(
            f"Warning: No tasks found for project '{project_name}'. The project may not have been decomposed yet."
        )
        return

    print(f"Tasks for project '{project_name}':")
    for task in tasks:
        print(
            f"ID: {task.id}, Priority: {task.priority}, Title: {task.title}, Status: {task.status}, Assigned: {task.assigned_to}, Type: {task.task_type}, RFC State: {task.rfc_state}"
        )


async def process_project(
    name: str, description: str, force: bool, process_rfcs: bool = True
):
    try:
        project_definition = ProjectDefinition(name=name, description=description)

        add_project_version(project_definition.name, project_definition.json())

        existing_tasks = get_tasks(project_definition.name)

        if not existing_tasks or force:
            if existing_tasks and force:
                print(
                    f"\nForce flag used. Re-decomposing project '{project_definition.name}' into tasks..."
                )
            else:
                print("\nDecomposing project into tasks...")

            initial_tasks = await decompose_project(project_definition)

            for task in initial_tasks:
                task_id = add_task(task)
                if task_id:
                    task.id = task_id
                    print(
                        f"Added task: {task.title} (Type: {task.task_type}, Assigned to: {task.assigned_to})"
                    )
                else:
                    logging.error(f"Failed to add task: {task.title}")

            create_project_directory(
                project_definition.name, project_definition.description, initial_tasks
            )
        else:
            print(
                f"\nTasks already exist for project '{project_definition.name}'. Skipping decomposition. Use --force to override."
            )

            create_project_directory(
                project_definition.name, project_definition.description, existing_tasks
            )

        if process_rfcs:
            print("\nProcessing RFC tasks...")
            rfc_tasks = [
                task
                for task in get_tasks(project_definition.name)
                if task.task_type == TaskType.RFC
            ]
            for rfc_task in rfc_tasks:
                try:
                    updated_rfc_task = await process_rfc(rfc_task, project_definition)
                    update_task(updated_rfc_task)
                    print(
                        f"Processed RFC task: {updated_rfc_task.title} (New state: {updated_rfc_task.rfc_state})"
                    )
                except Exception as e:
                    logging.error(f"Error processing RFC task {rfc_task.id}: {str(e)}")

        print(
            "\nProject setup complete. Tasks added to the database and project directory created."
        )
    except Exception as e:
        logging.error(f"An error occurred while processing the project: {str(e)}")
        raise
