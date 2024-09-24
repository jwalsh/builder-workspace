# File: coordinator/project_operations/project_management.py

import asyncio
import logging
import sqlite3
from typing import List
from ..models import ProjectDefinition, Task, TaskType
from ..db import add_project_version, add_task, get_db_path, get_tasks, update_task
from ..utils import create_project_directory
from .decompose import decompose_project
from .rfc_processing import process_rfc


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
