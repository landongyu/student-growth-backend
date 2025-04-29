from pydantic import BaseModel, EmailStr

class UserOut(BaseModel):
    user_id: int
    email: EmailStr

    class Config:
        orm_mode = True
