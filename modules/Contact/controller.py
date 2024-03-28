from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db, SessionLocal
from modules.Contact.model import ContactInsertRequest,ContactListResponse, ContactUpdateRequest
from modules.Contact.entity import Contact

router = APIRouter(prefix="/Contact", tags=["Contact"])


@router.get("/read/")
def get(db: Session = Depends(get_db)):
    contacts = db.query(Contact).all()
    return contacts


@router.post("/create/")
def create(request: ContactInsertRequest, db: Session = Depends(get_db)):
    item = Contact(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/update/{item_id}")
def update(item_id: int, request: ContactUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Contact).filter(Contact.id == item_id).first()
    if old_item:
        old_item.Id = request.Id
        old_item.Firstname = request.Firstname
        old_item.Lastname = request.Lastname
        old_item.Positionid = request.Positionid
        db.commit()
        db.refresh(old_item)
        return old_item
    return {"message": " Bruhh your Item not found"}

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Contact).filter(Contact.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item already deleted successfully"}
    return {"message": "Item not found in your program"}
