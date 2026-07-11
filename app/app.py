import streamlit as st
from pathlib import Path
from src.config import *

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load CSS
# -----------------------------
with open("app/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_svg(name: str) -> str:
    """Read a cartoon illustration from app/assets/illustrations/."""
    path = Path("app/assets/illustrations") / name
    return path.read_text() if path.exists() else ""


# -----------------------------
# Hero Section
# -----------------------------

st.markdown(
    f"""
    <div class="hero-banner">
        <div class="hero-art">{load_svg('hero.svg')}</div>
        <div class="hero-text">
            <div class="eyebrow">AI-Powered Protection</div>
            <h1>🛡 {APP_NAME}</h1>
            <p>
                Analyze women-safety-related text using <b>Natural Language Processing</b> and
                <b>Machine Learning</b> — predicting sentiment, evaluating risk, and offering
                actionable safety recommendations, in real time.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📊 Dataset", f"{DATASET_SIZE:,} Tweets")

with col2:
    st.metric("🧠 Best Model", MODEL_NAME)

with col3:
    st.metric("🎯 Accuracy", f"{MODEL_ACCURACY}%")

with col4:
    st.metric("🚨 Risk Engine", "🟢 Active")

st.divider()

# -----------------------------
# Workflow
# -----------------------------

st.subheader("⚙️ AI Workflow")

workflow_cols = st.columns(6)

steps = [
    "📝\nTweet",
    "🧹\nClean",
    "🔤\nTF-IDF",
    "🤖\nLinear SVM",
    "🚨\nRisk",
    "💡\nRecommendation"
]

for col, step in zip(workflow_cols, steps):
    with col:
        st.markdown(
            f"""
<div style="text-align:center;
padding:16px 10px;
background:var(--card);
border:1px solid var(--line);
border-radius:14px;
font-weight:600;
color:var(--ink);
transition:all .2s ease;">
{step}
</div>
""",
            unsafe_allow_html=True
        )

st.divider()

# -----------------------------
# Features
# -----------------------------

st.subheader("✨ Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
### 🤖 Sentiment Analysis

- Positive
- Neutral
- Negative
""")

with c2:
    st.warning("""
### 🚨 Risk Detection

- Low
- Medium
- High
- Critical
""")

with c3:
    st.success("""
### 💡 Smart Recommendations

- Emergency Guidance
- Keyword Detection
- Risk Assessment
""")

st.divider()

st.caption(
    f"{APP_NAME} v{APP_VERSION} • Developed by {DEVELOPER}"
)