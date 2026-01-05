from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI
from src.models.user import User
from src.models.roles import Roles
from src.db.db_settings import engine
from src.api import auth, users, admin, mock
from src.db.base import Base
import src.models

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(admin.router)
app.include_router(mock.router)