from fastapi import Depends
from app.security.dependecies import get_current_user
from app.exceptions import Forbidden


def require_admin(
    current_user = Depends(get_current_user)
):
    if current_user.role != "ADMIN":
        raise Forbidden()

    return current_user