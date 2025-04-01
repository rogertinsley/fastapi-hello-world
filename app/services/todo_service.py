from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas.schemas import TodoCreate, TodoUpdate
from bson import ObjectId
from app.database.connection import todos_collection

# Helper function to convert ObjectId to string
def todo_helper(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo.get("description", "")
    }

async def create_todo(todo: TodoCreate):
    todo_data = todo.dict()
    result = await todos_collection.insert_one(todo_data)
    created_todo = await todos_collection.find_one({"_id": result.inserted_id})
    return todo_helper(created_todo)

async def get_todo(todo_id: str):
    todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
    if todo:
        return todo_helper(todo)
    return None

async def get_todos():
    todos = []
    async for todo in todos_collection.find():
        todos.append(todo_helper(todo))
    return todos

async def update_todo(todo_id: str, todo_update: TodoUpdate):
    update_data = {k: v for k, v in todo_update.dict(exclude_unset=True).items()}
    result = await todos_collection.update_one(
        {"_id": ObjectId(todo_id)}, {"$set": update_data}
    )
    if result.modified_count == 1:
        updated_todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_helper(updated_todo)
    return None

async def delete_todo(todo_id: str):
    result = await todos_collection.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 1:
        return {"detail": "Todo deleted successfully"}
    return None