

from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.position.entity import Position
from modules.position.model import PositionInsertRequest, PositionUpdateRequest





router = APIRouter(prefix="/position", tags=["positon"])


@router.post("/Create")
def create(req:PositionInsertRequest, db: SessionLocal = Depends(get_db) ): 
    position = Position(**req.dict())
    db.add(position)
    db.commit()
    return "your record have already checked"


@router.get("/Read")
def read(db: SessionLocal = Depends(get_db)):
    return db.query(Position).all()


@router.put("/Update{item_id}")
def update(item_id: int, req:PositionUpdateRequest, db: SessionLocal = Depends(get_db) ):
    oldItem = db.query(Position).filter(Position.id == item_id).first()
    if oldItem is None:
        return "Position can't be found "
    else:
        # oldItem.Timework = req.T
        oldItem.positonname = req.name
        oldItem.Salary = req.Salary
        oldItem.email = req.email
        oldItem.Address = req. CurrentAddress
        oldItem.timework = req.datetime
        oldItem.newposition = req.newposition
        oldItem.responsibility = req.responsibility
        db.commit()
        db.refresh(oldItem)
        return("Your Position have been Successful for update")
    




@router.delete("/Delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)):
    oldItem = db.query(Position).filter(Position.id == item_id).first()
    if oldItem is None:
        return"the position can be delete due to not found"
    else:
        db.delete(oldItem)
        db.commit()
        return "your Position have been delete successfull for a while" 
    


     