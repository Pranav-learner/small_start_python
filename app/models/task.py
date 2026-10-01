from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String 
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user import User

class Task(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(20))

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id"),nullable=True
    )

    owner: Mapped["User"] = relationship(
        back_populates="tasks"
    )
 