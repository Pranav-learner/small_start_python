from fastapi import APIRouter, Depends, status
from app.services.task_service import TaskService, get_task_service
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.security.dependecies import get_current_user

router = APIRouter()

@router.get("/api/v1/tasks", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()


@router.get("/api/v1/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task(
   task_id: int, 
   current_user = Depends(get_current_user),
   service: TaskService = Depends(get_task_service)):
    return service.get_task(task_id,current_user.user_id)


@router.post("/api/v1/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task_data)


@router.patch("/api/v1/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task_data: TaskUpdate, service: TaskService = Depends(get_task_service)):
    return service.update_task(task_id, task_data)


@router.delete("/api/v1/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    service.delete_task(task_id)
    return None

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