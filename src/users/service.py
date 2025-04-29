from sqlalchemy.orm import Session
from src.users.models import User

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()
