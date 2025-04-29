from sqlalchemy import Column, BigInteger, String, DateTime, func
from sqlalchemy.orm import relationship

from src.core.models import Base

class User(Base):
    __tablename__ = "users"

    user_id     = Column(BigInteger, primary_key=True, autoincrement=True)
    email       = Column(String(128), unique=True, nullable=False)
    password    = Column(String(256), nullable=False)
    role        = Column(String(32),  default="student")
    created_at  = Column(DateTime,    server_default=func.now())

    # -------- 反向关系（可选）--------
    ai_assessments  = relationship("AIAssessment", back_populates="user")
    learning_style  = relationship("LearningStyle", back_populates="user", uselist=False)
    goals           = relationship("Goal", back_populates="user")
