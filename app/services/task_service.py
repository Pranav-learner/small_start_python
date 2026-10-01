from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.task_repository import TaskRepository
from app.db.database import get_db

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_task(self,task_id:int):
        return self.repository.get_task(task_id)
    
    def create_task(self,title:str,status:str="TODO"):
        return self.repository.create_task(title,status)
    
    def update_task(self,task_id:int,title:str,status:str):
        return self.repository.update_task(task_id,title,status)

    def delete_task(self,task_id:int):
        return self.repository.delete_task(task_id)


def get_task_service(db:Session = Depends(get_db)) -> TaskService:
    repository = TaskRepository(db)
    return TaskService(repository)