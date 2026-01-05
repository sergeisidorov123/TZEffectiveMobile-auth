from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from src.core.permissions import check_permission
from src.db.db_settings import SessionLocal
from src.models.roles import Roles
from src.models.permission import Permission
from src.models.user import User

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(check_permission("admin", "access"))],
)


@router.post("/roles")
def create_role(name: str):
    """Создание ролей"""
    with SessionLocal() as session:
        role = Roles(name=name)
        session.add(role)
        session.commit()
        return {"status": "role created"}


@router.post("/permissions")
def create_permission(resource: str, action: str):
    """Создание рарзешенией пользователям"""
    with SessionLocal() as session:
        perm = Permission(resource=resource, action=action)
        session.add(perm)
        session.commit()
        return {"status": "permission created"}


@router.post("/roles/{role_id}/permissions/{permission_id}")
def attach_permission(role_id: int, permission_id: int):
    """Выдача разрешений"""
    with SessionLocal() as session:
        role = session.get(Roles, role_id)
        perm = session.get(Permission, permission_id)

        if not role or not perm:
            raise HTTPException(status_code=404)

        role.permissions.append(perm)
        session.commit()
        return {"status": "permission attached"}


@router.post("/users/{user_id}/roles/{role_id}")
def assign_role(user_id: int, role_id: int):
    """Выдача ролей"""
    with SessionLocal() as session:
        user = session.get(User, user_id)
        role = session.get(Roles, role_id)

        if not user or not role:
            raise HTTPException(status_code=404)

        user.roles.append(role)
        session.commit()
        return {"status": "role assigned"}
