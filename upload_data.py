import pandas as pd
from sqlalchemy import create_engine

# 1. Define the exact file path using forward slashes to prevent Windows path errors
csv_file_path = "C:/Users/CHANDAN M N/Downloads/archive (1)/online_retail.csv"

print("🔄 Step 1: Reading the 500,000+ rows from your CSV file...")
# We use ISO-8859-1 encoding because this UK dataset contains currency symbols like £
df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")
print("✅ CSV loaded into Python successfully!")

# 2. Set up the direct connection to your MySQL database using your password
print("\n🔄 Step 2: Connecting to your MySQL local instance...")
engine = create_engine("mysql+mysqlconnector://root:Admin123@localhost:3306/ecommerce_db")

# 3. Stream the entire dataset straight into your database all at once
print("\n🔄 Step 3: Pushing data to MySQL (This will take roughly 30-45 seconds)...")
df.to_sql(name="online_retail", con=engine, if_exists="replace", index=False)

print("\n🚀 BOOM! Data pipeline complete! All rows successfully uploaded to MySQL.")