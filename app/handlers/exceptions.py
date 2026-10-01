from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.task import TaskNotFound, TaskForbidden


def task_not_found_handler(
    request: Request,
    exc: TaskNotFound
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "TASK_NOT_FOUND",
            "message": "Task not found"
        }
    )


def task_forbidden_handler(
    request: Request,
    exc: TaskForbidden
):
    return JSONResponse(
        status_code=403,
        content={
            "error": "TASK_FORBIDDEN",
            "message": "You cannot access this task"
        }
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(TaskNotFound, task_not_found_handler)
    app.add_exception_handler(TaskForbidden, task_forbidden_handler)