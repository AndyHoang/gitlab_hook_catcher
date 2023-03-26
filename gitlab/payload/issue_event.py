from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    username: str
    avatar_url: str
    email: Optional[str]

class Assignee(BaseModel):
    name: str
    username: str
    avatar_url: Optional[str]


class Project(BaseModel):
    id: int
    name: str
    description: str
    web_url: str
    avatar_url: Optional[str]
    git_ssh_url: str
    git_http_url: str
    namespace: str
    visibility_level: int
    path_with_namespace: str
    default_branch: str
    ci_config_path: Optional[str]
    homepage: str
    url: str
    ssh_url: str
    http_url: str


class Label(BaseModel):
    id: int
    title: str
    color: str
    project_id: int
    created_at: str
    updated_at: str
    template: bool
    description: str
    type: str
    group_id: int


class EscalationPolicy(BaseModel):
    id: int
    name: str


class ObjectAttributes(BaseModel):
    id: int
    title: str
    assignee_ids: List[int]
    assignee_id: int
    author_id: int
    project_id: int
    created_at: str
    updated_at: str
    updated_by_id: int
    last_edited_at: Optional[str]
    last_edited_by_id: Optional[int]
    relative_position: int
    description: str
    milestone_id: Optional[int]
    state_id: int
    confidential: bool
    discussion_locked: bool
    due_date: Optional[str]
    moved_to_id: Optional[int]
    duplicated_to_id: Optional[int]
    time_estimate: int
    total_time_spent: int
    time_change: int
    human_total_time_spent: Optional[str]
    human_time_estimate: Optional[str]
    human_time_change: Optional[str]
    weight: Optional[int]
    iid: int
    url: str
    state: str
    action: str
    severity: Optional[str]
    escalation_status: Optional[str]
    escalation_policy: Optional[EscalationPolicy]
    labels: Optional[List[Label]]


class Repository(BaseModel):
    name: str
    url: str
    description: str
    homepage: str


class IssueEventPayload(BaseModel):
    object_kind: str
    event_type: str
    user: User
    project: Project
    object_attributes: ObjectAttributes
    repository: Repository
    assignees: Optional[List[Assignee]]
    assignee: Optional[Assignee]
    labels: Optional[List[Label]]
    changes: Optional[dict]
