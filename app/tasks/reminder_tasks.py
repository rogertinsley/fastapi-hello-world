from celery import Celery

celery_app = Celery(
    "worker",
    backend="redis://redis:6379/0",
    broker="redis://redis:6379/0"
)

@celery_app.task
def send_reminder_email(email, task_title):
    print(f"📧 Sending reminder email to {email} about {task_title}")
    return f"Reminder sent to {email}"