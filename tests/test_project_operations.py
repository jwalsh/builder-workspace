from unittest.mock import Mock, patch

import pytest

from coordinator.models import ProjectDefinition, RFCState, Task, TaskType
from coordinator.project_operations import decompose_project, process_rfc


@pytest.fixture
def mock_llm_manager():
    with patch("coordinator.project_operations.llm_manager") as mock:
        yield mock


def test_decompose_project(mock_llm_manager):
    # Mock the LLM response
    mock_llm_manager.run_llm_command.return_value = """
    [
        {
            "title": "Task 1",
            "description": "Description 1",
            "status": "TODO",
            "assigned_to": "project-manager",
            "priority": 1,
            "dependencies": [],
            "task_type": "rfc",
            "rfc_state": "DRAFT"
        },
        {
            "title": "Task 2",
            "description": "Description 2",
            "status": "TODO",
            "assigned_to": "developer",
            "priority": 2,
            "dependencies": ["Task 1"],
            "task_type": "decompose",
            "rfc_state": null
        }
    ]
    """

    project_definition = ProjectDefinition(
        name="Test Project", description="A test project"
    )
    tasks = decompose_project(project_definition)

    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[0].task_type == TaskType.RFC
    assert tasks[0].rfc_state == RFCState.DRAFT
    assert tasks[1].title == "Task 2"
    assert tasks[1].task_type == TaskType.DECOMPOSE
    assert tasks[1].rfc_state is None


def test_process_rfc(mock_llm_manager):
    # Mock the LLM response
    mock_llm_manager.run_llm_command.return_value = """
    {
        "title": "Updated RFC",
        "description": "Updated description",
        "status": "IN_PROGRESS",
        "assigned_to": "reviewer",
        "priority": 2,
        "dependencies": [],
        "task_type": "rfc",
        "rfc_state": "REVIEW"
    }
    """

    project_definition = ProjectDefinition(
        name="Test Project", description="A test project"
    )
    task = Task(
        id=1,
        project_id="test_project",
        title="Original RFC",
        description="Original description",
        status="TODO",
        assigned_to="author",
        priority=1,
        dependencies=[],
        task_type=TaskType.RFC,
        rfc_state=RFCState.DRAFT,
    )

    updated_task = process_rfc(task, project_definition)

    assert updated_task.title == "Updated RFC"
    assert updated_task.status == "IN_PROGRESS"
    assert updated_task.assigned_to == "reviewer"
    assert updated_task.priority == 2
    assert updated_task.rfc_state == RFCState.REVIEW
