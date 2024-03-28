from fastapi import APIRouter, Depends
from core.database import SessionLocal, get_db

from modules.contact.entity import Contact
from modules.contact.model import contactInsertRequest, contactUpdateRequest

router=APIRouter(prefix="/contact",tags=["contact"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Contact).all();#    return"read all admin"

@router.post("/create")
def create(req: contactInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    contact = Contact(**req.dict())
    db.add(Contact)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: contactUpdateRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    olderItem = db.query(Contact).filter(Contact.id==item_id).first()
    if olderItem is None:
        return "Contact not found"
    else:
        olderItem.Firstame=req.Firstname
        olderItem.lastname=req.lastname
        olderItem.Positionid=req.Positionid
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)): # type: ignore
    contact = db.query(Contact).filter(Contact.id == item_id).first()
    if Contact is None:
        return "Contact not found"
    else:
        db.delete(Contact)
        db.commit()
        return "delete successful"