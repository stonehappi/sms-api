# from sqlalchemy import Column, Integer, String

# from core.database import Base
# from core.entity import Entity


from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class Teacher(Entity, Base):
    __tablename__ = "teacher"
    fullname = Column(String, index=True)
    age = Column(Integer)
    address = Column(String)
    # email = Column(String, index=True)
    # bod = Column(Integer)
