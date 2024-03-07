
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Phone.entity import Phone
from modules.Phone.model import PhoneInsertRequest, PhoneListResponse, PhoneUpdateRequest, PhoneDeleteRequest

router = APIRouter(prefix="/Phone", tags=["Phone"])


@router.get("/read")
def read(db: Session = Depends(get_db)):
    Positions = db.query(Phone).all()
    return Positions


@router.post("/create")
def create(request: PhoneInsertRequest, db: Session = Depends(get_db)):
    item = Phone(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return PhoneInsertRequest(**item.__dict__)

@router.put("/update/{item_id}")
def update(item_id: int, request: PhoneUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Phone).filter(Phone.id == item_id).first()
    if old_item is None:
        # old_item.update(request.dict())
        return {"message": "Item not found"}
    else:
        old_item.number = request.number
        old_item.name = request.name
        old_item.Contact_id = request.Contact_id
        db.commit()
        db.refresh(old_item)
        return "Updated"
    

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Phone).filter(Phone.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}