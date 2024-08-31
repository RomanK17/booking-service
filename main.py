from fastapi import FastAPI, Query, Depends
import uvicorn
from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.bookings.router import router as booking_router
from app.users.router import router as user_router
from app.pages.router import router as page_router

app = FastAPI()

app.include_router(user_router)
app.include_router(booking_router)
app.include_router(page_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)