from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List
from app.models.suppliers import Suplier
from app.database import get_db
from app.schemas.schema import SuplierBase

router = APIRouter()

@router.get('/supliers/', response_model=List[SuplierBase])
def get_all_supliers(db: Session = Depends(get_db)):
    """
    This endpoint returns a list of all suppliers in the database.

    Args:
        db (Session): A database session.

    Returns:
        List[SuplierBase]: A list of all suppliers in the database.
    """
    res = db.query(Suplier).all()

    # Use a generator to stream the response
    def stream():
        """
        Generator to stream the response
        """
        for suplier in res:
            yield suplier

    if not res:
        # Raise an exception if no suppliers are found
        raise HTTPException(status_code=404, detail="No suppliers found")
    
    # Return a StreamingResponse
    return StreamingResponse(stream(), media_type="application/json")
