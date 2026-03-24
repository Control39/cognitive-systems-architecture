from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

class Vacancy(BaseModel):
    id: str
    name: str
    employer: str
    salary: Optional[Dict] = None
    url: str
    description: str

class UserProfile(BaseModel):
    name: str
    skills: List[str]
    experience_years: int = 0

class Application(BaseModel):
    vacancy: Vacancy
    resume: str
    status: str = \"pending\"
    sent_at: datetime = datetime.now()

class AgentResult(BaseModel):
    success: bool
    output: str
    vacancies: Optional[List[Vacancy]] = None
    resume: Optional[str] = None
