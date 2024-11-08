# projects_service/service/models.py

from pydantic import BaseModel
from typing import List

class ProjectItem(BaseModel):
    title: str
    description: str
    technologies: List[str]
    link: str
    duration: str
