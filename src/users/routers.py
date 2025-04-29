from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.users import schemas, service

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_user(db, user_id)
