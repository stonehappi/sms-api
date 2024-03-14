from pydantic import BaseModel


class EmailListResponse(BaseModel):
    id: int
    mail: str
    name: str
    contact_id: int


class EmailInsertRequest(BaseModel):
    mail: str
    name: str
    contact_id: int


class EmailUpdateRequest(BaseModel):
    mail: str
    name: str
    contact_id: int
