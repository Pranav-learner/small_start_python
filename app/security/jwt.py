import jwt
from datetime import datetime,timedelta,timezone

from app.config import (
    JWT_SECRET_KEY as SECRET_KEY,
    JWT_ALGORITHM as ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES as ACESS_TOEKN_EXPIRE_MINUTES,
)
from app.exceptions import InvalidToken

ACCESS_TOKEN_EXPIRE_MINUTES = ACESS_TOEKN_EXPIRE_MINUTES

def create_acess_toekn(user_id:int)-> str:
    expires_at= (
        datetime.now(timezone.utc) + timedelta(minutes=ACESS_TOEKN_EXPIRE_MINUTES)
    )
    payload ={
        "sub":str(user_id),
        "exp":expires_at
    }

    return jwt.encode(payload,SECRET_KEY,algorithm = ALGORITHM)

def decode_acess_token(token:str)->int:
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except jwt.PyJWTError:
        raise InvalidToken()

    user_id = payload.get("sub")

    if user_id is None:
        raise InvalidToken()

    return int(user_id)