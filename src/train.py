import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score, recall_score,f1_score
import pickle

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
y=df['Category'].values


x_train, x_test, y_train, y_test= train_test_split(X,y,train_size=0.8,random_state=30)
LR= LogisticRegression()

LR.fit(x_train,y_train)
y_pred=LR.predict(x_test)

print(f"Accuracy: {accuracy_score(y_test,y_pred):.2f}") 
print(f"Precision: {precision_score(y_test,y_pred):.2f}")
print(f"Recall: {recall_score(y_test,y_pred):.2f}")
print(f"F1: {f1_score(y_test,y_pred):.2f}")

pickle.dump(tfidf,open('../models/vectorizer.pkl','wb'))
pickle.dump(LR,open('../models/LogisticReg.pkl','wb'))





