import os
import pandas as pd
from catboost import datasets

titanic_data = datasets.titanic()

titanic_df = titanic_data[0]

current_dir = os.getcwd()

script_dir = '/home/kali/Desktop/MLOPS3/MLOPS-URFU-/lab4/'

file_path = os.path.join(script_dir, 'titanic.csv')

titanic_df.to_csv(file_path, index=False)

print(f"Датасет 'titanic.csv' успешно сохранен в {script_dir}.")
### Vtoraya chast' scripta
titanic_df = pd.read_csv('titanic.csv')

selected_features = ["PassengerId", "Pclass", "Sex", "Age"]
titanic_modified_df = titanic_df[selected_features]

print(titanic_modified_df.head())

titanic_modified_df.to_csv('titanic.csv', index=False)
