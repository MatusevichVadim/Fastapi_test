from fastapi import APIRouter

router = APIRouter(
    prefix="/bookings",
    tags=['Бронирования'],
)


@router.get('')
def get_booking():
    pass


@router.get("/{booking_id}")
def get_booking(booking_id):
    pass
