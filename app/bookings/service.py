"""отдельный слой для работиы с БД, чтобы эта логика была отделена от роутера"""
from sqlalchemy import select

from app.service.base import BaseService
from app.bookings.models import Bookings


class BookingServise(BaseService):
    model = Bookings
