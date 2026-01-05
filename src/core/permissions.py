from fastapi import Depends, HTTPException, status
from src.core.crud import get_current_user
from src.models.user import User

def check_permission(resource: str, action: str):
    def checker(user: User = Depends(get_current_user)):
        for role in user.roles:
            for perm in role.permissions:
                if perm.resource == resource and perm.action == action:
                    return
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden"
        )
    return checker
