from sqlalchemy.orm import Session

from app.models.task import Task

class TaskRepository:

    def __init__(self,db:Session):
        self.db = db

    def get_task(self, id:int):
        return self.db.get(Task,id)