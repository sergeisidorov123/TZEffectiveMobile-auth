from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI
from src.models.user import User
from src.models.roles import Roles
from src.db.db_settings import engine

app = FastAPI()

