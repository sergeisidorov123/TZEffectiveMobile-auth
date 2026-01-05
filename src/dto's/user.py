from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool

    class Config:
        from_attributes = True


class UpdateUserRequest(BaseModel):
    full_name: str
