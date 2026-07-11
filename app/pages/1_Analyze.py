import streamlit as st
import plotly.graph_objects as go
from pathlib import Path

from src.report_generator import generate_report
from src.ai_engine import analyze_tweet
from src.history import save_prediction

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Safety Assessment",
    page_icon="🚨",
    layout="wide"
)

with open("app/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_svg(name: str) -> str:
    path = Path("app/assets/illustrations") / name
    return path.read_text() if path.exists() else ""


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    f"""
    <div class="hero-banner">
        <div class="hero-art">{load_svg('analyze.svg')}</div>
        <div class="hero-text">
            <div class="eyebrow">Section · Analyze</div>
            <h1>🚨 AI Safety Assessment</h1>
            <p>Analyze text using AI to identify potential women safety risks and receive safety recommendations.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Input
# --------------------------------------------------

tweet = st.text_area(
    "📝 Enter Text",
    placeholder="Example: Someone is following me near the bus stand. I feel unsafe.",
    height=180
)

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("🔍 Analyze Text", use_container_width=True):

    if tweet.strip() == "":
        st.warning("Please enter some text.")
        st.stop()

    # -----------------------------
    # AI Prediction
    # -----------------------------

    result = analyze_tweet(tweet)

    # -----------------------------
    # Save Prediction
    # -----------------------------

    save_prediction(tweet, result)

    st.markdown("---")

    # ==================================================
    # Sentiment & Risk Cards
    # ==================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("😊 Sentiment")

        sentiment = result["sentiment"]

        if sentiment == "Positive":
            st.success("😊 POSITIVE")

        elif sentiment == "Neutral":
            st.warning("😐 NEUTRAL")

        else:
            st.error("😡 NEGATIVE")

    with col2:

        st.subheader("🚨 Risk Level")

        risk = result["risk_level"]

        if risk == "LOW":
            st.success("🟢 LOW")

        elif risk == "MEDIUM":
            st.warning("🟡 MEDIUM")

        elif risk == "HIGH":
            st.error("🟠 HIGH")

        else:
            st.error("🔴 CRITICAL")

    # ==================================================
    # Risk Gauge
    # ==================================================

    st.markdown("---")

    st.subheader("📊 Women Safety Risk Score")

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=result["risk_score"],

        number={
            "font": {"size": 40}
        },

        title={
            "text": "Risk Score",
            "font": {"size": 24}
        },

        gauge={

            "axis": {"range": [0, 10]},

            "bar": {"color": "#1E2340"},

            "steps": [

                {"range": [0, 3], "color": "#0F9B8E"},

                {"range": [3, 6], "color": "#B8802B"},

                {"range": [6, 8], "color": "#E08A47"},

                {"range": [8, 10], "color": "#B8433D"}

            ]

        }

    ))

    st.plotly_chart(fig, use_container_width=True)

    # ==================================================
    # Keywords
    # ==================================================

    st.markdown("---")

    st.subheader("🏷 Detected Keywords")

    keywords = result.get("keywords", [])

    if keywords:

        cols = st.columns(4)

        for i, word in enumerate(keywords):

            cols[i % 4].markdown(
                f"""
                <div style="
                    background:#0F9B8E;
                    color:white;
                    padding:10px;
                    border-radius:12px;
                    text-align:center;
                    font-weight:bold;
                    margin-bottom:10px;
                ">
                {word}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.success("No important keywords detected.")

    # ==================================================
    # Recommendations
    # ==================================================

    st.markdown("---")

    st.subheader("💡 AI Safety Recommendations")

    recommendations = result.get("recommendation", [])

    if recommendations:

        for index, rec in enumerate(recommendations, start=1):
            st.info(f"**{index}.** {rec}")

    else:

        st.success("No recommendations available.")

    report_path = generate_report(tweet, result)

    with open(report_path, "rb") as pdf:

    	st.download_button(
        	label="📄 Download AI Report",
        	data=pdf,
        	file_name=report_path.name,
        	mime="application/pdf"
    	)

    # ==================================================
    # Summary
    # ==================================================

    st.markdown("---")

    st.subheader("📋 Analysis Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:

        st.metric("Sentiment", result["sentiment"])

        st.metric("Risk Level", result["risk_level"])

    with summary_col2:

        st.metric("Risk Score", f"{result['risk_score']}/10")

        st.metric("Keywords", len(keywords))

    # ==================================================
    # Expandable Raw Output
    # ==================================================

    st.markdown("---")

    with st.expander("🔍 View Complete AI Output"):

        st.json(result)