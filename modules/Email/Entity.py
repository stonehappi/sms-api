from sqlalchemy import Column, ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship
from core.entity import Entity


class Email(Entity, Base):
    __tablename__ = "Email"
    Mail = Column(String)
    Name = Column(String)
    ContactId = Column(Integer, ForeignKey("Contact.id"))
    contact = relationship("Contact", back_populates="emails")


    