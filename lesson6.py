import pandas as pd

data = pd.read_csv("sensor_data.csv")
print(data)
print(data["temperature"].mean())
print(data["vibration"].max())
print(data["failure"].sum())