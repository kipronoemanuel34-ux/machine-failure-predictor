import pandas as pd 

data = pd.read_csv("sensor_data.csv")

failed = data[data["failure"] == 1]

print(failed["temperature"].mean())  # 91.3333
print(failed["vibration"].mean())  #5.8

not_failed = data[data["failure"] == 0]

print(not_failed["temperature"].mean()) #72.0
print(not_failed["vibration"].mean()) #2.38

#machines that failed had higher average temperature and vibration readings compared to machines that did not fail. This suggests that higher temperature and vibration may be indicators of potential machine failure.