import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Load the data
print("Loading data...")
df = pd.read_csv('data/raw/data.csv', encoding='ISO-8859-1')

print("\n" + "="*60)
print("DATASET OVERVIEW")
print("="*60)

# Basic info
print(f"\nTotal Rows: {len(df):,}")
print(f"Total Columns: {len(df.columns)}")
print(f"\nColumn Names:")
print(df.columns.tolist())

print("\n" + "="*60)
print("DATA TYPES & MISSING VALUES")
print("="*60)
print(df.info())

print("\n" + "="*60)
print("MISSING VALUES COUNT")
print("="*60)
print(df.isnull().sum())

print("\n" + "="*60)
print("FIRST 10 ROWS")
print("="*60)
print(df.head(10))

print("\n" + "="*60)
print("STATISTICAL SUMMARY")
print("="*60)
print(df.describe())

print("\n" + "="*60)
print("UNIQUE VALUES PER COLUMN")
print("="*60)
for col in df.columns:
    print(f"{col}: {df[col].nunique():,} unique values")

print("\n" + "="*60)
print("DATE RANGE")
print("="*60)
if 'InvoiceDate' in df.columns:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    print(f"From: {df['InvoiceDate'].min()}")
    print(f"To: {df['InvoiceDate'].max()}")

print("\n" + "="*60)
print("SAMPLE COUNTRIES")
print("="*60)
if 'Country' in df.columns:
    print(df['Country'].value_counts().head(10))

print("\n✅ Exploration complete!")