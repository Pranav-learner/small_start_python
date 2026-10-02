from fastapi import APIRouter, Depends, status

from app.schemas.auth import RegisterRequest, LoginRequest, UserResponse
from app.services.auth_service import AuthService, get_auth_service
from app.services.user_service import UserService, get_user_service
from app.security.authorization import require_admin

router = APIRouter(tags=["auth"])


@router.post("/api/v1/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
    data: RegisterRequest,
    service: AuthService = Depends(get_auth_service)
):
    return service.register(data)


@router.post("/api/v1/auth/login", response_model=UserResponse, status_code=status.HTTP_200_OK)
def login(
    data: LoginRequest,
    service: AuthService = Depends(get_auth_service)
):
    return service.authenticate(data)


@router.delete("/api/v1/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    current_user = Depends(require_admin),
    user_service: UserService = Depends(get_user_service)
):
    user_service.delete_user(user_id)
    return None