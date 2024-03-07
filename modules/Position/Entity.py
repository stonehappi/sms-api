from sqlalchemy import Column, Integer, String
from core.database import Base

from core.entity import Entity


class Position(Entity, Base):
    __tablename__ = "Position"
    Name = Column(String)
    CompanyId = Column(Integer)

    