import pandas as pd
import numpy as np

np.random.seed(42)

# Number of rows
n = 2000

# Sample product names
products = [
    "Shampoo", "Conditioner", "Face Cream", "Body Lotion", "Hair Oil",
    "Handwash", "Serum", "Face Wash", "Lip Balm", "Sunscreen",
    "Toner", "Moisturizer", "Cleanser", "Hair Mask", "Night Cream"
]

# Create dataset
df = pd.DataFrame({
    "product_id": np.arange(1, n+1),
    "product_name": np.random.choice(products, n),
    "category": "Beauty",
    "stock_level": np.random.randint(10, 500, n),
    "avg_daily_sales": np.round(np.random.uniform(0.5, 20, n), 2),
    "unit_price": np.round(np.random.uniform(5, 50, n), 2)
})

# Calculate days remaining
df["days_remaining"] = df["stock_level"] / df["avg_daily_sales"]

# Slow-moving flag
df["slow_moving"] = df["days_remaining"] > 60

# Reorder flag (less than 14 days of stock)
df["reorder_flag"] = df["stock_level"] < (df["avg_daily_sales"] * 14)

df.head()
print(df.head())
print(df.info())
print(df.describe())
print(df["slow_moving"].value_counts())
print(df["reorder_flag"].value_counts())
print(df.groupby("product_name")["slow_moving"].mean())
print(df[df["slow_moving"]].head(10))
print(df[df["reorder_flag"]].head(10))
