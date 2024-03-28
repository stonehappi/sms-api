from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db, SessionLocal
from modules.Phone.model import PhoneInsertRequest, PhoneUpdateRequest
from modules.Phone.entity import Phone

router = APIRouter(prefix="/Phone", tags=["Phone"])


@router.get("/read/")
def get(db: Session = Depends(get_db)):
    Phones = db.query(Phone).all()
    return Phones


@router.post("/create/")
def create(request:  PhoneInsertRequest, db: Session = Depends(get_db)):
    item = Phone(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/update/{item_id}")
def update(item_id: int, request: PhoneUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Phone).filter(Phone.id == item_id).first()
    if old_item:
        old_item.number = request.number
        old_item.name = request.name
        old_item.contactId = request.contactid
        db.commit()
        db.refresh(old_item)
        return old_item
    return {"message": "shit your Item not found"}

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Phone).filter(Phone.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item already deleted successfully"}
    return {"message": "Item cannot found"}
