import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
db = client["resume_db"]
experience_collection = db["experience"]

def get_experience_data():
    experience = experience_collection.find()
    return [{"company": exp["company"], "position": exp["position"],
             "location": exp["location"], "duration": exp["duration"],
             "responsibilities": exp["responsibilities"]}
            for exp in experience]
