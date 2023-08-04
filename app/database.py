# import os
#
# import dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings

# dotenv.load_dotenv()
#
# DB_USER = str(os.getenv("DB_USER"))
# DB_PASS = str(os.getenv("DB_PASS"))
# DB_HOST = str(os.getenv("DB_HOST"))
# DB_PORT = str(os.getenv("DB_PORT"))
# DB_NAME = str(os.getenv("DB_NAME"))
#
#
# SQLALCHEMY_DATABASE_URL = (
#     f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

# engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
engine = create_async_engine(settings.get_database_url())

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
