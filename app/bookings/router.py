from fastapi import APIRouter
from sqlalchemy import select

from bookings.service import BookingServise

router = APIRouter(prefix='/bookings', tags=['Bookings'])

@router.get('')
async def get_bookings():
    return await BookingServise.find_all()