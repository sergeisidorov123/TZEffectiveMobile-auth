from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base

class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    resource: Mapped[str] = mapped_column(String)
    action: Mapped[str] = mapped_column(String)

    roles = relationship(
        "Roles",
        secondary="role_permissions",
        back_populates="permissions"
    )
