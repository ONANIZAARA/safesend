from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates/connects to the SQLite database file
engine = create_engine("sqlite:///safesend.db")

# Base class for all models
Base = declarative_base()

# Session for talking to the database
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()