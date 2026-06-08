import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

print("=" * 60)
print("NAV HISTORY CLEANING")
print("=" * 60)

nav = pd.read_csv("data/raw/02_nav_history.csv")

print("\nOriginal Shape:")
print(nav.shape)

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort values
nav = nav.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Validate NAV > 0
nav = nav[nav["nav"] > 0]

print("\nCleaned Shape:")
print(nav.shape)

nav.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("\nSaved Successfully")
print("\n")
print("=" * 60)
print("INVESTOR TRANSACTIONS CLEANING")
print("=" * 60)

transactions = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("\nOriginal Shape:")
print(transactions.shape)

# Convert date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Standardize transaction types
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only positive amounts
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Standardize KYC status
transactions["kyc_status"] = (
    transactions["kyc_status"]
    .str.strip()
    .str.title()
)

print("\nCleaned Shape:")
print(transactions.shape)

print("\nTransaction Types:")
print(transactions["transaction_type"].unique())

print("\nKYC Status:")
print(transactions["kyc_status"].unique())

transactions.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("\nInvestor Transactions Saved Successfully")
print("\n")
print("=" * 60)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 60)

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("\nOriginal Shape:")
print(performance.shape)

numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in numeric_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

print("\nMissing Values:")
print(
    performance[numeric_columns]
    .isnull()
    .sum()
)

print("\nExpense Ratio Range:")
print(
    performance["expense_ratio_pct"].min(),
    "to",
    performance["expense_ratio_pct"].max()
)

performance.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("\nScheme Performance Saved Successfully")