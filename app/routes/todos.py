from fastapi import APIRouter, HTTPException
from app.services.todo_service import create_todo, get_todo, get_todos, update_todo, delete_todo
from app.schemas.schemas import TodoCreate, TodoUpdate, TodoResponse

router = APIRouter()

@router.post("/", response_model=TodoResponse)
async def create_todo_endpoint(todo: TodoCreate):
    return await create_todo(todo)

@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo_endpoint(todo_id: str):
    todo = await get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.get("/", response_model=list[TodoResponse])
async def get_todos_endpoint():
    return await get_todos()

@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo_endpoint(todo_id: str, todo: TodoUpdate):
    updated_todo = await update_todo(todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}")
async def delete_todo_endpoint(todo_id: str):
    result = await delete_todo(todo_id)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    return result
