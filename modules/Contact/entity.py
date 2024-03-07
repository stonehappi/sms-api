from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.entity import Entity
from core.database import Base


class Contact(Entity, Base):
    __tablename__ = "Contact"
    #id = Column(Integer, primary_key=True)
    First_name = Column(String, unique=True)
    Last_name = Column(String, unique=True)

    Position_id = Column(Integer, ForeignKey("Position.id"))
    position = relationship("Position", backref="Contacts")