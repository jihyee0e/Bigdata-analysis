import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
titanic.to_csv('./titanic.csv', index=False)

titanic.isnull().sum()  #결측값 확인