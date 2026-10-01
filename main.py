from fastapi import FastAPI
from app.routers.tasks import router as task_router
from app.db.base import Base
from app.models.task import Task
from app.models.user import User

from app.db.database import engine
from app.exceptions.task import TaskNotFound, TaskForbidden
from app.handlers.exceptions import (
    task_not_found_handler,
    task_forbidden_handler,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_exception_handler(
    TaskNotFound,
    task_not_found_handler
)

app.add_exception_handler(
    TaskForbidden,
    task_forbidden_handler
)

app.include_router(task_router)
# include_router() is essentially telling FastAPI:These routes belong to this application; register them.

'''
Important

create_all() is useful for learning, but we will not use it as our production migration strategy. Later we'll introduce Alembic for proper schema migrations.

Task Python class
       ↓
SQLAlchemy ORM mapping
       ↓
Base.metadata
       ↓
SQLAlchemy Engine
       ↓
psycopg driver
       ↓
PostgreSQL
       ↓
tasks table
'''






"""from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

app = FastAPI()


all_tasks = [
    {
        "task_task_id" : 1,
        "title": "Learn Python",
        "status": "TODO"
    },
    {
        "task_task_id" : 2,
        "title": "Learn Spring Boot",
        "status": "TODO"
    },
    {
        "task_task_id" : 3,
        "title": "Learn FastAPI",
        "status": "TODO"
    }
]

class TaskCreate(BaseModel):
    title:str
    status:str

class TaskResponse(BaseModel):
    task_task_id: int
    title: str
    status: str

class TaskUpdate(BaseModel):
    title: str | None = None
    status: str | None = None

@app.get("/api/v1/tasks",response_model=list[TaskResponse],status_code=status.HTTP_200_OK)
def get_tasks(status: str | None = None):
    if status:
        return [
            task for task in all_tasks
            if task["status"] == status
        ]
    return all_tasks


@app.get("/api/v1/tasks/{task_task_id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def get_task(task_task_id:int):
    for task in all_tasks:
        if task["task_task_id"] == task_task_id:
            return task
    
    raise HTTPException(
        status_code=404,
        detail = "Task not found"
    )

Path parameter:
 /tasks/{task_task_id}
          ↑
      task_identifies resource

Query parameter:
 /tasks?status=TODO
        ↑
    modifies/filter the request

@app.post("/api/v1/tasks",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = {
        "task_task_id" : len(all_tasks) + 1,
        "title": task.title,
        "status": task.status
    }
    all_tasks.append(new_task)
    return new_task

@app.patch("/api/v1/tasks/{task_task_id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def update_task(task_task_id:int,task_update:TaskUpdate):
    for task in all_tasks:
        if task["task_task_id"] == task_task_id:
            if task_update.title is not None:
                task["title"] = task_update.title

            if task_update.status is not None:
                task["status"] = task_update.status

        return task

    raise HTTPException(
        status_code = 404,
        detail = "Task not found"
    ) 

@app.delete("/api/v1/tasks/{task_task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_task_id:int):
    for task in all_tasks:
        if task["task_task_id"] == task_task_id:
            all_tasks.remove(task)
            return
    #OR
    '''
    for index, task in enumerate(all_tasks):
        if task["tasks_task_id"] == task_task_id:
            all_tasks.pop(index)
            return
    '''
    raise HTTPException(
        status_code = 404,
        detail = "Task not found"
    )"""
