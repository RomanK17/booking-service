from fastapi import FastAPI, Query, Depends
import uvicorn
from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.bookings.router import router as booking_router

app = FastAPI()

app.include_router(booking_router)

class SchemaHotel(BaseModel):
    adress: str
    name: str
    start: int
    

class SearchHotelsArgs(BaseModel):
    def __init__(self,
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool],
    stars: Optional[int] = Query(None, ge=1, le=5) 
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars
        
    

@app.get("/hotels")
def get_hotels( search_args : SearchHotelsArgs = Depends()) -> list[SchemaHotel]:
    return search_args
 
class SchemaBooking(BaseModel):
    room_id : int
    date_from: date
    date_to: date

@app.post('/bookings')
def add_booking(booking: SchemaBooking):
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)