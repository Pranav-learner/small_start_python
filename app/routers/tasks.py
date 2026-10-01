from app.services.task_service import get_task_service
from fastapi import Depends
from fastapi import APIRouter
from app.services.task_service import TaskService
from pydantic import BaseModel
router = APIRouter()

class TaskCreate(BaseModel):
   title:str
   status:str

class TaskUpdate(BaseModel):
   title:str
   status:str
   
@router.get("/api/v1/tasks")
def get_tasks():
    return {"message": "Get all tasks"}


@router.get("/api/v1/tasks/{task_id}")
def get_task(task_id: int,service:TaskService = Depends(get_task_service)):
    return service.get_task(task_id)

@router.post("/api/v1/tasks")
def create_task(task_data:TaskCreate,service:TaskService = Depends(get_task_service)):
   return service.create_task(task_data.title,task_data.status)

@router.patch("/api/v1/tasks/{task_id}")
def update_task(task_id:int,task_data:TaskUpdate,service:TaskService = Depends(get_task_service)):
   return service.update_task(task_id,task_data.title,task_data.status)

@router.delete("/api/v1/tasks/{task_id}")
def delete_task(task_id:int,service:TaskService = Depends(get_task_service)):
   return service.delete_task(task_id)

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