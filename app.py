import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="IPL 2026 - Batsman Form Predictor",
    page_icon="🏏",
    layout="wide"
)

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    with open("best_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ================= TITLE =================
st.markdown(
    "<h1 style='text-align:center; color:#FF4B4B;'>🏏 IPL 2026 - Batsman Form Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Predict whether a batsman is in form using Machine Learning</p>",
    unsafe_allow_html=True
)

st.divider()

# ================= LAYOUT =================
col1, col2 = st.columns(2)

# ================= INPUT SECTION =================
with col1:
    st.subheader("📊 Enter Player Stats")

    player_name = st.text_input("Player Name")

    runs = st.number_input("Total Runs", min_value=0, value=300)
    balls = st.number_input("Balls Faced", min_value=1, value=200)
    strike_rate = st.number_input("Strike Rate", min_value=0.0, value=140.0)

    predict_btn = st.button("🚀 Predict Form", use_container_width=True)

# ================= OUTPUT SECTION =================
with col2:
    st.subheader("📈 Prediction Result")

    if predict_btn:

        input_data = np.array([[strike_rate, runs, balls]])

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.success("🔥 Player is IN FORM")
        else:
            st.error("❌ Player is NOT in form")

        # Extra info
        st.info(f"Strike Rate: {strike_rate}")
        st.info(f"Runs: {runs}")
        st.info(f"Balls: {balls}")

# ================= FOOTER =================
st.divider()
st.markdown(
    "<p style='text-align:center;'>Built with ❤️ using Streamlit & Machine Learning</p>",
    unsafe_allow_html=True
)