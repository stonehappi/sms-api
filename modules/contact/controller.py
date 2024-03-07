from fastapi import APIRouter, Depends
from core.database import SessionLocal, get_db

from modules.contact.entity import contact
from modules.contact.model import contactInsertRequest, contactUpdateRequest

router=APIRouter(prefix="/contact",tags=["contact"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(contact).all();#    return"read all admin"

@router.post("/create")
def create(req: contactInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    contact = contact(**req.dict())
    db.add(contact)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: contactUpdateRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    olderItem = db.query(contact).filter(contact.id==item_id).first()
    if olderItem is None:
        return "contact not found"
    else:
        olderItem.number=req.number
        olderItem.name=req.name
        olderItem.contactid=req.contactid
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)): # type: ignore
    contact = db.query(contact).filter(contact.id == item_id).first()
    if contact is None:
        return "contact not found"
    else:
        db.delete(contact)
        db.commit()
        return "delete successful"