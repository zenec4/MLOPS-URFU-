import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


df = pd.read_csv("train/preprocessed_train_data.csv")

X = df.drop("KAST", axis=1)
y = df["KAST"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)

print(f"Mean Squared Error на тренировочных данных: {mse}")

r2 = r2_score(y, y_pred)

print(f"Model train R²: {r2:.3f}")

joblib.dump(model, "model.pkl")

print("Модель успешно обучена и сохранена!")
