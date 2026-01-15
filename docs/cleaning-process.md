\# Data Cleaning Process



\*\*Date:\*\* January 15, 2026



\## Problems Fixed



\### 1. Date Format Issue

\- \*\*Problem:\*\* InvoiceDate stored as text

\- \*\*Solution:\*\* Converted to datetime using `pd.to\_datetime()`

\- \*\*Result:\*\* Can now analyze by year, month, day, hour



\### 2. Missing Product Descriptions (1,454 rows)

\- \*\*Decision:\*\* Removed these rows (0.27% of data)

\- \*\*Reasoning:\*\* Cannot analyze products without descriptions



\### 3. Negative Prices (outliers/bad data)

\- \*\*Problem:\*\* Some prices were negative or zero

\- \*\*Solution:\*\* Kept only positive unit prices

\- \*\*Result:\*\* 539,392 valid rows



\### 4. Returns vs Sales

\- \*\*Problem:\*\* Mixed returns with sales (invoices starting with 'C')

\- \*\*Solution:\*\* Created IsReturn flag, separated into 2 datasets

\- \*\*Result:\*\* 

&nbsp; - Sales: 530,104 rows

&nbsp; - Returns: 9,288 rows



\### 5. Missing CustomerIDs (135,080 rows)

\- \*\*Decision:\*\* Kept the data but flagged with HasCustomerID column

\- \*\*Reasoning:\*\* Valuable for sales analysis even without customer info

\- \*\*Use case:\*\* Guest checkouts or incomplete data entry



\### 6. Created Calculated Columns

Added these columns for analysis:

\- \*\*Revenue\*\* = Quantity × UnitPrice

\- \*\*Year, Month, MonthName\*\* (for time series)

\- \*\*Day, DayOfWeek, Hour\*\* (for pattern analysis)

\- \*\*HasCustomerID\*\* (boolean flag)



\## Before vs After



| Metric | Before | After (Sales) |

|--------|--------|---------------|

| Rows | 541,909 | 530,104 |

| Revenue | Mixed | £10,666,684 |

| Date Format | Text | Datetime |

| Returns Separated | No | Yes (9,288) |



\## Files Created

1\. `ecommerce\_cleaned.csv` - All cleaned data

2\. `ecommerce\_sales.csv` - Sales only (for Power BI)

3\. `ecommerce\_returns.csv` - Returns analysis



\## Data Quality Score

\- ✅ No missing critical values

\- ✅ All dates valid

\- ✅ All prices positive

\- ✅ Revenue calculated

\- ✅ Returns separated



\*\*Ready for Power BI!\*\* 🚀

