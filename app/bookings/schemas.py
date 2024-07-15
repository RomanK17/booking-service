from pydantic import BaseModel
from datetime import date    

class BookingsSchema(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    # total_costs: int #TODO: добавить эти поля в БД
    # total_days : int
    class Config:
        orm_mode = True
        from_attributes = True
    