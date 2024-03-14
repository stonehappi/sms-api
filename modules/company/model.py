from pydantic import BaseModel


class CompanyListResponse(BaseModel):
    id: int
    name: str
    address: str


class CompanyInsertRequest(BaseModel):
    name: str
    address: int


class CompanyUpdateRequest(BaseModel):
    name: str
    address: str
