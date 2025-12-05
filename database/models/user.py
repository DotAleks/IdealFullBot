from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column

from database.models.base import Base


class User(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    phone_number: Mapped[str] = mapped_column(String(12))
    email: Mapped[str] = mapped_column(String(70))