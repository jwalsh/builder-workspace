import pytest
from datetime import datetime
from coordinator.models import (
    TaskType,
    RFCState,
    LLMProvider,
    LLMConfig,
    ProjectDefinition,
    Task,
    ProjectVersion,
    ProjectSummary,
    TaskUpdate,
    ProjectStats,
    UserRole,
    User,
    AuditLog,
)


def test_task_type_enum():
    assert TaskType.RFC.value == "rfc"
    assert TaskType.DECOMPOSE.value == "decompose"
    assert TaskType.RFC_REVIEW.value == "rfc_review"
    assert TaskType.CODE_REVIEW.value == "code_review"
    assert TaskType.AUDIT.value == "audit"
    assert TaskType.UNKNOWN.value == "unknown"


def test_rfc_state_enum():
    assert RFCState.DRAFT.value == "DRAFT"
    assert RFCState.SUBMITTED.value == "SUBMITTED"
    assert RFCState.REVIEW.value == "REVIEW"
    assert RFCState.REVISE.value == "REVISE"
    assert RFCState.APPROVED.value == "APPROVED"
    assert RFCState.REJECTED.value == "REJECTED"
    assert RFCState.DEFERRED.value == "DEFERRED"
    assert RFCState.WITHDRAWN.value == "WITHDRAWN"
    assert RFCState.IMPLEMENTING.value == "IMPLEMENTING"
    assert RFCState.IMPLEMENTED.value == "IMPLEMENTED"
    assert RFCState.OBSOLETE.value == "OBSOLETE"
    assert RFCState.UNKNOWN.value == "UNKNOWN"


def test_llm_provider_enum():
    assert LLMProvider.OLLAMA.value == "ollama"
    assert LLMProvider.CLAUDE.value == "claude"
    assert LLMProvider.RANDOM.value == "random"


def test_llm_config():
    config = LLMConfig(
        provider=LLMProvider.OLLAMA,
        ollama_healthy=True,
        claude_healthy=False,
        last_check=datetime.now(),
    )
    assert config.provider == LLMProvider.OLLAMA
    assert config.ollama_healthy == True
    assert config.claude_healthy == False
    assert isinstance(config.last_check, datetime)


def test_project_definition():
    project = ProjectDefinition(name="Test Project", description="A test project")
    assert project.name == "Test Project"
    assert project.description == "A test project"


def test_task():
    task = Task(
        id=1,
        project_id="test_project",
        title="Test Task",
        description="A test task",
        status="TODO",
        assigned_to="tester",
        priority=1,
        dependencies=["Dep1", "Dep2"],
        task_type=TaskType.RFC,
        rfc_state=RFCState.DRAFT,
    )
    assert task.id == 1
    assert task.project_id == "test_project"
    assert task.title == "Test Task"
    assert task.description == "A test task"
    assert task.status == "TODO"
    assert task.assigned_to == "tester"
    assert task.priority == 1
    assert task.dependencies == ["Dep1", "Dep2"]
    assert task.task_type == TaskType.RFC
    assert task.rfc_state == RFCState.DRAFT


def test_project_version():
    version = ProjectVersion(
        id="test_project",
        definition='{"name": "Test Project", "description": "A test project"}',
        created_at=datetime.now(),
    )
    assert version.id == "test_project"
    assert (
        version.definition
        == '{"name": "Test Project", "description": "A test project"}'
    )
    assert isinstance(version.created_at, datetime)


def test_project_summary():
    summary = ProjectSummary(
        id="test_project",
        name="Test Project",
        description="A test project",
        task_count=5,
        last_updated=datetime.now(),
    )
    assert summary.id == "test_project"
    assert summary.name == "Test Project"
    assert summary.description == "A test project"
    assert summary.task_count == 5
    assert isinstance(summary.last_updated, datetime)


def test_task_update():
    update = TaskUpdate(
        title="Updated Task",
        status="IN_PROGRESS",
        assigned_to="new_tester",
        priority=2,
        task_type=TaskType.CODE_REVIEW,
    )
    assert update.title == "Updated Task"
    assert update.status == "IN_PROGRESS"
    assert update.assigned_to == "new_tester"
    assert update.priority == 2
    assert update.task_type == TaskType.CODE_REVIEW


def test_project_stats():
    stats = ProjectStats(
        total_tasks=10,
        completed_tasks=5,
        in_progress_tasks=3,
        pending_tasks=2,
        rfc_count=2,
        average_priority=2.5,
    )
    assert stats.total_tasks == 10
    assert stats.completed_tasks == 5
    assert stats.in_progress_tasks == 3
    assert stats.pending_tasks == 2
    assert stats.rfc_count == 2
    assert stats.average_priority == 2.5


def test_user_role_enum():
    assert UserRole.ADMIN.value == "admin"
    assert UserRole.MANAGER.value == "manager"
    assert UserRole.DEVELOPER.value == "developer"
    assert UserRole.VIEWER.value == "viewer"


def test_user():
    user = User(
        id=1,
        username="testuser",
        email="test@example.com",
        role=UserRole.DEVELOPER,
        created_at=datetime.now(),
        last_login=datetime.now(),
    )
    assert user.id == 1
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.role == UserRole.DEVELOPER
    assert isinstance(user.created_at, datetime)
    assert isinstance(user.last_login, datetime)


def test_audit_log():
    log = AuditLog(
        id=1,
        user_id=1,
        action="create_task",
        entity_type="Task",
        entity_id="123",
        timestamp=datetime.now(),
        details='{"task_id": 123, "title": "New Task"}',
    )
    assert log.id == 1
    assert log.user_id == 1
    assert log.action == "create_task"
    assert log.entity_type == "Task"
    assert log.entity_id == "123"
    assert isinstance(log.timestamp, datetime)
    assert log.details == '{"task_id": 123, "title": "New Task"}'
