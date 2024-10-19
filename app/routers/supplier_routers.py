from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.suppliers import Suplier
from app.database import get_db
from app.schemas.schema import SuplierBase

router = APIRouter()

@router.get('/supliers/', response_model=List[SuplierBase])
def get_all_supliers(db: Session = Depends(get_db)):
    """
        Get all suppliers
        params:
            db: Session
        return:
            res: List[Suplier]

    """
    res = db.query(Suplier).all()
    if not res:
        raise HTTPException(status_code=404, detail="No suppliers found")
    return res