from numbers import Integral
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class Admin(Entity, Base):
    __tablename__="admin"
    fullname = Column(String)
    password = Column(String)
    device = Column(Integer)
    email = Column(Integral)
    