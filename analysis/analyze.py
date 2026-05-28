# analysis/analyze.py
import pandas as pd
import json
from pathlib import Path

# Load data
df = pd.read_csv("./data/sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

# 1. Overall summary
summary = {
    "total_revenue": round(df["revenue"].sum(), 2),
    "total_orders": len(df),
    "average_order_value": round(df["revenue"].mean(), 2)
}

# 2. Monthly sales
monthly = df.groupby("month")["revenue"].sum().reset_index()
monthly["month"] = monthly["month"].astype(str)   # convert Period to string for JSON
monthly_sales = monthly.to_dict(orient="records")

# 3. Customer segmentation
customer_spend = df.groupby("customer_id")["revenue"].sum().reset_index()

def segment(spend):
    if spend > 1000:
        return "high"
    elif spend > 500:
        return "medium"
    else:
        return "low"

customer_spend["segment"] = customer_spend["revenue"].apply(segment)
segment_counts = customer_spend["segment"].value_counts().to_dict()

# Per‑customer detail (for the /customer/{id} endpoint)
customer_detail = {}
for _, row in customer_spend.iterrows():
    customer_detail[int(row["customer_id"])] = {
        "total_spent": round(row["revenue"], 2),
        "segment": row["segment"]
    }

# Save everything to JSON files
out_dir = Path("analysis/results")
out_dir.mkdir(exist_ok=True)

with open(out_dir / "summary.json", "w") as f:
    json.dump(summary, f, indent=2)

with open(out_dir / "monthly_sales.json", "w") as f:
    json.dump(monthly_sales, f, indent=2)

with open(out_dir / "segment_counts.json", "w") as f:
    json.dump(segment_counts, f, indent=2)

with open(out_dir / "customer_details.json", "w") as f:
    json.dump(customer_detail, f, indent=2)

print("Analysis complete. Results saved to analysis/results/")