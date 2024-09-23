# File: coordinator/models.py

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ImplementationState(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    TESTING = "testing"
    COMPLETED = "completed"


class TaskType(str, Enum):
    RFC = "rfc"
    DECOMPOSE = "decompose"
    RFC_REVIEW = "rfc_review"
    CODE_REVIEW = "code_review"
    AUDIT = "audit"
    IMPLEMENTATION = "implementation"
    TESTING = "testing"
    DOCUMENTATION = "documentation"
    INFRASTRUCTURE = "infrastructure"
    MONITORING = "monitoring"
    DIAGRAM = "diagram"
    RESEARCH = "research"
    UNKNOWN = "unknown"


class RFCState(str, Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    REVIEW = "REVIEW"
    REVISE = "REVISE"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    DEFERRED = "DEFERRED"
    WITHDRAWN = "WITHDRAWN"
    IMPLEMENTING = "IMPLEMENTING"
    IMPLEMENTED = "IMPLEMENTED"
    OBSOLETE = "OBSOLETE"
    UNKNOWN = "UNKNOWN"


class ImplementationState(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    TESTING = "testing"
    COMPLETED = "completed"


class LLMProvider(str, Enum):
    OLLAMA = "ollama"
    CLAUDE = "claude"
    RANDOM = "random"


class LLMConfig(BaseModel):
    provider: LLMProvider
    ollama_healthy: bool = True
    claude_healthy: bool = True
    last_check: Optional[datetime] = Field(default_factory=datetime.now)

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}

    @classmethod
    def parse_obj(cls, obj):
        if isinstance(obj.get("last_check"), str):
            obj["last_check"] = datetime.fromisoformat(obj["last_check"])
        return super().parse_obj(obj)


class ProjectDefinition(BaseModel):
    name: str
    description: str


class Task(BaseModel):
    id: int
    project_id: str
    title: str
    description: str
    status: str
    assigned_to: str
    priority: int
    dependencies: List[str]
    task_type: TaskType = Field(default=TaskType.UNKNOWN)
    rfc_state: Optional[RFCState] = Field(default=None)
    implementation_state: Optional[ImplementationState] = Field(default=None)


class ProjectVersion(BaseModel):
    id: str
    definition: str
    created_at: datetime


class ProjectSummary(BaseModel):
    id: str
    name: str
    description: str
    task_count: int
    last_updated: datetime


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    priority: Optional[int] = None
    dependencies: Optional[List[str]] = None
    task_type: Optional[TaskType] = None
    rfc_state: Optional[RFCState] = None
    implementation_state: Optional[ImplementationState] = None


class ProjectStats(BaseModel):
    total_tasks: int
    completed_tasks: int
    in_progress_tasks: int
    pending_tasks: int
    rfc_count: int
    average_priority: float


class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    DEVELOPER = "developer"
    VIEWER = "viewer"


class User(BaseModel):
    id: int
    username: str
    email: str
    role: UserRole
    created_at: datetime
    last_login: Optional[datetime] = None


class AuditLog(BaseModel):
    id: int
    user_id: int
    action: str
    entity_type: str
    entity_id: str
    timestamp: datetime
    details: Optional[str] = None
