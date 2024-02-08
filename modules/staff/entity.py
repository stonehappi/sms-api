


from sqlalchemy import Column, Date, Float, Integer, String, Time

from core.database import Base
from core.entity import Entity

class Staff(Entity, Base):
    __tablename__ = "staff"
    fullname = Column(String, index=True)
    age = Column(Integer)
    startdate = Column(Date)
    salary = Column(Float)
    workhour = Column(Float)
    position = Column(String)
    department = Column(String)
    location = Column(String)
    attendance_daily = Column(Time)
    email = Column(String)