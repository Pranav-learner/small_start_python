from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.database import get_db
from app.exceptions import UserAlreadyExists, InvalidCredentials
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest, LoginRequest
from app.security.password import (
    hash_password,
    verify_password
)



class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, data: RegisterRequest):

        existing_user = (
            self.user_repository
            .get_by_username(data.username)
        )

        if existing_user:
            raise UserAlreadyExists()

        password_hash = hash_password(data.password)

        return self.user_repository.create(
            username=data.username,
            password_hash=password_hash
        )

    def authenticate(self, data: LoginRequest):
        user = self.user_repository.get_by_username(
            data.username
        )

        if user is None:
            raise InvalidCredentials()

        if not verify_password(
            data.password,
            user.password_hash
        ):
            raise InvalidCredentials()

        return user
    
    



def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    repository = UserRepository(db)
    return AuthService(repository)