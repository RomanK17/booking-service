"""базовый класс для работы с БД"""
from sqlalchemy import select

from database import async_session


class BaseService:
    model = None  
    @classmethod
    async def find_all(cls):
        async with async_session() as session:
            query = select(cls.model)
            res = await session.execute(query)
            return res.mappings().all()