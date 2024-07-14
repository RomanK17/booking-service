from sqlalchemy import Column, Integer, ForeignKey, Date, Computed
from sqlalchemy.ext.hybrid import hybrid_property
from app.database import Base

class Bookings(Base):
     __tablename__ = 'bookings'
     id = Column(Integer, primary_key=True, nullable=False)
     room_id = Column(Integer, ForeignKey('rooms.id'))
     user_id = Column(Integer, ForeignKey('users.id'))
     date_from = Column(Date)
     date_to = Column(Date)
     price = Column(Integer, nullable=False)
     @hybrid_property
     def total_costs(self):
         return (self.date_from - self.date_to).days * self.price
     
     @hybrid_property
     def total_days(self):
         return (self.date_from - self.date_to).days
    #  total_costs = Column(Integer, Computed('(date_from - date_to) * price')) # TODO: протестить, может ли total_costs ссылаться на total_days
    #  total_days = Column(Integer, Computed('date_from - date_to)'))
     image_id = Column(Integer)