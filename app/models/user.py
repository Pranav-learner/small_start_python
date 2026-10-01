from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.task import Task

class User(Base):
    __tablename__ = "users"

    user_id : Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(50),unique = True,nullable = False)
    
    tasks:Mapped[list["Task"]] = relationship(
        back_populates = "owner"
    )
