
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Email.entity import Email
from modules.Email.model import EmailInsertRequest, EmailListResponse, EmailUpdateRequest, EmailDeleteRequest

router = APIRouter(prefix="/Email", tags=["Email"])


@router.get("/read")
def read(db: Session = Depends(get_db)):
    Emails = db.query(Email).all()
    return Emails


@router.post("/create")
def create(request: EmailInsertRequest, db: Session = Depends(get_db)):
    item = Email(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return EmailInsertRequest(**item.__dict__)

@router.put("/update/{item_id}")
def update(item_id: int, request: EmailUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Email).filter(Email.id == item_id).first()
    if old_item is None:
        # old_item.update(request.dict())
        return {"message": "Item not found"}
    else:
        old_item.mail = request.mail
        old_item.name = request.name
        old_item.Contact_id = request.Contact_id
        db.commit()
        db.refresh(old_item)
        return "Updated"
    

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Email).filter(Email.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}