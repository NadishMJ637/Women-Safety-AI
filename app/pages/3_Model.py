import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Model Performance", page_icon="📈", layout="wide")

with open("app/assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_svg(name: str) -> str:
    path = Path("app/assets/illustrations") / name
    return path.read_text() if path.exists() else ""


st.markdown(
    f"""
    <div class="hero-banner">
        <div class="hero-art">{load_svg('model.svg')}</div>
        <div class="hero-text">
            <div class="eyebrow">Section · Model</div>
            <h1>📈 Machine Learning Model Performance</h1>
            <p>How each candidate model compares on accuracy, training time, and prediction speed.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------
# Model Data
# -------------------------

models = pd.DataFrame({

    "Model":[
        "Naive Bayes",
        "Logistic Regression",
        "Linear SVM",
        "Random Forest"
    ],

    "Accuracy":[
        95.23,
        96.42,
        97.40,
        97.07
    ],

    "Training Time":[
        0.05,
        0.516,
        0.081,
        0.747
    ],

    "Prediction Time":[
        0.001,
        0.001,
        0.001,
        0.003
    ]
})

# -------------------------
# Best Model Card
# -------------------------

st.success("🏆 Best Model : Linear SVM (97.40%)")

st.divider()

# -------------------------
# Charts
# -------------------------

col1,col2 = st.columns(2)

with col1:

    fig = px.bar(
        models,
        x="Model",
        y="Accuracy",
        text="Accuracy",
        title="Accuracy Comparison",
        color_discrete_sequence=["#0F9B8E"]
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.bar(
        models,
        x="Model",
        y="Training Time",
        text="Training Time",
        title="Training Time Comparison",
        color_discrete_sequence=["#B8802B"]
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Prediction Time
# -------------------------

fig = px.bar(
    models,
    x="Model",
    y="Prediction Time",
    text="Prediction Time",
    title="Prediction Time Comparison",
    color_discrete_sequence=["#1E2340"]
)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Table
# -------------------------

st.subheader("📋 Complete Comparison")

st.dataframe(
    models,
    use_container_width=True
)