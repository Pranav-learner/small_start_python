class TaskService:

    def get_task(self,task_id:int):
        return {
            "task_id" : task_id,
            "title" : "Learn Python",
            "status" : "TODO"
        }
        