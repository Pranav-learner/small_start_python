from sqlalchemy import String 
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(20))

 