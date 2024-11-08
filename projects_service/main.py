# projects_service/main.py

from fastapi import FastAPI
from service.projects_service import get_projects_data

app = FastAPI()

@app.get("/projects")
async def get_projects():
    return get_projects_data()
