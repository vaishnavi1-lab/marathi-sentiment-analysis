
from predict import analyze_sentiment

texts = [
    "मला हा प्रोजेक्ट खूप छान वाटला",
    "हे पूर्णपणे चुकीचे आहे"
]

for text in texts:
    result = analyze_sentiment(text)
    print(f"Text: {text}")
    print("Sentiment:", result)
    print()