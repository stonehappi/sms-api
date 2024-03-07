

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
# Create/Insert New Position
#
@router.post("/create")
def create(req: InsertNewEmail, db: Session = Depends(get_db)):
    new_position = Email(**req.dict())
    db.add(new_position)
    db.commit()
    return "New Position has been added!"

#
# Update/Change the Position
#
@router.put("/update/{position_id}")
def update(item_id: int, req: UpdateEmail, db: Session = Depends(get_db)):
    oldEmail = db.query(Email).filter(Email.id == item_id).first()
    if oldEmail is None:
        return "Position no found!!"
    else: 
        oldEmail.mail = req.mail
        oldEmail.name = req.name
        oldEmail.contactid = req.contactid
        db.commit()
        db.refresh(oldEmail)
        return "Position Info Has Been Updated!!"

#
# Delete Position
#
@router.delete("/delete")
def delete(position_id: int, db: Session = Depends(get_db)):
    position = db.query(Email).filter(Email.id == position_id).first()
    if position:
        db.delete(position)
        db.commit()
        return "Position Has Been Deleted!!"
    return "Position no found!!"