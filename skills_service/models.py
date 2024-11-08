# skills_service/service/models.py

from pydantic import BaseModel
from typing import List

class SkillItem(BaseModel):
    category: str          # Example: "Programming Languages"
    skills: List[str]      # Example: ["Python", "JavaScript", "C++"]
