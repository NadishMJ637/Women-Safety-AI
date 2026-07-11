import streamlit as st
from src.history import load_history

st.title("📜 Prediction History")

history = load_history()

if history.empty:
    st.info("No predictions yet.")
else:
    st.dataframe(history, use_container_width=True)

    st.download_button(
        "⬇ Download CSV",
        history.to_csv(index=False),
        "prediction_history.csv",
        "text/csv"
    )