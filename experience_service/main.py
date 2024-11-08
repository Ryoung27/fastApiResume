from fastapi import FastAPI
from service.experience_service import get_experience_data

app = FastAPI()

@app.get("/experience")
async def read_experience():
    return get_experience_data()
