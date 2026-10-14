import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

data = pd.read_csv("sensor_data_big.csv")

x = data[["temperature", "vibration", "pressure"]]
y = data["failure"]

models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=3, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42),
    "Forest (balanced)": RandomForestClassifier(n_estimators=100, max_depth=5, class_weight="balanced", random_state=42),
}

names = []
recalls = [] 
for name, model in models.items():
    score = cross_val_score(model, x, y, cv=5, scoring="recall").mean()
    names.append(name)
    recalls.append(score)
    print(name, "recall:", round(score, 2))
plt.bar(names, recalls)
plt.ylabel("recall (failures caught)")
plt.title("Which model catches the most failures?")
plt.ylim(0, 1)
plt.show()