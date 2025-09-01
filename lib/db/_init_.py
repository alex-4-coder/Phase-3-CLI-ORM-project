# lib/db/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Path to your SQLite database (or change to another DB if needed)
DATABASE_URL = "sqlite:///gatekeeper.db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True prints SQL queries for debugging

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Import models so they are registered with Base.metadata
from .models import Base, User, Door, AccessLog
