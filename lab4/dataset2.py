import pandas as pd

titanic_df = pd.read_csv('titanic.csv')

mean_age = titanic_df['Age'].mean()

titanic_df['Age'].fillna(mean_age, inplace=True)

sex_encoded = pd.get_dummies(titanic_df['Sex'], prefix='Sex')

titanic_df = pd.concat([titanic_df, sex_encoded], axis=1)

titanic_df.to_csv('titanic.csv', index=False)

print(titanic_df.head())
