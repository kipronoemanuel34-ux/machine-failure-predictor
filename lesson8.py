import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("sensor_data.csv")

x = data[["temperature", "vibration", "pressure"]]
y = data["failure"]

model = DecisionTreeClassifier()
model.fit(x, y)

new_machine = pd.DataFrame({"temperature": [86], "vibration": [4.5], "pressure": [105]})

print(model.predict(new_machine))  