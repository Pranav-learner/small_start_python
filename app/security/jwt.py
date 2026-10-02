import jwt
from datetime import datetime,timedelta,timezone

from app.exceptions import InvalidToken

SECRET_KEY = "small-start-python"
ALGORITHM = "HS256"
ACESS_TOEKN_EXPIRE_MINUTES = 30

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