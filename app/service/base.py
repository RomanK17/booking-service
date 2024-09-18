"""базовый класс для работы с БД"""
from sqlalchemy import select, insert, delete

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
    async def find_one_or_none(cls, **filters):
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
    
    
    @classmethod
    async def insert_data(cls, **data):
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_data(cls, **filters):
        """Два варианта, как можно написать этот метод:
        1. Сразу удаляем все записи (если их нет, то ничего не удалится). Проблема в том, что тогда мы не можем узнать, удалялось ли что-то
        2. Делаем запрос -> если находтся забронированные номера, то мы их удаляем."""
        async with async_session() as session:
            await session.execute(delete(cls.model).filter_by(**filters))
            await session.commit()


