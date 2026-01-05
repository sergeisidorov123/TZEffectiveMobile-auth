from fastapi import APIRouter, Depends, HTTPException
from src.dtos.user import UserResponse, UpdateUserRequest
from src.core.crud import get_current_user
from src.db.db_settings import SessionLocal
from src.models.user import User

router = APIRouter(tags=["Users"])


@router.get("/user", response_model=UserResponse)
def me(user: User = Depends(get_current_user)):
    """Посмотреть юзера"""
    return user


@router.put("/user")
def update_me(data: UpdateUserRequest, user: User = Depends(get_current_user),):
    """Смена имени"""
    with SessionLocal() as session:
        db_user = session.get(User, user.id)
        db_user.full_name = data.full_name
        session.commit()
        session.close()
        return {"status": "updated"}


@router.delete("/user")
def delete_me(user: User = Depends(get_current_user)):
    """Мягкое удаление(меняется флаг)"""
    with SessionLocal() as session:
        db_user = session.get(User, user.id)
        db_user.is_active = False
        session.commit()
        session.close()
        return {"status": "account deactivated"}
