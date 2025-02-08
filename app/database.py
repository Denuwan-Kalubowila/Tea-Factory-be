"""
This module contains the database configuration and session management
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
URL = os.getenv("DATABASE_URL", #url to connect to the database
)
engine = create_engine(URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base= declarative_base()
def get_db():
    """This function returns a database session instance."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()