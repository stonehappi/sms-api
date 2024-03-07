from pydantic import BaseModel


class PhoneInsertRequest(BaseModel):
    Number : int
    Name : str
    ContactId : int
class PhoneUpdateRequest(BaseModel):
    Number : int
    Name : str
    ContactId : int
class PhoneRespon(BaseModel):
    Number : int
    Name : str
    ContactId : int
