from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.check import CheckedRouteQuantity
from app.database import get_db
from app.schemas.schema import CheckedRouteQuntityBase
from pydantic import BaseModel
from app.core.daily.daily import DailySupply
from app.core.monthly.month import MonthSupply

router = APIRouter()

@router.post('/checked/', response_model=CheckedRouteQuntityBase)
def add_checked_route(checked: CheckedRouteQuntityBase, db: Session = Depends(get_db)):
    if checked.quantity - checked.reject == checked.prod:
        new_checked = CheckedRouteQuantity(**checked.dict())
        db.add(new_checked)
        db.commit()
        db.refresh(new_checked)
        return new_checked
    else:
        raise ValueError("Quantity minus reject does not equal production")
    
class Data(BaseModel):
    quantity: int
    prod: int
    reject: int
    prod_rate: float

# GET endpoint to get daily supply
@router.get('/daily_supply_quantity/', response_model=Data)
def get_daily_supply_quantity(db: Session = Depends(get_db)):
    daily_matrix = DailySupply().daily_supply_quntity(db)
    return Data(**daily_matrix)

# GET endpoint to get monthly supply
@router.get('/monthly_supply_quantity/', response_model=Data)
def get_monthly_supply_quantity(db: Session = Depends(get_db)):
    monthly_matrix = MonthSupply().monthly_supply_quntity(db)
    return Data(**monthly_matrix)

# GET endpoint to get daily supply to quantity
@router.get('/daily_supply_prod/')
def get_daily_supply_prod(db: Session = Depends(get_db)):
   return DailySupply().daily_supply_from_route(db)


class week_supply(BaseModel):
    date: datetime
    day_name: str
    total_prod: int
    total_reject: int

# GET endpoint to get week supply to quantity
@router.get('/weekly_supply/',response_model=list[week_supply],status_code=200)
def get_weekly_supply(db: Session = Depends(get_db)):
    try:
        weekly = DailySupply().weekly_supply(db)
        if not weekly:
             raise HTTPException(status_code=404, detail="No supply data found")
        return weekly
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
















# @router.get('/daily_supply_prod/', response_model=Data)
# def get_daily_supply_prod(db: Session = Depends(get_db)):
#     total_prod = DailySupply().daily_supply_to_production(db)
#     return Data(total=total_prod)

# @router.get('/daily_supply_reject/', response_model=Data)
# def get_daily_supply_reject(db: Session = Depends(get_db)):
#     total_reject = DailySupply().daily_supply_to_rejection(db)
#     return Data(total=total_reject)

# @router.get('/monthly_supply_prod/', response_model=Data)
# def get_monthly_supply_prod(db: Session = Depends(get_db)):
#     total_prod = MonthSupply().monthly_supply_to_production(db)
#     return Data(total=total_prod)

# @router.get('/monthly_supply_reject/', response_model=Data)
# def get_monthly_supply_reject(db: Session = Depends(get_db)):
#     total_reject = MonthSupply().monthly_supply_to_rejection(db)
#     return Data(total=total_reject)

# @router.get('/daily_supply_quantity/')
# def get_daily_supply_quantity(db: Session = Depends(get_db)):
#     metrics = DailySupply.get_daily_metrics(db)
#     return {"total": metrics['quantity']}