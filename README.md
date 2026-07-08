
# Spam Email Classifier

## Overview
This project is a Machine Learning based Spam Email Classifier that predicts whether a given email or SMS message is Spam or Ham(Not Spam) 

The model is built using **Logistic Regression** and **TF-IDF Vectorization**. A user friendly web interface is created using **Streamlit** to allow users to enter message and receive instant predictions.


## Features

- Spam/Ham message classification
- Text preprocessing and cleaning
- Logistic Regression model
- Interactive Streamlit web application


## Model Workflow
1. Load dataset
2. Clean and preprocess text
3. Convert text into numerical features using TF-IDF
4. Split data into training and testing sets
5. Train Logistic Regression Model
6. Evaluate model performance
7. Save trained model and vectorizer
8. Deploy using Streamlit
## Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Seaborn
- NLTK
- Pickle


## Run Locally

Clone the project:

```bash
  git clone https://github.com/reddy-saab/spam-classification-ml.git
```

Go to the project directory:

```bash
  cd spam-classification-ml
```

Install dependencies:

```bash
  pip install -r requirements.txt
```

Run the Streamlit application:

```bash
  streamlit run app.py
```

## Model Performance

| Metric         |       Score                                                              |
| ----------------- |    ------------------------------------------------------------------ |
| Accuracy | 98% |
| Precision | 95% |
| Recall | 86% |
| F-1 Score | 90% |
