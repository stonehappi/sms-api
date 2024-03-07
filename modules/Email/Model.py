from pydantic import BaseModel


class EmailInsertRequest(BaseModel):
    Mail : str
    Name : str
    ContactId : int

class EmailUpdateRequest(BaseModel):
    Mail : str
    Name : str
    ContactId : int
class EmailRespon(BaseModel):
    Mail : str
    Name : str
    ContactId : int
