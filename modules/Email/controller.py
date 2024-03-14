
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from core.database import get_db
from modules.Email.entity import Email
from modules.Email.model import InsertNewEmail, UpdateEmail


router = APIRouter(prefix="/email", tags=["email"])
#
# Get Information
#
@router.get("/read")
def gets(db: Session = Depends(get_db)):
    return db.query(Email).all()

#
# Create/Insert New Email
#
@router.post("/create")
def create(req: InsertNewEmail, db: Session = Depends(get_db)):
    new_email = Email(**req.dict())
    db.add(new_email)
    db.commit()
    return "New Email has been added!"

#
# Update/Change the Email
#
@router.put("/update/{email_id}")
def update(item_id: int, req: UpdateEmail, db: Session = Depends(get_db)):
    oldEmail = db.query(Email).filter(Email.id == item_id).first()
    if oldEmail is None:
        return "Email no found!!"
    else: 
        oldEmail.mail = req.mail
        oldEmail.name = req.name
        oldEmail.contactid = req.contactid
        db.commit()
        db.refresh(oldEmail)
        return "Email Info Has Been Updated!!"

#
# Delete Email
#
@router.delete("/delete")
def delete(email_id: int, db: Session = Depends(get_db)):
    email = db.query(Email).filter(Email.id == email_id).first()
    if email:
        db.delete(email)
        db.commit()
        return "Email Has Been Deleted!!"
    return "Email no found!!"