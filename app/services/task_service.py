from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.task_repository import TaskRepository
from app.db.database import get_db

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_task(self,id:int):
        return self.repository.get_task(id)


def get_task_service(db:Session = Depends(get_db)) -> TaskService:
    repository = TaskRepository(db)
    return TaskService(repository)