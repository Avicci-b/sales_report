# api/server.py
from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

app = FastAPI(title="Sales Analysis API", version="1.0.0")

# Load analysis results once at startup (for a demo; in production you’d use caching/DB)
results_dir = Path("./analysis/results")

with open(results_dir / "summary.json") as f:
    summary = json.load(f)

with open(results_dir / "monthly_sales.json") as f:
    monthly_sales = json.load(f)

with open(results_dir / "segment_counts.json") as f:
    segment_counts = json.load(f)

with open(results_dir / "customer_details.json") as f:
    customer_details = json.load(f)

@app.get("/")
def root():
    return {"message": "Sales Analysis API. Visit /docs for Swagger UI."}

@app.get("/summary")
def get_summary():
    return summary

@app.get("/monthly-sales")
def get_monthly_sales():
    return monthly_sales

@app.get("/segments")
def get_segment_counts():
    return segment_counts

@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    cust = customer_details.get(str(customer_id))   # JSON keys are strings
    if cust is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return cust