from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from fastapi.security import OAuth2PasswordRequestForm
from src.core.crud import oauth2_scheme, get_current_user
from src.dtos.auth import RegisterRequest, LoginRequest, TokenResponse
from src.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from src.db.db_settings import SessionLocal
from src.models.user import User
from src.models.blacklist import BlackList

router = APIRouter(tags=["Auth"])


@router.post("/register")
def register(data: RegisterRequest):
    """Регистрация"""
    if data.password != data.password_repeat:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    with SessionLocal() as session:
        existing_user = session.scalar(select(User).where(User.email == data.email))
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        new_user = User(
            email=data.email,
            full_name=data.full_name,
            password_hash=hash_password(data.password),
            is_active=True
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {"id": new_user.id, "email": new_user.email}


@router.post("/login", response_model=TokenResponse)
def login(data: OAuth2PasswordRequestForm = Depends()):  # Замени LoginRequest на форму
    """Логин"""
    with SessionLocal() as session:
        # В OAuth2PasswordRequestForm поле называется .username
        # Мы используем его как email
        user = session.scalar(select(User).where(User.email == data.username))

        if not user or not user.is_active:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not verify_password(data.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token(user.id)

        # Swagger ОБЯЗАТЕЛЬНО ждет поле token_type: bearer
        return {"access_token": token, "token_type": "bearer"}


@router.post("/logout")
def logout(user: User = Depends(get_current_user), token: str = Depends(oauth2_scheme)):
    """Логаут"""
    with SessionLocal() as session:
        revoked_token = BlackList(token=token)
        session.add(revoked_token)
        session.commit()

    return {"status": "logged out"}
