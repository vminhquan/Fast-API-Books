from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engire = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread" : False} if settings.SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {},
)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engire)