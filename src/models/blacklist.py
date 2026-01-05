from sqlalchemy import Column, String, DateTime
from datetime import datetime
from src.db.base import Base

class BlackList(Base):
    __tablename__ = "blacklist"

    token: str = Column(String, primary_key=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
