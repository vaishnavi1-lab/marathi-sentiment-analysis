# 🇮🇳 Marathi Sentiment Analysis using Machine Learning

## 📌 Project Overview

This project is a Marathi Language Sentiment Analysis System built using Machine Learning.  
It classifies Marathi text into:

- ✅ Positive  
- ❌ Negative  
- ➖ Neutral  

The project demonstrates practical implementation of Natural Language Processing (NLP) techniques.

---

## 🎯 Objectives

- Perform text preprocessing on Marathi data  
- Convert text into numerical features using TF-IDF  
- Train a Machine Learning classification model  
- Predict sentiment for new user input  
- Save trained model for future use  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle  
- NLP Techniques  

---

## 📂 Project Structure


marathi_sentiment_ml/
│
├── data.csv
├── train_model.py
├── predict.py
├── test.py
├── sentiment_model.pkl
├── vectorizer.pkl
├── setup.py
├── requirements.txt
└── README.md


---

## ⚙️ How the System Works

### 1️⃣ Data Loading
Dataset containing Marathi sentences is loaded using Pandas.

### 2️⃣ Text Preprocessing
- Lowercasing  
- Removing special characters  
- Cleaning unwanted symbols  

### 3️⃣ Feature Extraction
Text is converted into numerical vectors using **TF-IDF Vectorizer**.

### 4️⃣ Model Training
A Machine Learning classifier is trained using labeled data.

### 5️⃣ Model Saving
The trained model and vectorizer are saved using Pickle.

### 6️⃣ Prediction
New Marathi text input is passed to the model to predict sentiment.

---

## ▶️ How to Run the Project

### 🔹 Step 1: Clone Repository


git clone https://github.com/your-username/marathi-sentiment-analysis.git

cd marathi-sentiment-analysis


### 🔹 Step 2: Create Virtual Environment (Optional)


python -m venv venv
venv\Scripts\activate


### 🔹 Step 3: Install Dependencies


pip install -r requirements.txt


If requirements.txt is not available:


pip install pandas numpy scikit-learn


### 🔹 Step 4: Train the Model


python train_model.py


### 🔹 Step 5: Run Prediction


python test.py


OR


python predict.py


---

## 🧪 Example Usage

```python
from predict import analyze_sentiment

result = analyze_sentiment("मला हा प्रोजेक्ट खूप छान वाटला")
print("Sentiment:", result)
Sample Output
Input Text	Prediction
मला हा प्रोजेक्ट खूप छान वाटला	Positive
हे पूर्णपणे चुकीचे आहे	Negative
