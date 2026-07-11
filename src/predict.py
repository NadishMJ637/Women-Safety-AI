from pathlib import Path
import joblib

from src.preprocessing import clean_tweet

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

model = joblib.load(MODEL_DIR / "svm_model.pkl")
vectorizer = joblib.load(MODEL_DIR / "tfidf_vectorizer.pkl")


def predict_sentiment(tweet):
    cleaned = clean_tweet(tweet)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return prediction