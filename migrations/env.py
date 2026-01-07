from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import sys
import os

# --- CẤU HÌNH PATH CHUẨN ---
# Lấy đường dẫn thư mục 'migrations' hiện tại
current_path = os.path.dirname(os.path.abspath(__file__))
# Lấy thư mục gốc dự án (Fast-API-Books) bằng cách lùi ra 1 cấp
root_path = os.path.join(current_path, "..")
sys.path.insert(0, os.path.abspath(root_path))
# ---------------------------

from app.core.config import settings
from app.db.base import Base # Import từ file gom models

config = context.config
config.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
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
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()