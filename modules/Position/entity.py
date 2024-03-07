

from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class Position(Entity, Base):
    __tablename__ = "position"
    name = Column(String, index=True)
    companyid = Column(Integer)