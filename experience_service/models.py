# experience_service/service/models.py

from pydantic import BaseModel
from typing import List

class ExperienceItem(BaseModel):
    company: str
    position: str
    location: str
    duration: str
    responsibilities: List[str]
