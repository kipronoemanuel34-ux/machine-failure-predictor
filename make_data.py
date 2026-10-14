import numpy as np
import pandas as pd 

np.random.seed(42)
n = 300

temperature = np.random.normal(78, 10, n).round(1)
vibration = np.random.normal(3, 1.2, n).round(2)
pressure = np.random.normal(103, 4, n).round(1)

risk = (temperature - 78) / 10 + (vibration - 3) / 1.2 + np.random.normal(0, 0.7, n)
failure = (risk > 1).astype(int)

data = pd.DataFrame({"temperature": temperature, "vibration": vibration, "pressure": pressure, "failure": failure})
data.to_csv("sensor_data_big.csv", index=False)
print(data["failure"].value_counts())