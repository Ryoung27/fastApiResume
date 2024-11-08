import os
from pymongo import MongoClient

# Connect to MongoDB using the environment variable
client = MongoClient(os.getenv("Mongo_URI"))
db = client["resume_db"]
personal_info_collection = db["personal_info"]