from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.entity import Entity


class Email(Entity, Base):
    __tablename__ = "email"
    mail = Column(String, name="Mail", index=True, unique=True, nullable=False)
    name = Column(String, name="Name")
    contact_id = Column(Integer, ForeignKey("contact.id"), name="ContactId")
    contact = relationship("Contact", back_populates="emails")
