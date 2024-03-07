
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from modules.Company.entity import Company
from modules.Company.model import InsertNewCompanyName, UpdateCompany


router = APIRouter(prefix="/company", tags=["company"])

#
# Get Information
#
@router.get("/read")
def gets(db: Session = Depends(get_db)):
    return db.query(Company).all()

#
# Create/Insert New Company
#
@router.post("/create")
def create(req: InsertNewCompanyName, db: Session = Depends(get_db)):
    new_company = Company(**req.dict())
    db.add(new_company)
    db.commit()
    return "New Company has been added!"

#
# Update/Change the Company
#
@router.put("/update/{company_id}")
def update(item_id: int, req: UpdateCompany, db: Session = Depends(get_db)):
    oldCompany = db.query(Company).filter(Company.id == item_id).first()
    if oldCompany is None:
        return "Company no found!!"
    else: 
        oldCompany.name = req.name
        oldCompany.address = req.address
        db.commit()
        db.refresh(oldCompany)
        return "Company Info Has Been Updated!!"

#
# Delete Company
#
@router.delete("/delete")
def delete(company_id: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == company_id).first()
    if company:
        db.delete(company)
        db.commit()
        return "Company Has Been Deleted!!"
    return "Company no found!!"