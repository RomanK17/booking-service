from datetime import date
from fastapi import APIRouter, Depends, Request
from sqlalchemy import select

from app.bookings.service import BookingServise
from app.bookings.schemas import BookingsSchema
from app.exceptions import RoomCannotBeBooked
from app.users.dependencies import get_current_user_id
from app.users.models import Users

router = APIRouter(prefix='/bookings', tags=['Bookings'])

@router.get('')
async def get_bookings(user_id: int = Depends(get_current_user_id)) -> list[BookingsSchema]:
    return await BookingServise.find_all(user_id=user_id)


@router.post('/add')
async def add_booking(room_id: int, date_from: date, date_to: date, user_id: int = Depends(get_current_user_id)):
    booking = await BookingServise.add(user_id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked



@router.post('/delete')
async def delete_booking(booking_id : int, user_id: int = Depends(get_current_user_id)):
    deleted_bookings = await BookingServise.delete_data(id=booking_id, user_id=user_id)