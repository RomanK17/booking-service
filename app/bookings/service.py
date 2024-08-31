"""отдельный слой для работиы с БД, чтобы эта логика была отделена от роутера"""
from sqlalchemy import func, select, and_, or_, insert
from datetime import date
from app.rooms.models import Rooms
from app.service.base import BaseService
from app.bookings.models import Bookings
from app.database import engine, async_session


class BookingServise(BaseService):
    model = Bookings
    
    @classmethod
    async def add(cls,  user_id : id,  room_id : int, date_from : date, date_to : date):
        """
        SELECT * FROM rooms;
        /* TODO: нужно прочекать второе условие, когда добавлю броинрование */

        WITH booked_rooms AS (
            SELECT * FROM bookings
            WHERE room_id=1 AND
                (date_from >= '2023-05-15' AND date_from <= '2023-06-20')
            OR (date_from <= '2023-05-15' AND date_to > '2023-06-20' )
        )

        SELECT rooms.quantity - COUNT(booked_rooms.id) FROM rooms
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id=booked_rooms.id # TODO: WHERE скорее всего не обязательно
        GROUP BY rooms.quantity, booked_rooms.room_id
        """
        async with async_session() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == room_id,
                    or_(
                        and_(Bookings.date_from >= date_from, Bookings.date_from <= date_to),
                        and_(Bookings.date_from <= date_from, Bookings.date_to > date_from)
                    )
                )
            ).alias("booked_rooms")

            get_rooms_left = select(
                (Rooms.quantity - func.count(booked_rooms.c.id)).label('rooms_left')
            ).select_from(Rooms).join(booked_rooms, Rooms.id == booked_rooms.c.room_id, isouter=True).where(Rooms.id == room_id).group_by(Rooms.quantity, booked_rooms.c.room_id)

            res = await session.execute(get_rooms_left)
            res : int = res.scalar()


            if res > 0:
                get_price = select(Rooms.price).filter(Rooms.id == room_id)
                price = await session.execute(get_price)
                price : int = price.scalar()
                add_bookings = insert(Bookings).values(
            room_id = room_id,
            user_id = user_id,
            date_from = date_from,
            date_to = date_to,
            price = price,
                ).returning(Bookings)

                new_booking = await session.execute(add_bookings)
                await session.commit()
                return new_booking
            else:
                return None

