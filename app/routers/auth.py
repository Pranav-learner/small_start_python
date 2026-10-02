from fastapi import APIRouter, Depends, status

from app.schemas.auth import RegisterRequest, LoginRequest, UserResponse
from app.services.auth_service import AuthService, get_auth_service

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
    data: RegisterRequest,
    service: AuthService = Depends(get_auth_service)
):
    return service.register(data)


@router.post("/login", response_model=UserResponse, status_code=status.HTTP_200_OK)
def login(
    data: LoginRequest,
    service: AuthService = Depends(get_auth_service)
):
    return service.authenticate(data)
