import pandas as pd
import requests
import os

# Create folder if it doesn't exist
os.makedirs("data/raw/live_nav", exist_ok=True)

# Fund Codes
funds = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("=" * 60)
print("LIVE NAV FETCH")
print("=" * 60)

for fund_name, amfi_code in funds.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    try:

        response = requests.get(url)

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = f"data/raw/live_nav/{fund_name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"SUCCESS: {fund_name}")

    except Exception as e:

        print(f"ERROR: {fund_name}")
        print(e)