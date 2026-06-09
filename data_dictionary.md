# Data Dictionary

## 1. NAV History Dataset

| Column Name | Data Type | Description                                   |
| ----------- | --------- | --------------------------------------------- |
| amfi_code   | Integer   | Unique identifier for each mutual fund scheme |
| date        | Date      | NAV recorded date                             |
| nav         | Float     | Net Asset Value of the scheme                 |

---

## 2. Investor Transactions Dataset

| Column Name      | Data Type | Description                 |
| ---------------- | --------- | --------------------------- |
| investor_id      | Integer   | Unique investor identifier  |
| transaction_date | Date      | Date of transaction         |
| transaction_type | String    | SIP, Lumpsum, or Redemption |
| amount           | Float     | Transaction amount          |
| state            | String    | Investor's state            |
| city_tier        | String    | T30 or B30 classification   |
| age_group        | String    | Investor age category       |
| gender           | String    | Investor gender             |
| kyc_status       | String    | KYC verification status     |

---

## 3. Scheme Performance Dataset

| Column Name       | Data Type | Description                           |
| ----------------- | --------- | ------------------------------------- |
| amfi_code         | Integer   | Unique scheme identifier              |
| return_1yr_pct    | Float     | One-year return percentage            |
| return_3yr_pct    | Float     | Three-year return percentage          |
| return_5yr_pct    | Float     | Five-year return percentage           |
| sharpe_ratio      | Float     | Risk-adjusted return measure          |
| sortino_ratio     | Float     | Downside risk-adjusted return measure |
| alpha             | Float     | Excess return over benchmark          |
| beta              | Float     | Market sensitivity measure            |
| expense_ratio_pct | Float     | Annual expense ratio percentage       |
| max_drawdown_pct  | Float     | Maximum decline from peak NAV         |

---

## Source

- Raw datasets provided by Bluestock Fintech Internship.
- Live NAV data fetched from mfapi.in API.
