import os
import datetime
import logging
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# Ensure the data directory exists for the SQLite file
data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Define the connection string (Using SQLite local file)
DATABASE_URL = "sqlite:///data/market_tracker.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the Market Data Model
class MarketData(Base):
    __tablename__ = "market_data"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    asset_symbol = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    fetched_at = Column(DateTime, default=datetime.datetime.utcnow)

# Define the Expense Model
class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    logged_at = Column(DateTime, default=datetime.datetime.utcnow)

def init_db():
    """Creates the tables in the database if they do not exist."""
    try:
        Base.metadata.create_all(bind=engine)
        logging.info("Database tables initialized or confirmed existing.")
    except Exception as e:
        logging.critical(f"Failed to initialize database: {str(e)}")
        raise e