"""
AI 相关两张表：
- AIAssessment : 每一次综合评估
- LearningStyle: 学习风格画像
"""
from datetime import date

from sqlalchemy import (
    Column, BigInteger, Integer, Date, JSON, ForeignKey
)
from sqlalchemy.orm import relationship

from src.core.models import Base

# -------------------------------------------------- #
# 1. 综合评估
# -------------------------------------------------- #
class AIAssessment(Base):
    __tablename__ = "ai_assessments"

    assessment_id  = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id        = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)

    assess_date    = Column(Date, default=date.today)
    overall_score  = Column(Integer)
    subscores_json = Column(JSON)

    user = relationship("User", back_populates="ai_assessments")


# -------------------------------------------------- #
# 2. 学习风格
# -------------------------------------------------- #
class LearningStyle(Base):
    __tablename__ = "learning_styles"

    style_id   = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id    = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)

    memorising  = Column(Integer)
    researching = Column(Integer)
    practising  = Column(Integer)
    reading     = Column(Integer)

    user = relationship("User", back_populates="learning_style", uselist=False)


__all__ = ["AIAssessment", "LearningStyle"]
