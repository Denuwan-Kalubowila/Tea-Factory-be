from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.leaves import TeaLeaf
from app.database import get_db
from app.schemas.schema import TeaLeafBase

router = APIRouter()

@router.get('/leaves/', response_model=List[TeaLeafBase])
def get_all_leaves(db: Session = Depends(get_db)):
    """
        Get all tea leaves
        params:
            db: Session
        return:
            res: List[TeaLeaf]
    """
    res = db.query(TeaLeaf).all()
    if not res:
        raise HTTPException(status_code=404, detail="No tea leaves found")
    return res