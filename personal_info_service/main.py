from fastapi import FastAPI, HTTPException
from .models import PersonalInfo
from .database import personal_info_collection

app = FastAPI()

@app.get("/personal_info", response_model=PersonalInfo)
async def get_personal_info():
    #Retrieve the first document in the personal_info collection
    personal_info = personal_info_collection.find_one()
    if personal_info:
        # Convert MongoDB's ObjectId to a string for JSON serialization
        personal_info["_id"] = str(personal_info["_id"])
        return personal_info
    raise HTTPException(status_code=404, detail="Personal info not found")