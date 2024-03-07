

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from core.database import get_db
from modules.Contact.entity import Contact
from modules.Contact.model import InsertNewContact, UpdateContact


router = APIRouter(prefix="/contact", tags=["contact"])

#
# Get Information
#
@router.get("/read")
def gets(db: Session = Depends(get_db)):
    return db.query(Contact).all()

#
# Create/Insert New Contact
#
@router.post("/create")
def create(req: InsertNewContact, db: Session = Depends(get_db)):
    new_Contact = Contact(**req.dict())
    db.add(new_Contact)
    db.commit()
    return "New Contact has been added!"

#
# Update/Change the Contact
#
@router.put("/update/{contact_id}")
def update(item_id: int, req: UpdateContact, db: Session = Depends(get_db)):
    oldContact = db.query(Contact).filter(Contact.id == item_id).first()
    if oldContact is None:
        return "Contact no found!!"
    else: 
        oldContact.firstname = req.firstname
        oldContact.lastname = req.lastname
        oldContact.positionid = req.positionid
        db.commit()
        db.refresh(oldContact)
        return "Contact Info Has Been Updated!!"

#
# Delete Contact
#
@router.delete("/delete")
def delete(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
        return "Contact Has Been Deleted!!"
    return "Contact no found!!"