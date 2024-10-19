from fastapi import APIRouter, HTTPException, Depends
from datetime import date as Date
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from app.models.supply import SupplyData
from app.models.leaves import TeaLeaf
from app.database import get_db
from app.schemas.schema import SupplyBase

router = APIRouter()

@router.get('/suply/', response_model=List[SupplyBase])
def get_all_suply_data(db: Session = Depends(get_db)):
    """
        Get all supply data
        params:
            db: Session
        return:
            res: List[SupplyData]
    """
    res = db.query(SupplyData).all()
    if not res:
        raise HTTPException(status_code=404, detail="No supply data found")
    return res

@router.get('/type_quntity/')
def get_quantity_of_type(db: Session = Depends(get_db), target_date: Date = Date.today()):
    """
        Get the quantity of each type of tea leaf for a specific date
        params:
            db: Session
            target_date: Date
        return:
            result: List[dict[str, any]]
    """
    res = db.query(
        TeaLeaf.type,
        TeaLeaf.grade,
        func.sum(SupplyData.quantity).label('total_quantity'),
    ).join(
        SupplyData, TeaLeaf.leaf_id == SupplyData.leaf_id
    ).filter(
        func.date(SupplyData.created_at) == target_date
    ).group_by(
        TeaLeaf.type, TeaLeaf.grade
    ).all()

    result = []
    for row in res:
        result.append({
            'type': row.type,
            'grade': row.grade,
            'total_quantity': row.total_quantity
        })
    return result

@router.post('/suply/', response_model=SupplyBase)
def add_supply_data(supply: SupplyBase, db: Session = Depends(get_db)):
    """
        Add new supply data
        params:
            supply: SupplyBase
            db: Session
        return:
            new_supply: SupplyData
        
    """
    new_supply = SupplyData(**supply.model_dump())
    db.add(new_supply)
    db.commit()
    db.refresh(new_supply)
    return new_supply