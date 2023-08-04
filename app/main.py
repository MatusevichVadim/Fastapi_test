from fastapi import FastAPI, Query, Depends
from typing import Optional
from pydantic import BaseModel
from datetime import date

from app.bookings.router import router as router_bookings

app = FastAPI()
app.include_router(router_bookings)


class SchemaHotel(BaseModel):
    address: str
    name: str
    stars: int


class SchemaHotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: bool | None = None,
            stars: int | None = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get("/hotels")
def get_hotels(
        search_args: SchemaHotelsSearchArgs = Depends()
) -> list[SchemaHotel]:
    hotels = [
        {
            "address": 'Gagarin st. ap. 1',
            "name": 'Super hotel',
            "stars": 5,
        }
    ]
    context = {
        'date_from': search_args.date_from,
        'date_to': search_args.date_to
    }
    return hotels


# class SchemaBooking(BaseModel):
#     room_id: int
#     date_from: date
#     date_to: date
#     price: int
#
#
# @app.post("/bookings")
# def add_booking(booking: SchemaBooking):
#     pass
