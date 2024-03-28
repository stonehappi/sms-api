
from pydantic import BaseModel 

class EmailListResponse(BaseModel):
    id: int
    mails: str
    namelocation: str
    contactId: int
    status: str
class EmailInsertRequest(BaseModel):  # type: ignore
    mails: str
    namelocation: str
    contactId: int
    status: str
class EmailUpdateRequest(BaseModel):  # type: ignore
    mails: str
    namelocation: str
    contactId: int
    status: str