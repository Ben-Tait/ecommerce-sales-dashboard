import pandas as pd
import warnings
warnings.filterwarnings('ignore')

print("🧹 Starting data cleaning process...\n")

# Load data
df = pd.read_csv('data/raw/data.csv', encoding='ISO-8859-1')
print(f"Original data: {len(df):,} rows")

# 1. Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print("✅ Converted InvoiceDate to datetime")

# 2. Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']
print("✅ Created Revenue column")

# 3. Identify returns (invoices starting with 'C')
df['IsReturn'] = df['InvoiceNo'].astype(str).str.startswith('C')
print(f"✅ Identified {df['IsReturn'].sum():,} return transactions")

# 4. Remove rows with missing Description
df_clean = df[df['Description'].notna()].copy()
print(f"✅ Removed {len(df) - len(df_clean):,} rows with missing descriptions")

# 5. Remove rows with zero or negative prices (bad data)
df_clean = df_clean[df_clean['UnitPrice'] > 0].copy()
print(f"✅ Kept only positive prices: {len(df_clean):,} rows remain")

# 6. Extract date components for analysis
df_clean['Year'] = df_clean['InvoiceDate'].dt.year
df_clean['Month'] = df_clean['InvoiceDate'].dt.month
df_clean['MonthName'] = df_clean['InvoiceDate'].dt.strftime('%B')
df_clean['Day'] = df_clean['InvoiceDate'].dt.day
df_clean['DayOfWeek'] = df_clean['InvoiceDate'].dt.day_name()
df_clean['Hour'] = df_clean['InvoiceDate'].dt.hour
print("✅ Extracted date components")

# 7. Clean CustomerID (convert to integer where not null)
df_clean['CustomerID'] = df_clean['CustomerID'].fillna(0).astype(int)
df_clean['HasCustomerID'] = df_clean['CustomerID'] > 0
print("✅ Cleaned CustomerID column")

# 8. Create separate datasets
# Sales only (positive quantities, not returns)
df_sales = df_clean[(df_clean['Quantity'] > 0) & (~df_clean['IsReturn'])].copy()
print(f"✅ Sales dataset: {len(df_sales):,} rows")

# Returns only
df_returns = df_clean[df_clean['IsReturn']].copy()
print(f"✅ Returns dataset: {len(df_returns):,} rows")

# 9. Summary statistics
print("\n" + "="*60)
print("CLEANED DATA SUMMARY")
print("="*60)
print(f"Total Revenue: £{df_sales['Revenue'].sum():,.2f}")
print(f"Average Order Value: £{df_sales.groupby('InvoiceNo')['Revenue'].sum().mean():,.2f}")
print(f"Number of Orders: {df_sales['InvoiceNo'].nunique():,}")
print(f"Number of Customers: {df_sales[df_sales['HasCustomerID']]['CustomerID'].nunique():,}")
print(f"Date Range: {df_sales['InvoiceDate'].min()} to {df_sales['InvoiceDate'].max()}")

# 10. Save cleaned data
df_clean.to_csv('data/cleaned/ecommerce_cleaned.csv', index=False)
df_sales.to_csv('data/cleaned/ecommerce_sales.csv', index=False)
df_returns.to_csv('data/cleaned/ecommerce_returns.csv', index=False)

print("\n✅ Saved 3 files to data/cleaned/:")
print("   - ecommerce_cleaned.csv (all cleaned data)")
print("   - ecommerce_sales.csv (sales only)")
print("   - ecommerce_returns.csv (returns only)")

print("\n🎉 Data cleaning complete!")