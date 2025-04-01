from fastapi import APIRouter
from app.tasks.reminder_tasks import send_reminder_email

router = APIRouter()

@router.post("/send/")
async def send_reminder(email: str, task_title: str):
    task = send_reminder_email.delay(email, task_title)
    return {"task_id": task.id, "status": "queued"}