from datetime import date as Date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.route import Routes
from app.models.check import CheckedRouteQuantity as check_route  

class DailySupply:
    def __init__(self):
        pass
    @staticmethod
    def daily_supply_quantity(db: Session, target_date: Date = Date.today()) -> dict[str, float]:
        try:
            res = db.query(
                func.sum(check_route.quantity).label('total_quantity'),
                func.sum(check_route.prod).label('total_prod'),
                func.sum(check_route.reject).label('total_reject')
            ).filter(
                func.date(check_route.created_at) == target_date
            ).first()

            if res.total_quantity > 0:
                prod_rate = (res.total_prod / res.total_quantity) * 100
            else:
                prod_rate = 0

            if res.total_quantity == 0:
                raise HTTPException(status_code=404, detail="No supply data found")

            return {
                'quantity': res.total_quantity or 0,
                'prod': res.total_prod or 0,
                'reject': res.total_reject or 0,
                'prod_rate': round(prod_rate, 2)
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
    
    @staticmethod
    def daily_supply_from_route(db: Session, target_date: Date = Date.today()) -> list[dict[str, any]]:
       try:
            res = db.query(
            Routes.route_name,
            func.sum(check_route.quantity).label('total_quantity'),
            func.date(check_route.created_at).label('date'),
            ).join(check_route, Routes.route_id == check_route.route_id
            ).filter(
                func.date(check_route.created_at) == target_date
            ).group_by(
                Routes.route_name, func.date(check_route.created_at)
            ).all()
            
            result = []
            for row in res:
                result.append({
                    'route': row.route_name,
                    'total_quantity': row.total_quantity,
                    'date': row.date
                })
            
            return result
       except Exception as e:
           raise HTTPException(status_code=500, detail=str(e)) from e
           