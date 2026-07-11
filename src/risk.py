HIGH_RISK = {
    "rape",
    "raped",
    "rapist",
    "molest",
    "molestation",
    "harassment",
    "harass",
    "attack",
    "assault",
    "abuse",
    "kidnap",
    "murder",
    "violence",
    "unsafe",
    "stalking",
    "follow",
    "following",
    "help",
    "danger",
    "threat"
}

MEDIUM_RISK = {
    "fear",
    "scared",
    "alone",
    "night",
    "dark",
    "road",
    "street",
    "panic"
}

from src.preprocessing import clean_tweet


def calculate_risk(tweet):

    tweet = clean_tweet(tweet)

    words = tweet.split()

    score = 0

    detected = []

    for word in words:

        if word in HIGH_RISK:
            score += 3
            detected.append(word)

        elif word in MEDIUM_RISK:
            score += 1
            detected.append(word)

    if score >= 6:
        level = "CRITICAL"

    elif score >= 3:
        level = "HIGH"

    elif score >= 1:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {
        "risk": level,
        "score": score,
        "keywords": detected
    }