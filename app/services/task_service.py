from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.db.database import get_db
from app.exceptions.task import TaskNotFound, TaskForbidden

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_tasks(self) -> list[Task]:
        return self.repository.get_tasks()

    def get_task(self, task_id: int, user_id: int) -> Task:
        task = self.repository.get_task(task_id)
        if task is None:
            raise TaskNotFound()

        if task.user_id != user_id:
            raise TaskForbidden()
        return task
    
    def create_task(self, data: TaskCreate) -> Task:
        task_data = data.model_dump(exclude_unset=True)
        return self.repository.create_task(task_data)
    
    def update_task(
        self,
        task_id: int,
        data: TaskUpdate,
        user_id: int | None = None
    ) -> Task:
        task = self.repository.get_task(task_id)
        if task is None:
            raise TaskNotFound()

        if user_id is not None and task.user_id != user_id:
            raise TaskForbidden()

        update_data = data.model_dump(exclude_unset=True)
        updated_task = self.repository.update_task(task_id, update_data)
        return updated_task

    def delete_task(
        self,
        task_id: int,
        user_id: int | None = None
    ) -> None:
        task = self.repository.get_task(task_id)
        if task is None:
            raise TaskNotFound()

        if user_id is not None and task.user_id != user_id:
            raise TaskForbidden()

        self.repository.delete_task(task_id)


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    repository = TaskRepository(db)
    return TaskService(repository)