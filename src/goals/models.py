# src/goals/models.py
from sqlalchemy import Column, BigInteger, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.core.models import Base

class Goal(Base):
    __tablename__ = "goals"

    goal_id      = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id      = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    goal_category = Column(String(8))
    goal_subtype  = Column(String(32))
    target_name   = Column(String(128))
    target_date   = Column(Date)
    progress_pct  = Column(BigInteger)
    status        = Column(String(16))

    # 和 GoalTask 建立反向关系
    tasks = relationship("GoalTask", back_populates="goal")


class GoalTask(Base):
    __tablename__ = "goal_tasks"

    task_id    = Column(BigInteger, primary_key=True, autoincrement=True)
    goal_id    = Column(BigInteger, ForeignKey("goals.goal_id"), nullable=False)
    title      = Column(String(128))
    due_date   = Column(Date)
    weight_pct = Column(BigInteger)
    state      = Column(String(16))

    # 和 Goal 建立正向关系
    goal = relationship("Goal", back_populates="tasks")
