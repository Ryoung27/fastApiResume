# skills_service/service/database.py

import os
from pymongo import MongoClient

# Connect to MongoDB using the environment variable
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")  # Default to localhost if MONGO_URI is not set
client = MongoClient(MONGO_URI)

# Define the database
db = client["resume_db"]

# Define the skills collection
skills_collection = db["skills"]
