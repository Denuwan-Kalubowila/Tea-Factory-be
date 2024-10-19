"""This module contains the pydantic schema for the application."""
from pydantic import BaseModel

class TeaLeafBase(BaseModel):
    """
        This class defines the schema for the tea leaf model.
        leaf_type: str
        grade: str
    """
    type: str
    grade: str

    class Config:
        orm_mode = True

class RouteBase(BaseModel):
    """
        This class defines the schema for the route model.
        route_name: str
        distance: int

    """
    route_name: str
    distance: int

    class Config:
        orm_mode = True

class SuplierBase(BaseModel):

    """
        This class defines the schema for the suplier model.
        username: str
        first_name: str
        last_name: str
        phone: str
        email: str
        role: str

    """
    username: str
    first_name: str
    last_name: str
    phone: str
    email: str
    role: str

    class Config:
        orm_mode = True

class SupplyBase(BaseModel):
    """
        This class defines the schema for the supply model.
        suplier_id: int
        leaf_id: int
        quantity: int
        route_id: int
    """
    suplier_id: int
    leaf_id: int
    quantity: int
    route_id: int

    class Config:
        orm_mode = True

class CheckedRouteQuntityBase(BaseModel):
    """
        This class defines the schema for the checked route quantity model.
        route_id: int
        quantity: int
        prod: int
        reject: int
    """
    route_id: int
    quantity: int
    prod: int
    reject: int

    class Config:
        orm_mode = True

class ProgressBase(BaseModel):
    """
        This class defines the schema for the progress model.
        quantity: int
        prod: int
        reject: int
        prod_rate: float
    """
    route: int
    prod: int
    reject: int
    prod_rate: float

    class Config:
        orm_mode = True
