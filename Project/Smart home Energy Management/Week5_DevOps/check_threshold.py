# Week 5 Threshold Check Script
import pandas as pd

df = pd.read_csv("energy_usage.csv")
alerts = df.groupby("device_id")['energy_kwh'].sum()
alerts = alerts[alerts > 10]

if not alerts.empty:
    print("ALERT: Devices exceeding 10 kWh/day:")
    print(alerts)
else:
    print("All devices under safe usage.")
