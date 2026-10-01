from anyio import NoEventLoopError
from sqlalchemy.orm import Session

from app.models.task import Task

class TaskRepository:

    def __init__(self,db:Session):
        self.db = db

    def get_task(self, task_id:int):
        return self.db.get(Task,task_id)

    def create_task(self,title:str,status:str = "TODO"):
        task = Task( #It has not necessarily been inserted into PostgreSQL yet.
            title=title,
            status=status
        )

        self.db.add(task) #It queues the object for insertion
        self.db.commit()  #It executes the pending SQL INSERT
        self.db.refresh(task) #It reloads the row from PostgreSQL into the object
        return task


    def update_task(
        self,
        task_id:int,
        title:str,
        status:str
    ):
        task = self.db.get(Task,task_id)
        if task is None:
            return None
        
        task.title = title
        task.status = status

        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self,task_id:int):
        task = self.db.get(Task,task_id)
        
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