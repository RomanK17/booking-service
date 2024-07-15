"""базовый класс для работы с БД"""
from sqlalchemy import select

from app.database import async_session


class BaseService:
    model = None  
    
    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=model_id)
            res = await session.execute(query)
            return res.scalar_one_or_none()
        
        
    @classmethod
    async def find_one_or_none(cls, filters):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filters)
            res = await session.execute(query)
            return res.scalar_one_or_none()
    
    @classmethod
    async def find_all(cls, **filters):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filters)
            res = await session.execute(query)
            return res.scalars().all()