import streamlit as st
import plotly.express as px
from pathlib import Path

from src.analytics import *

st.set_page_config(page_title="Analytics Dashboard", page_icon="📊", layout="wide")

with open("app/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_svg(name: str) -> str:
    path = Path("app/assets/illustrations") / name
    return path.read_text() if path.exists() else ""


st.markdown(
    f"""
    <div class="hero-banner">
        <div class="hero-art">{load_svg('analytics.svg')}</div>
        <div class="hero-text">
            <div class="eyebrow">Section · Analytics</div>
            <h1>📊 Analytics Dashboard</h1>
            <p>A look at sentiment trends, tweet length, and top sources across everything analyzed so far.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

CHART_COLORS = ["#0F9B8E", "#B8802B", "#1E2340", "#B8433D", "#565C7C"]

# Sentiment Pie Chart
sentiment = get_sentiment_counts()

fig = px.pie(
    values=sentiment.values,
    names=sentiment.index,
    title="Sentiment Distribution",
    color_discrete_sequence=CHART_COLORS,
    hole=0.45
)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

# Tweet Length
lengths = get_tweet_lengths()

fig = px.histogram(
    x=lengths,
    title="Tweet Length Distribution",
    color_discrete_sequence=["#0F9B8E"]
)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

# Source Distribution
sources = get_source_counts()

fig = px.bar(
    x=sources.index,
    y=sources.values,
    title="Top Tweet Sources",
    color_discrete_sequence=["#1E2340"]
)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)