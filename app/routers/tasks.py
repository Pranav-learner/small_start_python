from fastapi import APIRouter
from app.services.task_service import TaskService
router = APIRouter()

task_service = TaskService()

@router.get("/api/v1/tasks")
def get_tasks():
    return {"message": "Get all tasks"}


@router.get("/api/v1/tasks/{task_id}")
def get_task(task_id: int):
    return task_service.get_task(task_id)