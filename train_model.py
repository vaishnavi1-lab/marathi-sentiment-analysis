import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
data = pd.read_csv("data.csv")

X = data["text"]
y = data["label"]

# Convert text to vectors
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Save model
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully!")