"""отдельный слой для работиы с БД, чтобы эта логика была отделена от роутера"""
from sqlalchemy import select

from service.base import BaseService
from bookings.models import Bookings

class BookingServise(BaseService):
    model = Bookings
