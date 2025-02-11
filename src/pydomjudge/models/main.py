from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from pydomjudge.models.shared import StatementFile, ImageFile, ArchiveFile


class User(BaseModel):
    id: str
    username: str
    name: str
    email: Optional[str] = None
    team_id: Optional[str] = None
    roles: List[str]
    enabled: bool
    last_login_time: Optional[datetime] = None

class ContestState(BaseModel):
    started: Optional[datetime] = None
    ended: Optional[datetime] = None
    frozen: Optional[datetime] = None
    thawed: Optional[datetime] = None
    finalized: Optional[datetime] = None
    end_of_updates: Optional[datetime] = None

class ContestProblem(BaseModel):
    id: str
    label: str
    name: str
    time_limit: float
    statement: List[StatementFile] = Field(default_factory=list)

class Contest(BaseModel):
    id: str
    name: str
    shortname: str
    start_time: datetime
    end_time: datetime
    banner: List[ImageFile] = Field(default_factory=list)  # From "Banner" schema

class Team(BaseModel):
    id: str
    name: str
    display_name: Optional[str] = None
    group_ids: List[str] = Field(default_factory=list)
    photo: List[ImageFile] = Field(default_factory=list)  # From "Photo" schema

class Submission(BaseModel):
    id: str
    language_id: str
    problem_id: str
    team_id: str
    time: datetime
    files: List[ArchiveFile] = Field(default_factory=list)  # From "Files" schema

class JudgementType(BaseModel):
    id: str
    name: str
    penalty: bool
    solved: bool

class Judgement(BaseModel):
    id: str
    submission_id: str
    judgement_type_id: Optional[str] = None
    valid: bool
    max_run_time: Optional[float] = None

class Clarification(BaseModel):
    id: str
    text: str
    problem_id: Optional[str] = None
    from_team_id: Optional[str] = None
    to_team_id: Optional[str] = None
    time: Optional[datetime] = None
