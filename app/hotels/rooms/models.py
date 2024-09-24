from sqlalchemy import JSON, Column, Integer, String, ForeignKey, Date, Computed
from app.database import Base
from sqlalchemy.orm import relationship


class  Rooms(Base):
     __tablename__ = 'Rooms'
     id = Column(Integer, primary_key=True, nullable=False)
     hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False )
     name = Column(String, nullable=False )
     description = Column(String, nullable=False )
     price = Column(Integer, nullable=False )
     services = Column(JSON)
     quantity = Column(Integer, nullable=False )
     image_id = Column(Integer)

     hotel = relationship("Hotels", back_populates="rooms")