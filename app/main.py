"""
This module initializes and configures the FastAPI application.
It includes the following routers:
- routes_routers
- supplier_routers
- leaves_routers
- checked_routers
- supply_routers
It also sets up the database by creating all the necessary tables.
Attributes:
    app (FastAPI): The FastAPI application instance.
"""
from fastapi import FastAPI
from app.routers import routes_routers, supplier_routers, leaves_routers, checked_routers,supply_routers
from app.database import Base, engine

app = FastAPI()
app.include_router(routes_routers.router)
app.include_router(supplier_routers.router)
app.include_router(leaves_routers.router)
app.include_router(checked_routers.router)
app.include_router(supply_routers.router)

Base.metadata.create_all(bind=engine)
