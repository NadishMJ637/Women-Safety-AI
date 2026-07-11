import re
import string
import ast

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def decode_tweet(tweet):
    """
    Decode byte-string tweets.
    """

    try:
        if isinstance(tweet, str) and tweet.startswith("b'"):
            return ast.literal_eval(tweet).decode(
                "utf-8",
                errors="ignore"
            )
        return tweet
    except:
        return tweet


def clean_tweet(text):
    """
    Complete preprocessing pipeline.
    """

    if text is None:
        return ""

    text = decode_tweet(text)

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"\brt\b", "", text)

    text = re.sub(r"@\w+", "", text)

    text = re.sub(r"#", "", text)

    text = re.sub(
        r"[\u200b-\u200f\u202a-\u202e\u2066-\u2069]",
        "",
        text
    )

    text = text.replace("…", " ")

    text = re.sub(r"\d+", "", text)

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    text = re.sub(r"\s+", " ", text).strip()

    words = []

    for word in text.split():

        if word not in stop_words and len(word) > 2:
            words.append(
                lemmatizer.lemmatize(word)
            )

    return " ".join(words)