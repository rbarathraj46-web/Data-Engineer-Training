import pandas as pd
import numpy as np

# Load Data (simulate from CSV)
sales = pd.read_csv("sales.csv")
inventory = pd.read_csv("inventory.csv")

# Clean Missing Values
sales.fillna({"quantity_sold": 0, "total_amount": 0}, inplace=True)
inventory["stock_level"].fillna(inventory["stock_level"].mean(), inplace=True)

# Format Date Columns
sales["sale_date"] = pd.to_datetime(sales["sale_date"])

# Monthly Sales Summary
sales["month"] = sales["sale_date"].dt.to_period("M")
monthly_sales = sales.groupby("month")["total_amount"].sum().reset_index()

# Inventory Turnover
inventory_turnover = np.round(
    sales["quantity_sold"].sum() / inventory["stock_level"].sum(), 2
)

# Top & Low Performers
top_products = sales.groupby("product_id")["total_amount"].sum().sort_values(ascending=False).head(5)
underperforming = sales.groupby("product_id")["total_amount"].sum().sort_values().head(5)

# Export Reports
monthly_sales.to_csv("monthly_sales_report.csv", index=False)
top_products.to_csv("top_products.csv")
underperforming.to_csv("underperforming_products.csv")

print("Monthly sales summary, top performers, and underperformers exported successfully.")
