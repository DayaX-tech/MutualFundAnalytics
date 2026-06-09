-- 1. Funds with Expense Ratio below 1%
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 2. Top 5 Funds by 3-Year Return
SELECT amfi_code, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 3. Top 5 Funds by Sharpe Ratio
SELECT amfi_code, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 4. Average 1-Year Return
SELECT AVG(return_1yr_pct) AS avg_1yr_return
FROM fact_performance;

-- 5. Highest Alpha Funds
SELECT amfi_code, alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- 6. Lowest Maximum Drawdown
SELECT amfi_code, max_drawdown_pct
FROM fact_performance
ORDER BY max_drawdown_pct DESC
LIMIT 5;

-- 7. Investor Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 8. Transaction Type Distribution
SELECT transaction_type, COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- 9. KYC Status Distribution
SELECT kyc_status, COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;

-- 10. NAV Records per Fund
SELECT amfi_code, COUNT(*) AS nav_records
FROM fact_nav
GROUP BY amfi_code
ORDER BY nav_records DESC;