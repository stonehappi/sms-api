
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Position.entity import Position
from modules.Position.model import PositionInsertRequest, PositionListResponse, PositionUpdateRequest, PositionDeleteRequest

router = APIRouter(prefix="/Position", tags=["Position"])


@router.get("/read")
def read(db: Session = Depends(get_db)):
    positions = db.query(Position).all()
    return positions


@router.post("/create")
def create(request: PositionInsertRequest, db: Session = Depends(get_db)):
    item = Position(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return PositionInsertRequest(**item.__dict__)

@router.put("/update/{item_id}")
def update(item_id: int, request: PositionUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Position).filter(Position.id == item_id).first()
    if old_item is None:
        # old_item.update(request.dict())
        return {"message": "Item not found"}
    else:
        old_item.name = request.name
        old_item.Company_id = request.Company_id
        db.commit()
        db.refresh(old_item)
        return "Updated"
    

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Position).filter(Position.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}