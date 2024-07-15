from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.service import BookingServise
from app.bookings.schemas import BookingsSchema

router = APIRouter(prefix='/bookings', tags=['Bookings'])

@router.get('')
async def get_bookings() -> list[BookingsSchema]:
    return await BookingServise.find_all()