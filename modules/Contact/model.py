

from pydantic import BaseModel


class InsertNewContact(BaseModel):
    firstname: str
    lastname: str
    positionid: int

class UpdateContact(BaseModel):
    firstname: str
    lastname: str
    positionid: int