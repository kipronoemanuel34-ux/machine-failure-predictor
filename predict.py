import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("sensor_data_big.csv")

x = data[["temperature", "vibration", "pressure"]]
y = data["failure"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, max_depth=5, class_weight="balanced", random_state=42)
model.fit(x_train, y_train)

print(classification_report(y_test, model.predict(x_test)))

def check_machine(temperature, vibration, pressure):
    reading = pd.DataFrame({
        "temperature": [temperature],
        "vibration": [vibration],
        "pressure": [pressure]
    })
    probability = model.predict_proba(reading)[0][1]
    if probability >= 0.5:
        status = "WARNING"
    else:
        status = "Normal"
    return status, round(probability, 2)

print(check_machine(66, 1.8, 99))
print(check_machine(90, 5.5, 106))
print(check_machine(80, 3.5, 103))