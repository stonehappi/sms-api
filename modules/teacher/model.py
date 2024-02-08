from pydantic import BaseModel


class TeacherListResponse(BaseModel):
    id: int
    name: str


class TeacherInsertRequest(BaseModel):
    name: str


class TeacherUpdateRequest(BaseModel):
    name: str
