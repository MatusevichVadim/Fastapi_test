from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel
from datetime import date

app = FastAPI()


@app.get("/hotels")
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: bool | None = None,
        stars: int | None = Query(None, ge=1, le=5),
):
    context = {
        'date_from': date_from,
        'date_to': date_to
    }
    return context

class SchemaBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
    price: int


@app.post("/bookings")
def add_booking(booking: SchemaBooking):
    pass
