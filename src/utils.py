"""
Utility Functions
"""

from src.constants import *


def get_sentiment_icon(sentiment):

    icons = {

        POSITIVE: "😊",

        NEGATIVE: "😡",

        NEUTRAL: "😐"

    }

    return icons.get(sentiment, "❓")


def get_risk_icon(level):

    icons = {

        LOW: "🟢",

        MEDIUM: "🟡",

        HIGH: "🟠",

        CRITICAL: "🔴"

    }

    return icons.get(level, "⚪")