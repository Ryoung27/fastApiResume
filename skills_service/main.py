# skills_service/main.py

from fastapi import FastAPI
from service.skills_service import get_skills_data

app = FastAPI()

@app.get("/skills")
async def get_skills():
    return get_skills_data()
