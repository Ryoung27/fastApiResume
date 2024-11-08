from pydantic import BaseModel, Field

class PersonalInfo(BaseModel):
    name: str
    email: str
    phone: str
    linkedin: str
    github: str
    summary: str