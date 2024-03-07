from pydantic import BaseModel


class studentInsertRequest(BaseModel):
    name  : str
    address : int
    age:int
class studentUpdateRequest(BaseModel):
    name  : str
    address : int
    age:int
