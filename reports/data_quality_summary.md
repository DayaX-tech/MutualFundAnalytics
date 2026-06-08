# Data Quality Summary

## Dataset Validation Results

- Total Datasets Loaded: 10
- Total Mutual Fund Schemes: 40
- Total NAV Records: 46,000
- Total Investor Transactions: 32,778

## Data Quality Findings

### Missing Values

- 04_monthly_sip_inflows.csv
  - yoy_growth_pct: 12 missing values
  - Expected due to unavailable prior-year comparison periods.

### Duplicate Records

- No duplicate records found across datasets.

### AMFI Validation

- Total Fund Master Codes: 40
- Total NAV Codes: 40
- Missing Codes: 0

### Conclusion

All datasets passed initial quality validation and are suitable for downstream ETL, analytics, dashboarding, and reporting workflows.