from sqlalchemy.orm import declarative_base

Base = declarative_base()

# 下面把各模块的 ORM 类 import 进来，让 Alembic 能扫描到
from src.users.models import User          
from src.goals.models import Goal, GoalTask 
from src.ai.models import (
    AIAssessment, LearningStyle
)