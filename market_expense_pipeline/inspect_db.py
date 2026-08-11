from src.database import SessionLocal, MarketData, Expense

def inspect_database():
    session = SessionLocal()
    try:
        print("\n--- MARKET DATA TABLE ---")
        market_records = session.query(MarketData).order_by(MarketData.fetched_at.desc()).limit(10).all()
        if not market_records:
            print("No market data found.")
        for row in market_records:
            print(f"ID: {row.id} | Asset: {row.asset_symbol:<10} | Price: ${row.price:<10.2f} | Time: {row.fetched_at}")

        print("\n--- EXPENSES TABLE ---")
        expense_records = session.query(Expense).order_by(Expense.logged_at.desc()).limit(10).all()
        if not expense_records:
            print("No expenses found.")
        for row in expense_records:
            print(f"ID: {row.id} | Category: {row.category:<15} | Amount: ${row.amount:<8.2f} | Time: {row.logged_at}")

    except Exception as e:
        print(f"Error reading database: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    inspect_database()