from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Task

class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_tasks(self) -> list[Task]:
        return list(self.db.scalars(select(Task)).all())

    def get_task(self, task_id: int) -> Task | None:
        return self.db.get(Task, task_id)

    def create_task(self, data: dict) -> Task:
        task = Task(**data)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(
        self,
        task_id: int,
        data: dict
    ) -> Task | None:
        task = self.db.get(Task, task_id)
        if task is None:
            return None
        
        for field, value in data.items():
            setattr(task, field, value)

        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        task = self.db.get(Task, task_id)
        
        if task is None:
            return False

        self.db.delete(task)
        self.db.commit()
        return True
#For Create
'''
Session created
      ↓
Task object created
      ↓
add()
      ↓
pending change
      ↓
commit()
      ↓
flush SQL
      ↓
COMMIT
      ↓
refresh()
      ↓
updated Python object
'''
#For Update
'''
Session
 ↓
get()
 ↓
tracked ORM object
 ↓
modify object
 ↓
commit()
 ↓
SQL UPDATE
 ↓
COMMIT
'''
#For delete
'''
Session
 ↓
get()
 ↓
tracked ORM object
 ↓
delete()
 ↓
commit()
 ↓
SQL DELETE
 ↓
COMMIT
'''

# The basic Transaction
'''
self.db.add(task)

# something goes wrong

self.db.commit()

The transaction may be rolled back.

The basic transaction pattern is:

try:
    self.db.add(task)
    self.db.commit()
    self.db.refresh(task)
except:
    self.db.rollback()
    raise
'''