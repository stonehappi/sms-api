from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from core.database import Base
from core.entity import Entity
from modules.contact.model import contactInsertRequest
from sqlalchemy.orm import relationship


class Email(Entity, Base):
    __tablename__ = "email"
    Name = Column(String, name="Name", index=True, unique=True, nullable=False)
    Email = Column(Integer, name="Email")
    Contactid = Column(Integer, ForeignKey("contact.id"), name="Contactid")
    contact = relationship("Contact", back_populates="emails")
    
