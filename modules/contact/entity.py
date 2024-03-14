from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.entity import Entity


class Contact(Entity, Base):
    __tablename__ = "contact"
    firstname = Column(String, name="FirstName")
    lastname = Column(String, name="LastName")
    position_id = Column(Integer, name="PositionId")
    emails = relationship("Email", back_populates="contact")
    phones = relationship("Phone", back_populates="contact")
