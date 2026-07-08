import pickle
from .preprocess import transform_text

with open("models/LogisticReg.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

def Predict(text):
    cleaned_text=transform_text(text)
    vectorized_text=tfidf.transform([cleaned_text])
    prediction=model.predict(vectorized_text)
    return prediction

if __name__=='__main__':
    print(Predict("Congratulations, you won $100, click to claim")[0])

    
