import pandas as pd
import numpy as np

df = pd.read_csv("energy_usage.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['energy_kwh'] = pd.to_numeric(df['energy_kwh'], errors='coerce').fillna(0)

device_summary = df.groupby('device_id')['energy_kwh'].agg(['sum', 'mean'])
print("Device Summary:\n", device_summary)

room_summary = df.groupby('room_id')['energy_kwh'].sum()
print("\nRoom Summary:\n", room_summary)
