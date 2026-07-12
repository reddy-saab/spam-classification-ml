# 📧 Spam Email Classifier

## 🔍 Overview
This project is a Machine Learning based Spam Email Classifier that predicts whether a given email or SMS message is **Spam** or **Ham (Not Spam)**. 

The model is built using **Logistic Regression** and **TF-IDF Vectorization**. A user-friendly web interface is created using **Streamlit** to allow users to enter messages and receive instant predictions. 🎈

## ✨ Features
- 🛡️ **Spam/Ham message classification**: Instantly classify messages.
- 🧹 **Text preprocessing and cleaning**: Converting to lowercase, tokenization, removing stopwords/punctuation, and stemming.
- 🤖 **Logistic Regression model**: Lightweight and efficient classifier.
- 💻 **Interactive Streamlit web application**: Modern, clean, and responsive UI.

## ⚙️ Model Workflow
1. 📥 **Load dataset**: Load raw email/SMS dataset.
2. 🧹 **Clean and preprocess text**: Standardize the text input.
3. 🔢 **Vectorize text**: Convert text into numerical features using TF-IDF.
4. ✂️ **Split data**: Divide the data into training and testing sets.
5. 🧠 **Train model**: Train the Logistic Regression Model.
6. 📊 **Evaluate performance**: Measure metrics like accuracy, precision, recall, and F1-score.
7. 💾 **Save artifacts**: Export the trained model and vectorizer.
8. 🚀 **Deploy**: Run the app locally using Streamlit.

## 🛠️ Tech Stack
- 🐍 **Python**
- 🐼 **Pandas**
- 🤖 **Scikit-learn**
- 🎈 **Streamlit**
- 📊 **Seaborn & Matplotlib**
- 🔤 **NLTK**
- 📦 **Pickle**

## 🚀 Run Locally

Follow these steps to run the application on your local machine:

1. **Clone the project:**
   ```bash
   git clone https://github.com/reddy-saab/spam-classification-ml.git
   cd spam-classification-ml
   ```

2. **Set up a Virtual Environment:**
   Creating a virtual environment helps keep the dependencies isolated and clean.
   
   - **Create the virtual environment:**
     ```bash
     python -m venv .venv
     ```
   
   - **Activate the virtual environment:**
     - **Windows (PowerShell):**
       ```powershell
       .venv\Scripts\Activate.ps1
       ```
     - **Windows (CMD):**
       ```cmd
       .venv\Scripts\activate.bat
       ```
     - **macOS/Linux:**
       ```bash
       source .venv/bin/activate
       ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

## 📊 Model Performance

| Metric | Score |
| :--- | :--- |
| 🎯 **Accuracy** | 98% |
| 🎯 **Precision** | 95% |
| 🎯 **Recall** | 86% |
| 🎯 **F1-Score** | 90% |
