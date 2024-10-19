from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.route import Routes
from app.database import get_db
from app.schemas.schema import RouteBase

router = APIRouter()

@router.get('/routes/', response_model=List[RouteBase])
def get_all_routes(db: Session = Depends(get_db)):
    """
        Get all routes
        params:
            db: Session
        return:
            res: List[Routes]
    """
    res = db.query(Routes).all()
    if not res:
        raise HTTPException(status_code=404, detail="No tea leaves found")
    return res