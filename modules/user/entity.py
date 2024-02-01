from sqlalchemy import Column, Integer, String

from core.database import Base
from core.entity import Entity


class User(Entity, Base):
    __tablename__ = "user"
    username = Column(String, index=True)
    profile_photo = Column(String)
    password = Column(String)
    email = Column(String, index=True)
    age = Column(Integer)
