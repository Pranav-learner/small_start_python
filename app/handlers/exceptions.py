from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.task import TaskNotFound, TaskForbidden
from app.exceptions.user import (
    UserAlreadyExists,
    InvalidCredentials,
    InvalidToken,
    Forbidden,
    UserNotFound
)


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


def user_already_exists_handler(
    request: Request,
    exc: UserAlreadyExists
):
    return JSONResponse(
        status_code=409,
        content={
            "error": "USER_ALREADY_EXISTS",
            "message": "User already exists"
        }
    )


def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentials
):
    return JSONResponse(
        status_code=401,
        content={
            "error": "INVALID_CREDENTIALS",
            "message": "Invalid username or password"
        }
    )


def invalid_token_handler(
    request: Request,
    exc: InvalidToken
):
    return JSONResponse(
        status_code=401,
        content={
            "error": "INVALID_TOKEN",
            "message": "Invalid or expired token"
        }
    )

def forbidden_handler(request: Request, exc: Forbidden):
    return JSONResponse(
        status_code=403,
        content={
            "error": "FORBIDDEN",
            "message": "You do not have permission to perform this action"
        }
    )


def user_not_found_handler(request: Request, exc: UserNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "error": "USER_NOT_FOUND",
            "message": "User not found"
        }
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(TaskNotFound, task_not_found_handler)
    app.add_exception_handler(TaskForbidden, task_forbidden_handler)
    app.add_exception_handler(UserAlreadyExists, user_already_exists_handler)
    app.add_exception_handler(InvalidCredentials, invalid_credentials_handler)
    app.add_exception_handler(InvalidToken, invalid_token_handler)
    app.add_exception_handler(Forbidden, forbidden_handler)
    app.add_exception_handler(UserNotFound, user_not_found_handler)