import requests
import logging
from src.database import SessionLocal, MarketData, Expense

# Free public API endpoint (no key required for basic rates)
COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

def fetch_market_prices():
    """Fetches live market prices from the API with proper error logging."""
    logging.info("Attempting to fetch market prices from CoinGecko API...")
    try:
        response = requests.get(COINGECKO_URL, timeout=10)
        # Raise HTTPError if response code is not 200 OK
        response.raise_for_status() 
        data = response.json()
        
        logging.info("Successfully fetched raw market data from API.")
        return data
    except requests.exceptions.Timeout:
        logging.error("API request timed out. Check network connection.")
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch market data: {str(e)}")
        return None

def store_market_data(api_data):
    """Parses API response and saves records to the database using SQLAlchemy ORM."""
    if not api_data:
        logging.warning("No API data received. Skipping database insertion.")
        return

    session = SessionLocal()
    records_inserted = 0

    try:
        # Map JSON structure to database objects
        # CoinGecko returns: {'bitcoin': {'usd': 60000}, 'ethereum': {'usd': 3000}, ...}
        for asset, rates in api_data.items():
            price = rates.get('usd')
            if price is not None:
                market_record = MarketData(
                    asset_symbol=asset.upper(),
                    price=float(price)
                )
                session.add(market_record)
                records_inserted += 1

        # Commit transaction to database
        session.commit()
        logging.info(f"Successfully committed {records_inserted} market records to database.")

    except Exception as e:
        session.rollback() # Revert changes if transaction fails
        logging.error(f"Database transaction failed. Rolling back changes. Error: {str(e)}")
    finally:
        session.close() # Always close the session

def add_manual_expense(category: str, amount: float):
    """Helper function to log expenses into the database."""
    session = SessionLocal()
    try:
        expense_record = Expense(category=category, amount=amount)
        session.add(expense_record)
        session.commit()
        logging.info(f"Expense logged successfully: {category} - ${amount}")
    except Exception as e:
        session.rollback()
        logging.error(f"Failed to log expense: {str(e)}")
    finally:
        session.close()

def run_pipeline():
    """Main execution sequence for the pipeline."""
    # 1. Fetch live market rates
    raw_data = fetch_market_prices()
    
    # 2. Save market rates to DB
    store_market_data(raw_data)
    
    # 3. Insert a sample expense to verify the expenses table works
    add_manual_expense("Server Hosting", 15.50)