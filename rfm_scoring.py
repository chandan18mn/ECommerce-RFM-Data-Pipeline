import pandas as pd
from sqlalchemy import create_engine

# 1. Connect to MySQL to grab your hard work
print("🔄 Step 1: Fetching clean data from MySQL...")
engine = create_engine("mysql+mysqlconnector://root:Admin123@localhost:3306/ecommerce_db")

# This is the exact query you just ran!
query = """
SELECT 
    CustomerID,
    DATEDIFF((SELECT MAX(InvoiceDate) FROM retail_clean), MAX(InvoiceDate)) AS Recency,
    COUNT(DISTINCT InvoiceNo) AS Frequency,
    ROUND(SUM(TotalAmount), 2) AS Monetary
FROM retail_clean
GROUP BY CustomerID;
"""
# Load the SQL data straight into a Python DataFrame
rfm_df = pd.read_sql(query, engine)

print("✅ Data fetched! Now scoring customers from 1 to 5...")

# 2. Assign Scores from 1 to 5 using Pandas 'qcut' (Quintiles)
# Recency: Lower days = Better (Score of 5)
rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], q=5, labels=[5, 4, 3, 2, 1])

# Frequency & Monetary: Higher numbers = Better (Score of 5)
# Note: We use rank(method='first') on Frequency to prevent errors from people who all have exactly 1 order
rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5])
rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'], q=5, labels=[1, 2, 3, 4, 5])

# 3. Combine scores into one master segment (e.g., '555' for Champions)
rfm_df['RFM_Segment'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str) + rfm_df['M_Score'].astype(str)

# 4. Export the final scored data to your Downloads folder
export_path = "C:/Users/CHANDAN M N/Downloads/archive (1)/Final_RFM_Scored.csv"
rfm_df.to_csv(export_path, index=False)

print(f"🚀 BOOM! Customers scored and saved successfully to: {export_path}") 