# data/generate_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n = 1000
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(n)]
product_ids = np.random.randint(1, 10, size=n)
quantities = np.random.randint(1, 5, size=n)
prices = np.random.uniform(10, 200, size=n).round(2)
customer_ids = np.random.randint(1000, 1100, size=n)
regions = np.random.choice(["North", "South", "East", "West"], size=n)

df = pd.DataFrame({
    "date": dates,
    "product_id": product_ids,
    "quantity": quantities,
    "price": prices,
    "customer_id": customer_ids,
    "region": regions
})
df["revenue"] = df["quantity"] * df["price"]
df.to_csv("data/sales_data.csv", index=False)
print("Sample data saved to data/sales_data.csv")