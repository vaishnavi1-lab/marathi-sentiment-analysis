import joblib

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def analyze_sentiment(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction[0]