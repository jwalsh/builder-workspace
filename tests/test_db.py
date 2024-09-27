import os
import sqlite3

import pytest

from coordinator.db import (
    add_project_version,
    add_task,
    create_tables,
    delete_project,
    get_all_projects,
    get_db_path,
    get_project_version,
    get_tasks,
    update_task,
)
from coordinator.models import RFCState, Task, TaskType


@pytest.fixture(scope="function")
def test_db_path(tmp_path):
    db_path = tmp_path / "test.db"
    old_db_path = os.environ.get("DB_PATH")
    os.environ["DB_PATH"] = str(db_path)
    yield str(db_path)
    if old_db_path:
        os.environ["DB_PATH"] = old_db_path
    else:
        del os.environ["DB_PATH"]
    if os.path.exists(str(db_path)):
        os.unlink(str(db_path))


@pytest.fixture(scope="function")
def db_connection(test_db_path):
    create_tables()
    conn = sqlite3.connect(test_db_path)
    yield conn
    conn.close()


def test_get_db_path(test_db_path):
    assert get_db_path() == test_db_path


def test_create_tables(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert ("tasks",) in tables
    assert ("project_versions",) in tables


def test_add_project_version(db_connection):
    project_id = "test_project"
    definition = '{"name": "Test Project", "description": "A test project"}'
    add_project_version(project_id, definition)

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM project_versions WHERE id = ?", (project_id,))
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == project_id
    assert result[1] == definition


def test_add_and_get_tasks(db_connection):
    task = Task(
        id=0,
        project_id="test_project",
        title="Test Task",
        description="A test task",
        status="TODO",
        assigned_to="tester",
        priority=1,
        dependencies=[],
        task_type=TaskType.RFC,
        rfc_state=RFCState.DRAFT,
    )

    task_id = add_task(task)
    assert task_id is not None

    tasks = get_tasks("test_project")
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task"
    assert tasks[0].task_type == TaskType.RFC
    assert tasks[0].rfc_state == RFCState.DRAFT


def test_update_task(db_connection):
    task = Task(
        id=0,
        project_id="test_project",
        title="Original Task",
        description="Original description",
        status="TODO",
        assigned_to="tester",
        priority=1,
        dependencies=[],
        task_type=TaskType.RFC,
        rfc_state=RFCState.DRAFT,
    )

    task_id = add_task(task)
    task.id = task_id
    task.title = "Updated Task"
    task.status = "IN_PROGRESS"

    update_task(task)

    updated_tasks = get_tasks("test_project")
    assert len(updated_tasks) == 1
    assert updated_tasks[0].title == "Updated Task"
    assert updated_tasks[0].status == "IN_PROGRESS"


def test_get_project_version(db_connection):
    project_id = "test_project"
    definition = '{"name": "Test Project", "description": "A test project"}'
    add_project_version(project_id, definition)

    retrieved_definition = get_project_version(project_id)
    assert retrieved_definition == definition


def test_delete_project(db_connection):
    project_id = "test_project"
    definition = '{"name": "Test Project", "description": "A test project"}'
    add_project_version(project_id, definition)

    task = Task(
        id=0,
        project_id=project_id,
        title="Test Task",
        description="A test task",
        status="TODO",
        assigned_to="tester",
        priority=1,
        dependencies=[],
        task_type=TaskType.RFC,
        rfc_state=RFCState.DRAFT,
    )
    add_task(task)

    delete_project(project_id)

    assert get_project_version(project_id) is None
    assert len(get_tasks(project_id)) == 0


def test_get_all_projects(db_connection):
    projects = [
        ("project1", '{"name": "Project 1", "description": "First project"}'),
        ("project2", '{"name": "Project 2", "description": "Second project"}'),
    ]

    for project_id, definition in projects:
        add_project_version(project_id, definition)

    all_projects = get_all_projects()
    assert len(all_projects) == 2
    assert (
        "project1",
        {"name": "Project 1", "description": "First project"},
    ) in all_projects
    assert (
        "project2",
        {"name": "Project 2", "description": "Second project"},
    ) in all_projects
