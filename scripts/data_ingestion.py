import pandas as pd
import os

DATA_PATH = "data/raw"

print("=" * 60)
print("MUTUAL FUND DATA INGESTION")
print("=" * 60)

for file in os.listdir(DATA_PATH):

    if file.endswith(".csv"):

        file_path = os.path.join(DATA_PATH, file)

        print("\n" + "=" * 60)
        print(f"FILE: {file}")
        print("=" * 60)

        try:

            df = pd.read_csv(file_path)

            print("\nShape:")
            print(df.shape)

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

        except Exception as e:
            print(f"Error reading {file}: {e}")
            print("\n")
print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())
print("\n")
print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

fund_master_codes = set(fund_master["amfi_code"])

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_master_codes - nav_codes

print(f"\nTotal Fund Master Codes: {len(fund_master_codes)}")
print(f"Total NAV Codes: {len(nav_codes)}")

print("\nMissing Codes:")

if len(missing_codes) == 0:
    print("All AMFI codes validated successfully.")
else:
    print(missing_codes)