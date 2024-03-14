
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Position.entity import Position
from modules.Position.model import InsertNewPosition, UpdatePosition


router = APIRouter(prefix="/position", tags=["position"])

#
# Get Information
#
@router.get("/read")
def gets(db: Session = Depends(get_db)):
    return db.query(Position).all()

#
# Create/Insert New Position
#
@router.post("/create")
def create(req: InsertNewPosition, db: Session = Depends(get_db)):
    new_position = Position(**req.dict())
    db.add(new_position)
    db.commit()
    return "New Position has been added!"

#
# Update/Change the Position
#
@router.put("/update/{position_id}")
def update(item_id: int, req: UpdatePosition, db: Session = Depends(get_db)):
    oldPosition = db.query(Position).filter(Position.id == item_id).first()
    if oldPosition is None:
        return "Position no found!!"
    else: 
        oldPosition.name = req.name
        oldPosition.companyid = req.companyid
        db.commit()
        db.refresh(oldPosition)
        return "Position Info Has Been Updated!!"

#
# Delete Position
#
@router.delete("/delete")
def delete(position_id: int, db: Session = Depends(get_db)):
    position = db.query(Position).filter(Position.id == position_id).first()
    if position:
        db.delete(position)
        db.commit()
        return "Position Has Been Deleted!!"
    return "Position no found!!"