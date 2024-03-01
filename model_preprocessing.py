import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


paths_input = ["train/train_data.csv", "test/test_data.csv"]
paths_output = ["train/preprocessed_train_data.csv", "test/preprocessed_test_data.csv"]


def preprocessing_data(path_input: str, path_output: str)-> None:
    data = pd.read_csv(path_input)

    column_names = data.columns

    non_numeric_cols = data.select_dtypes(include=['object']).columns

    column_names = list(filter(lambda name: name not in non_numeric_cols, column_names))

    data = data.drop(non_numeric_cols, axis=1)

    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    np.savetxt(path_output, data, delimiter=',', header=','.join(column_names))

for i in range(len(paths_input)):
    preprocessing_data(paths_input[i], paths_output[i])

print("Данные успешно предобработаны!")
