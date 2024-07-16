from fastapi import APIRouter, Depends, Request
from sqlalchemy import select

from app.bookings.service import BookingServise
from app.bookings.schemas import BookingsSchema
from app.users.dependencies import get_current_user_id

router = APIRouter(prefix='/bookings', tags=['Bookings'])

@router.get('')
async def get_bookings(user_id: int = Depends(get_current_user_id)) -> list[BookingsSchema]:
    
    return await BookingServise.find_all(user_id=user_id)