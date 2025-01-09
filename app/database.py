"""
This module contains the database configuration and session management
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL = os.getenv('DB_URL')

engine= create_engine("postgresql://postgres:teaApp32#$$@database-tea-factory.cx8ygyuusoap.us-east-1.rds.amazonaws.com:5432/tea_users")
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base= declarative_base()

def get_db():
    """This function returns a database session instance."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()