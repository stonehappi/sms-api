from pydantic import BaseModel


class contactInsertRequest(BaseModel):
    Firstname  : str
    LatName : str
    PositionId : int
class contactUpdateRequest(BaseModel):
    Firstname  : str
    LatName : str
    PositionId : int
