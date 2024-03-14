
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Phone.model import InsertNewPhone, UpdatePhone
from modules.Phone.entity import Phone


router = APIRouter(prefix="/phone", tags=["phone"])

#
# Get Information
#
@router.get("/read")
def gets(db: Session = Depends(get_db)):
    return db.query(Phone).all()

#
# Create/Insert New Phone
#
@router.post("/create")
def create(req: InsertNewPhone, db: Session = Depends(get_db)):
    new_phone = Phone(**req.dict())
    db.add(new_phone)
    db.commit()
    return "New Phone has been added!"

#
# Update/Change the Phone
#
@router.put("/update/{phone_id}")
def update(phone_id: int, req: UpdatePhone, db: Session = Depends(get_db)):
    oldphone = db.query(Phone).filter(Phone.id == phone_id).first()
    if oldphone is None:
        return "Phone no found!!"
    else:
        oldphone.number = req.number 
        oldphone.name = req.name
        oldphone.contactid = req.contactid
        db.commit()
        db.refresh(oldphone)
        return "Phone Info Has Been Updated!!"

#
# Delete Phone 
#
@router.delete("/delete")
def delete(phone_id: int, db: Session = Depends(get_db)):
    phone = db.query(Phone).filter(Phone.id == phone_id).first()
    if phone:
        db.delete(phone)
        db.commit()
        return "Phone Has Been Deleted!!"
    return "Phone no found!!"