"""
Pydantic models for Career Development System.
These models are used by CompetencyTracker and API.
"""
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime
import uuid


class CompetencyMarker(BaseModel):
    """A competency marker representing a specific achievement."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: Optional[str] = None
    status: str = Field(default="pending", regex="^(pending|in_progress|completed)$")
    required_level: int = Field(default=1, ge=1, le=5)
    evidence_url: Optional[HttpUrl] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Skill(BaseModel):
    """A skill with a level and associated competency markers."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    level: int = Field(default=1, ge=1, le=5)
    markers: List[CompetencyMarker] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserProfile(BaseModel):
    """User profile with skills and personal info."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    skills: List[Skill] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Export
__all__ = ["CompetencyMarker", "Skill", "UserProfile"]