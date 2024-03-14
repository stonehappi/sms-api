from sqlalchemy import Column, Integer, String

from core.database import Base
from core.entity import Entity


class Building(Entity, Base):
    __tablename__ = "building"
    name = Column(String, name="Name", index=True, unique=True, nullable=False)
