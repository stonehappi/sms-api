from pickle import NONE
from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.Position.Entity import Position
from modules.Position.Model import PositionInsertRequest, PositionUpdateRequest


router = APIRouter(prefix="/Position", tags=["Position"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Position).all()


@router.post("/create")
def creat(req: PositionInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    item = Position(**req.dict())
    db.add(item)
    db.commit()
    return "inserted"

@router.put("/update/{item_id}")
def update(
    item_id: int,req:PositionUpdateRequest, db:SessionLocal = Depends(get_db) # type: ignore
):
    oldItem = db.query(Position).filter(Position.id == item_id).first()
    if oldItem is None:
        return "Position not Found"
    else:
        oldItem.name= req.name
        oldItem.address = req.address
        db.commit()
        return "Update Successfull"
    
@router.delete("/dlete/{item_id}")
def delete(
    item_id: int, db:SessionLocal = Depends(get_db) # type: ignore
):      
    oldItem = db.query(Position).filter(Position.id == item_id).first()
    if oldItem is None:
        return "Position not found"
    else : 
        db.delete(oldItem)
        db.commit()
        return "Position has deleted"