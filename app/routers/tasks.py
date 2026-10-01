from app.services.task_service import get_task_service
from fastapi import Depends
from fastapi import APIRouter
from app.services.task_service import TaskService
router = APIRouter()


@router.get("/api/v1/tasks")
def get_tasks():
    return {"message": "Get all tasks"}


@router.get("/api/v1/tasks/{id}")
def get_task(id: int,service:TaskService = Depends(get_task_service)):
    return service.get_task(id)

'''
Request
   ↓
Depends(get_task_service)
   ↓
get_task_service(db)
   ↓
Depends(get_db)
   ↓
SessionLocal()
   ↓
TaskRepository(db)
   ↓
TaskService(repository)
   ↓
get_task()
'''