import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

data = pd.read_csv("sensor_data_big.csv")

x = data[["temperature", "vibration", "pressure"]]
y = data["failure"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(x_train, y_train)

predictions = model.predict(x_test)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
