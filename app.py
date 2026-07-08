import streamlit as st
from src import predict

st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

st.title("Email Spam Classifier")

input = st.text_area(
    "Enter your message",
    placeholder="Type or paste your email here..."
)

if(st.button('Predict')):

  prediction=predict.Predict(input)

  if(prediction[0]==1):
    st.error("Spam")
  else:
    st.success("Not spam")

with st.sidebar:
    st.header("About")
    st.write("**Model:** Logistic Regression")
    st.write("**Vectorizer:** TF-IDF")
     
    st.divider()
    
    st.header("📊 Test Performance")
    st.write("**Precision:** 95%")
    st.write("**Recall:** 86%")

