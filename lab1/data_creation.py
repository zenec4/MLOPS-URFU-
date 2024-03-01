import pandas as pd
from sklearn.model_selection import train_test_split
import os

os.environ['KAGGLE_USERNAME'] = "dlyamlops"
os.environ['KAGGLE_KEY'] = "cd1a44ff3116161a8ca94e1ab133af14"  #В данном случае мы использовали токен, сгенерированный на аккаунт временной электронной почты 


import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi



datasetname = 'yuvalbogachev/csgo-player-ranking-dataset'
folder_path = 'full_dataset'
train_csv_path = 'train/train_data.csv'
test_csv_path = 'test/test_data.csv'
dirs = ["train", "test"]
cols_to_drop = ["Kill/Death Ratio", "Damage Per Round", "Kills Per Round", "Deaths Per Round", "Rating 2.0"]


def create_dir(name: str)-> None:
    if not os.path.exists(name):
        os.makedirs(name)


def load_data()-> tuple[pd.DataFrame, pd.DataFrame]:
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(datasetname, folder_path, unzip=True)
    data = pd.read_csv(folder_path + "/" +os.listdir(folder_path)[0])
    data.columns = list(map(lambda x: x.strip(), data.columns))
    data = data.drop(cols_to_drop, axis=1)
    return train_test_split(data, test_size=0.2, random_state=42)


train_data, test_data = load_data()


for dir in dirs:
    create_dir(dir)



train_data.to_csv(train_csv_path, index=False)
test_data.to_csv(test_csv_path, index=False)

