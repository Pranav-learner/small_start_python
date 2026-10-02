from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.exceptions import InvalidToken
from app.models import User
from app.repositories.user_repository import UserRepository
from app.security.jwt import decode_acess_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)
# OAuth2PasswordBearer responsibility

# It primarily handles extracting the bearer token and also informs FastAPI's OpenAPI/docs about the bearer authentication scheme.

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    user_id = decode_acess_token(token)
    user_repository = UserRepository(db)
    user = user_repository.get_by_id(user_id)
    if user is None:
        raise InvalidToken()
    return user