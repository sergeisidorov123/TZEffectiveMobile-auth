from sqlalchemy.ext.declarative import declarative_base

from src.models.user import User
from src.models.roles import Roles
from src.db.db_settings import engine

Base = declarative_base()

Base.metadata.create_all(engine)