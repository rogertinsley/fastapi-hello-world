from fastapi import FastAPI
from app.routes.reminders import router as reminders_router
from app.routes.todos import router as todos_router

app = FastAPI()

app.include_router(reminders_router, prefix="/reminders")
app.include_router(todos_router, prefix="/todos")
