\# Data Exploration Report



\*\*Date:\*\* January 15, 2026  

\*\*Dataset:\*\* E-Commerce Transactions (UK Retailer)



\## Dataset Overview

\- \*\*Total Transactions:\*\* 541,909

\- \*\*Time Period:\*\* December 2010 - December 2011 (1 year)

\- \*\*Columns:\*\* 8

\- \*\*Products:\*\* 4,070 unique items

\- \*\*Customers:\*\* 4,372 unique IDs

\- \*\*Countries:\*\* 38



\## Column Structure

| Column | Type | Description |

|--------|------|-------------|

| InvoiceNo | Text | Unique invoice number (starts with 'C' for cancellations) |

| StockCode | Text | Product code |

| Description | Text | Product name/description |

| Quantity | Integer | Number of items purchased |

| InvoiceDate | Text | Transaction timestamp |

| UnitPrice | Float | Price per item (GBP) |

| CustomerID | Float | Unique customer identifier |

| Country | Text | Customer country |



\## Data Quality Issues Found



\### 1. Missing Values

\- \*\*CustomerID:\*\* 135,080 missing (24.9%)

&nbsp; - Likely guest purchases or data entry issues

&nbsp; - Decision: Keep for sales analysis, exclude for customer analysis

&nbsp; 

\- \*\*Description:\*\* 1,454 missing (0.27%)

&nbsp; - Decision: Keep rows, label as "Unknown Product"



\### 2. Negative Values (Returns/Cancellations)

\- \*\*Quantity:\*\* Min = -80,995

\- \*\*UnitPrice:\*\* Min = -$11,062

\- Invoices starting with 'C' indicate cancellations

\- \*\*Decision:\*\* Separate analysis for returns vs. sales



\### 3. Extreme Values (Potential Outliers)

\- Max Quantity: 80,995 (needs investigation)

\- Max Price: $38,970 (luxury item or error?)

\- \*\*Decision:\*\* Investigate top 10 transactions



\### 4. Data Type Issues

\- InvoiceDate stored as text, needs conversion to datetime

\- CustomerID stored as float (should be integer/text)



\## Geographic Distribution

\- \*\*United Kingdom:\*\* 91.4% of transactions (495,478)

\- \*\*Germany:\*\* 1.8% (9,495)

\- \*\*France:\*\* 1.6% (8,557)

\- \*\*Other 35 countries:\*\* 5.2%



\## Next Steps

1\. Clean data (handle nulls, negatives, dates)

2\. Create separate datasets: Sales vs Returns

3\. Calculate revenue (Quantity × UnitPrice)

4\. Identify and handle outliers

5\. Build Power BI dashboard



\## Key Metrics to Track

\- Total Revenue

\- Number of Orders

\- Average Order Value

\- Return Rate

\- Top Products by Revenue

\- Monthly Sales Trends

\- Customer Lifetime Value

