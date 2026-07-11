import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

with open("app/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_svg(name: str) -> str:
    path = Path("app/assets/illustrations") / name
    return path.read_text() if path.exists() else ""


st.markdown(
    f"""
    <div class="hero-banner">
        <div class="hero-art">{load_svg('about.svg')}</div>
        <div class="hero-text">
            <div class="eyebrow">Section · About</div>
            <h1>ℹ️ About Women Safety AI</h1>
            <p>An AI-powered web application developed to analyze tweets related to women safety.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
## 🛡 Project Overview

Women Safety AI is an AI-powered web application developed to analyze tweets related to women safety.

The system applies **Natural Language Processing (NLP)** and **Machine Learning** to:

- Detect tweet sentiment
- Identify potential safety risks
- Detect dangerous keywords
- Recommend appropriate safety actions
""")

st.divider()

st.subheader("🎯 Objectives")

st.markdown("""
- Improve awareness of women safety issues
- Analyze social media discussions
- Detect high-risk situations
- Provide quick recommendations
""")

st.divider()

st.subheader("⚙️ Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.success("🐍 Python")
    st.success("🤖 Scikit-learn")
    st.success("📊 Pandas")
    st.success("🧠 NLP")

with col2:
    st.info("🌐 Streamlit")
    st.info("📈 Plotly")
    st.info("🔤 TF-IDF")
    st.info("💻 Linear SVM")

st.divider()

st.subheader("🧠 AI Workflow")

st.code("""
User Input
     │
     ▼
Text Preprocessing
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Linear SVM Model
     │
     ▼
Risk Detection
     │
     ▼
Safety Recommendation
""")

st.divider()

st.subheader("📈 Model Performance")

st.metric("Best Model", "Linear SVM")
st.metric("Accuracy", "97.40%")

st.divider()

st.subheader("👨‍💻 Developer")

st.write("**Name:** Nadish M J")
st.write("**Department:** Artificial Intelligence and Data Science")
st.write("**Project:** Women Safety AI using NLP")