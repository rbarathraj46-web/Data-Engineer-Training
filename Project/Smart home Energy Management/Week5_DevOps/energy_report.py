# Week 5 Report Script
import pandas as pd

df = pd.read_csv("energy_usage.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

summary = df.groupby(df['timestamp'].dt.date)['energy_kwh'].sum()
summary.to_csv("reports/daily_report.csv")

print("Report generated successfully.")
