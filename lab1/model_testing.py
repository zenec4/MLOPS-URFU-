import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Загрузка модели
model = joblib.load("model.pkl")

# Загрузка тестовых данных
df_test = pd.read_csv("test/preprocessed_test_data.csv")

# Отделение целевой переменной
X_test = df_test.drop("KAST", axis=1)
y_test = df_test["KAST"]

# Предсказание на тестовых данных
y_pred = model.predict(X_test)

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error на тестовых данных: {mse}")

r2 = r2_score(y_test, y_pred)

print(f"Model test R²: {r2:.3f}")