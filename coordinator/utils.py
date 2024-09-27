import pytest
import os
from datetime import datetime

from coordinator.models import RFCState, Task, TaskType
from coordinator.utils import extract_json_from_response

from coordinator.utils import (
    calculate_project_progress,
    create_project_directory,
    extract_json_from_response,
    format_file_size,
    format_org_mode_task,
    format_time_estimate,
    generate_cache_key,
    generate_project_summary,
    generate_task_id,
    is_valid_url,
    parse_dependencies,
    sanitize_filename,
    truncate_string,
    validate_email,
)


def test_extract_json_from_response():
    assert extract_json_from_response('{"key": "value"}') == {"key": "value"}

    nested_json = """
    {
      "person": {
        "name": "John",
        "age": 30,
        "address": {
          "street": "123 Main St",
          "city": "Anytown"
        }
      }
    }
    """
    expected_nested = {
        "person": {
            "name": "John",
            "age": 30,
            "address": {"street": "123 Main St", "city": "Anytown"},
        }
    }
    assert extract_json_from_response(nested_json) == expected_nested

    json_with_comments = """
    {
      "task": "Deploy application",
      // This is a comment
      "status": "In Progress",
      "assigned_to": "devops-team", /* Another comment */
      "priority": 1
    }
    """
    expected_with_comments = {
        "task": "Deploy application",
        "status": "In Progress",
        "assigned_to": "devops-team",
        "priority": 1,
    }
    assert extract_json_from_response(json_with_comments) == expected_with_comments

    json_with_text = """
    Some text before JSON
    {
      "result": "success",
      "data": {
        "id": 123,
        "name": "Test"
      }
    }
    Some text after JSON
    """
    expected_with_text = {"result": "success", "data": {"id": 123, "name": "Test"}}
    assert extract_json_from_response(json_with_text) == expected_with_text

    assert extract_json_from_response('{"key": "value",}') == {}
    assert (
        extract_json_from_response("This is just a plain text without any JSON.") == {}
    )


def test_create_project_directory(tmp_path):
    project_name = "TestProject"
    description = "A test project"
    tasks = [
        Task(
            id=1,
            project_id=project_name,
            title="Task 1",
            description="Description 1",
            status="TODO",
            assigned_to="Tester",
            priority=1,
            dependencies=[],
            task_type=TaskType.RFC,
            rfc_state=RFCState.DRAFT,
        )
    ]

    create_project_directory(project_name, description, tasks)

    project_path = os.path.join(tmp_path, "projects", project_name)
    assert os.path.exists(project_path)
    assert os.path.exists(os.path.join(project_path, "project_info.json"))
    assert os.path.exists(os.path.join(project_path, "tasks.json"))


def test_generate_cache_key():
    key1 = generate_cache_key("prompt1", "role1")
    key2 = generate_cache_key("prompt1", "role1")
    key3 = generate_cache_key("prompt2", "role1")

    assert key1 == key2
    assert key1 != key3


def test_sanitize_filename():
    assert sanitize_filename("file name.txt") == "file_name.txt"
    assert sanitize_filename("file/name.txt") == "filename.txt"
    assert sanitize_filename("file:name.txt") == "filename.txt"
    assert len(sanitize_filename("a" * 300)) == 255


def test_format_time_estimate():
    assert format_time_estimate(0.5) == "30 minutes"
    assert format_time_estimate(2) == "2.0 hours"
    assert format_time_estimate(48) == "2.0 days"


def test_parse_dependencies():
    assert parse_dependencies("dep1, dep2, dep3") == ["dep1", "dep2", "dep3"]
    assert parse_dependencies("dep1,dep2,dep3") == ["dep1", "dep2", "dep3"]
    assert parse_dependencies("  dep1  ,  dep2  ") == ["dep1", "dep2"]


def test_generate_task_id():
    id1 = generate_task_id("project1", "task1")
    id2 = generate_task_id("project1", "task1")
    id3 = generate_task_id("project1", "task2")

    assert id1 == id2
    assert id1 != id3
    assert len(id1) == 8


def test_calculate_project_progress():
    tasks = [
        Task(
            id=1,
            project_id="test",
            title="Task 1",
            description="",
            status="COMPLETED",
            assigned_to="",
            priority=1,
            dependencies=[],
        ),
        Task(
            id=2,
            project_id="test",
            title="Task 2",
            description="",
            status="IN_PROGRESS",
            assigned_to="",
            priority=1,
            dependencies=[],
        ),
        Task(
            id=3,
            project_id="test",
            title="Task 3",
            description="",
            status="TODO",
            assigned_to="",
            priority=1,
            dependencies=[],
        ),
    ]
    assert calculate_project_progress(tasks) == 100 / 3


def test_format_org_mode_task():
    task = Task(
        id=1,
        project_id="test",
        title="Test Task",
        description="A test task",
        status="TODO",
        assigned_to="Tester",
        priority=1,
        dependencies=["Dep1"],
        task_type=TaskType.RFC,
        rfc_state=RFCState.DRAFT,
    )
    formatted = format_org_mode_task(task)
    assert "* TODO Test Task" in formatted
    assert ":ID: 1" in formatted
    assert ":PRIORITY: 1" in formatted
    assert ":ASSIGNED: Tester" in formatted
    assert "A test task" in formatted
    assert "Dependencies: Dep1" in formatted


def test_generate_project_summary():
    tasks = [
        Task(
            id=1,
            project_id="test",
            title="Task 1",
            description="",
            status="COMPLETED",
            assigned_to="",
            priority=1,
            dependencies=[],
        ),
        Task(
            id=2,
            project_id="test",
            title="Task 2",
            description="",
            status="TODO",
            assigned_to="",
            priority=1,
            dependencies=[],
        ),
    ]
    summary = generate_project_summary("Test Project", "A test project", tasks)
    assert "* Project: Test Project" in summary
    assert ":PROGRESS: 50.0%" in summary
    assert "A test project" in summary
    assert "* DONE Task 1" in summary
    assert "* TODO Task 2" in summary


def test_validate_email():
    assert validate_email("test@example.com")
    assert validate_email("test.name@example.co.uk")
    assert not validate_email("invalid-email")
    assert not validate_email("test@example")


def test_is_valid_url():
    assert is_valid_url("http://www.example.com")
    assert is_valid_url("https://example.com/path?query=value")
    assert not is_valid_url("not a url")
    assert not is_valid_url("http://")


def test_truncate_string():
    assert truncate_string("This is a long string", 10) == "This is..."
    assert truncate_string("Short", 10) == "Short"


def test_format_file_size():
    assert format_file_size(500) == "500.0 B"
    assert format_file_size(1024) == "1.0 KB"
    assert format_file_size(1024 * 1024) == "1.0 MB"
    assert format_file_size(1024 * 1024 * 1024) == "1.0 GB"
