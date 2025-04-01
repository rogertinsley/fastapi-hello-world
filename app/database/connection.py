from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from pymongo import ASCENDING
import os

MONGO_DETAILS = os.getenv("MONGO_URL")
print(f"MONGO_URL: {MONGO_DETAILS}")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.todo
todos_collection = database.get_collection("todos")

def get_db():
    return todos_collection