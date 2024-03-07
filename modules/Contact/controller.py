from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Contact.entity import Contact
from modules.Contact.model import ContactInsertRequest, ContactListResponse, ContactUpdateRequest, ContactDeleteRequest

router = APIRouter(prefix="/Contact", tags=["Contact"])


@router.get("/read")
def read(db: Session = Depends(get_db)):
    contacts = db.query(Contact).all()
    return contacts


@router.post("/create")
def create(request: ContactInsertRequest, db: Session = Depends(get_db)):
    item = Contact(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return ContactInsertRequest(**item.__dict__)

@router.put("/update/{item_id}")
def update(item_id: int, request: ContactUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Contact).filter(Contact.id == item_id).first()
    if old_item is None:
        # old_item.update(request.dict())
        return {"message": "Item not found"}
    else:
        old_item.First_name = request.First_name
        old_item.Last_name = request.Last_name
        old_item.Position_id = request.Position_id
        db.commit()
        db.refresh(old_item)
        return "Updated"
    

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Contact).filter(Contact.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}