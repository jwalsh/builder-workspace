import json
import logging
import os
import sqlite3
from datetime import datetime
from typing import List

from .models import RFCState, Task, TaskType


def get_db_path():
    return os.path.join(os.getcwd(), "tasks.db")


def create_tables():
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS tasks
                     (id INTEGER PRIMARY KEY,
                      project_id TEXT,
                      title TEXT,
                      description TEXT,
                      status TEXT,
                      assigned_to TEXT,
                      priority INTEGER,
                      dependencies TEXT,
                      task_type TEXT,
                      rfc_state TEXT)"""
        )
        c.execute(
            """CREATE TABLE IF NOT EXISTS project_versions
                     (id TEXT PRIMARY KEY,
                      definition TEXT,
                      created_at TIMESTAMP)"""
        )
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")
    finally:
        conn.close()


def add_project_version(project_id: str, definition: str):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """INSERT OR REPLACE INTO project_versions (id, definition, created_at)
                     VALUES (?, ?, ?)""",
            (project_id, definition, datetime.utcnow().isoformat()),
        )
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error adding project version: {e}")
    finally:
        conn.close()


def add_task(task: Task):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """INSERT INTO tasks (project_id, title, description, status, assigned_to, priority, dependencies, task_type, rfc_state)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                task.project_id,
                task.title,
                task.description,
                task.status,
                task.assigned_to,
                task.priority,
                json.dumps(task.dependencies),
                task.task_type.value,
                task.rfc_state.value if task.rfc_state else None,
            ),
        )
        task_id = c.lastrowid
        conn.commit()
        return task_id
    except sqlite3.Error as e:
        logging.error(f"Error adding task: {e}")
        return None
    finally:
        conn.close()


def get_tasks(project_id: str):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE project_id = ?", (project_id,))
        tasks = c.fetchall()
        return [
            Task(
                id=task[0],
                project_id=task[1],
                title=task[2],
                description=task[3],
                status=task[4],
                assigned_to=task[5],
                priority=task[6],
                dependencies=json.loads(task[7]),
                task_type=TaskType(task[8]),
                rfc_state=RFCState(task[9]) if task[9] else None,
            )
            for task in tasks
        ]
    except sqlite3.Error as e:
        logging.error(f"Error getting tasks: {e}")
        return []
    finally:
        conn.close()


def update_task(task: Task):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """UPDATE tasks SET
                     title = ?, description = ?, status = ?, assigned_to = ?,
                     priority = ?, dependencies = ?, task_type = ?, rfc_state = ?
                     WHERE id = ?""",
            (
                task.title,
                task.description,
                task.status,
                task.assigned_to,
                task.priority,
                json.dumps(task.dependencies),
                task.task_type.value,
                task.rfc_state.value if task.rfc_state else None,
                task.id,
            ),
        )
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error updating task: {e}")
    finally:
        conn.close()


def get_project_version(project_id: str):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute("SELECT definition FROM project_versions WHERE id = ?", (project_id,))
        result = c.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        logging.error(f"Error getting project version: {e}")
        return None
    finally:
        conn.close()


def delete_project(project_id: str):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE project_id = ?", (project_id,))
        c.execute("DELETE FROM project_versions WHERE id = ?", (project_id,))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error deleting project: {e}")
    finally:
        conn.close()


def get_all_projects():
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute("SELECT id, definition FROM project_versions")
        projects = c.fetchall()
        return [(project[0], json.loads(project[1])) for project in projects]
    except sqlite3.Error as e:
        logging.error(f"Error getting all projects: {e}")
        return []
    finally:
        conn.close()
