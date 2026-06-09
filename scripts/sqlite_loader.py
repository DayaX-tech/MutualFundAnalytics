import pandas as pd
from sqlalchemy import create_engine
import os

print("=" * 60)
print("SQLITE DATABASE LOADING")
print("=" * 60)

# Create database folder
os.makedirs("data/db", exist_ok=True)

# SQLite connection
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Read cleaned CSV files
nav = pd.read_csv("data/processed/clean_nav_history.csv")
transactions = pd.read_csv("data/processed/clean_investor_transactions.csv")
performance = pd.read_csv("data/processed/clean_scheme_performance.csv")

# Load into SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("\nTables Loaded Successfully!")

print("\nRow Counts:")
print("fact_nav:", len(nav))
print("fact_transactions:", len(transactions))
print("fact_performance:", len(performance))

print("\nDatabase Created Successfully!")
print("Location: data/db/bluestock_mf.db")