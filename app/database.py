from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from config import DB_URL


 
engine = create_async_engine(DB_URL)
# AsyncSession - асинхронная сессия, expire_on_commit - сессия не закрывается после записи в БД
async_session = sessionmaker(engine, class_= AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    """класс для хранения метаданных о всех таблицах"""
    pass 