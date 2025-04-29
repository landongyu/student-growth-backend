"""Alembic migration environment."""

from __future__ import annotations

import os
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv

# ------------------------------------------------------------------
# 1️⃣  加载 .env 里的 DATABASE_URL
# ------------------------------------------------------------------
# 在仓库根目录寻找 .env
ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

# ------------------------------------------------------------------
# 2️⃣  读取 alembic.ini，并把 sqlalchemy.url 动态替换
# ------------------------------------------------------------------
config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL", ""))

# 日志配置（保持原样）
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ------------------------------------------------------------------
# 3️⃣  导入 Base 让 Alembic 能扫描所有模型
# ------------------------------------------------------------------
from src.core.models import Base  # <-- 你的 Base 所在模块

target_metadata = Base.metadata

# ------------------------------------------------------------------
# 下面 run_migrations_* 两个函数基本保持默认
# ------------------------------------------------------------------
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # 自动比较字段类型变化（可选）
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
