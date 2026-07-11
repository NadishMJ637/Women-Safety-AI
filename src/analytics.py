import pandas as pd

# Load dataset once
df = pd.read_csv("data/twitter_labeled.csv")


def get_sentiment_counts():
    return df["Sentiment"].value_counts()


def get_source_counts():
    return df["source"].value_counts().head(10)


def get_tweet_lengths():
    return df["lens"]


def get_likes():
    return df["likes"]


def get_retweets():
    return df["retweets"]