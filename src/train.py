import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df=pd.read_csv('../Data/email.csv')
#print(df.head())
df = df[df["Category"].isin(["ham", "spam"])]

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
df['Category']=encoder.fit_transform(df['Category'])
#print(df.head())

#check duplicates
#print(df.duplicated().sum()) # 415 values

df.drop_duplicates(keep='first',inplace=True)
#print(df.duplicated().sum())

df['transformed_text']=df['Message'].apply(preprocess.transform_text)

#vectorization
tfidf=TfidfVectorizer()
X=tfidf.fit_transform(df['transformed_text']).toarray()

print(X)





