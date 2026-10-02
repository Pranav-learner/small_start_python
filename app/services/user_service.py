from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.database import get_db
from app.exceptions import UserNotFound
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def delete_user(self, user_id: int) -> None:
        user = self.user_repository.get_by_id(user_id)
        if user is None:
            raise UserNotFound()

        self.user_repository.delete(user)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)
