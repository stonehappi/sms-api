from pydantic import BaseModel\

class InsertNewEmail(BaseModel):
    mail: str
    name: str
    contactid: int

class UpdateEmail(BaseModel):
    mail: str
    name: str
    contactid: int