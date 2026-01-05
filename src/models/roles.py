from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base
from .associative import user_roles, role_permissions


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    users = relationship("User", secondary=user_roles, back_populates="roles")
    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")

