import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("sensor_data_big.csv")

x = data[["temperature", "vibration", "pressure"]]
y = data["failure"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

predictions = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, predictions))