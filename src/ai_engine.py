from src.predict import predict_sentiment
from src.risk import calculate_risk


def get_recommendation(level):

    if level == "CRITICAL":
        return [
            "🚨 Call Police immediately",
            "📍 Share Live Location",
            "📞 Contact trusted family member",
            "🏃 Move to a safe public place"
        ]

    elif level == "HIGH":
        return [
            "📍 Share Live Location",
            "📞 Inform trusted person",
            "🚔 Stay alert and seek help nearby"
        ]

    elif level == "MEDIUM":
        return [
            "⚠ Stay aware of surroundings",
            "📱 Keep your phone accessible"
        ]

    else:
        return [
            "✅ No immediate danger detected"
        ]


def analyze_tweet(tweet):

    sentiment = predict_sentiment(tweet)

    risk = calculate_risk(tweet)

    return {
        "tweet": tweet,
        "sentiment": sentiment,
        "risk_level": risk["risk"],
        "risk_score": risk["score"],
        "keywords": risk["keywords"],
        "recommendation": get_recommendation(risk["risk"])
    }