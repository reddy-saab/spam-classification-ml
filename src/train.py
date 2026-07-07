import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('../Data/email.csv')
#print(df.head())
df = df[df["Category"].isin(["ham", "spam"])]

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
df['Category']=encoder.fit_transform(df['Category'])
#print(df.head())

#check duplicates
print(df.duplicated().sum()) # 415 values

df.drop_duplicates(keep='first',inplace=True)
print(df.duplicated().sum())



