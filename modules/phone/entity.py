from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base
from core.entity import Entity


class Phone(Entity, Base):
    __tablename__ = "phone"
    number = Column(String, name="Number", index=True, unique=True, nullable=False)
    name = Column(String, name="Name")
    contact_id = Column(Integer, ForeignKey("contact.id"), name="ContactId")
    contact = relationship("Contact", back_populates="phones")
