from sqlalchemy import Column, ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship
from core.entity import Entity


class Phone(Entity, Base):
    __tablename__ = "Phone"
    Number = Column(Integer)
    Name = Column(String)
    ContactId = Column(Integer, ForeignKey("Contact.id"))
    contact = relationship("Contact", back_populates="phones")
    