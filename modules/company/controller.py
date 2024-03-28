from fastapi import APIRouter, Depends
from core.database import SessionLocal, get_db

from modules.company.entity import Company
from modules.company.model import companyInsertRequest, companyUpdateRequest

router=APIRouter(prefix="/company",tags=["company"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Company).all();#    return"read all admin"

@router.post("/create")
def create(req: companyInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    company = Company(**req.dict())
    db.add(company)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: companyUpdateRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    olderItem = db.query(Company).filter(Company.id==item_id).first()
    if olderItem is None:
        return "company not found"
    else:
        olderItem.Name=req.Name
        olderItem.Address=req.Address
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)): # type: ignore
    company = db.query(Company).filter(Company.id == item_id).first()
    if Company is None:
        return "Company not found"
    else:
        db.delete(Company)
        db.commit()
        return "delete successful"