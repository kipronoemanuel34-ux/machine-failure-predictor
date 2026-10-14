import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score

data = pd.read_csv("sensor_data_big.csv")

x = data[["temperature", "vibration", "pressure"]]
y = data["failure"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

for depth in [1, 2, 3, 5, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(x_train, y_train)
    train_acc = model.score(x_train, y_train)
    test_acc = model.score(x_test, y_test)
    cv_acc = cross_val_score(model, x, y, cv=5).mean()
    print("depth", depth, "| train:", round (train_acc, 2), "| test:", round(test_acc, 2), "|cross-val:", round(cv_acc, 2))
    # depth None means no limit on depth of tree. The model will keep splitting until it perfectly classifies the training data. This can lead to overfitting, where the model performs well on training data but poorly on unseen test data.