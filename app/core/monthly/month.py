from datetime import date as Date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.check import CheckedRouteQuantity as check_route  # Import check_route from the appropriate module

class MonthSupply:
    @staticmethod
    def monthly_supply_quntity(db: Session,target_date:Date = Date.today())->dict[str,float]:
        res = db.query(
            func.sum(check_route.quantity).label('total_quantity'),
            func.sum(check_route.prod).label('total_prod'),
            func.sum(check_route.reject).label('total_reject'),
        ).filter(
            func.extract('MONTH', check_route.created_at) == target_date.month
        ).first()

        if res.total_quantity > 0:
            prod_rate = (res.total_prod / res.total_quantity) * 100
        else:
            prod_rate = 0

        if res.total_quantity == 0:
            raise HTTPException(status_code=404, detail="No supply data found")
        
        return {
            'quantity':res.total_quantity or 0,
            'prod':res.total_prod or 0,
            'reject':res.total_reject or 0,
            'prod_rate':round(prod_rate,2)
        }
    
