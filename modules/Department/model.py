from pydantic import BaseModel


class DepartmentInsertRequest(BaseModel):
        name: str
        short_name: str
        floor: int
class DepartmentUpdateRequest(BaseModel):
        name: str
        short_name: str
        floor : int
        room : int