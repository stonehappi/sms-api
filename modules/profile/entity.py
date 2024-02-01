from sqlalchemy import Column, String, Integer
from core.database import Base
from core.entity import Entity


class Profile(Entity, Base):
    __tablename__ = "profile"
    first_name = Column(String, index=True, max_length=50)
    last_name = Column(String, index=True, max_length=50)
    profile_photo = Column(String)
    user_id = Column(Integer, index=True)
    address = Column(String, index=True, max_length=100)
    phone = Column(String, index=True, max_length=20)
