from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from app.database import Base

class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON)
    quantity = Column(Integer)
    image_id = Column(Integer)
