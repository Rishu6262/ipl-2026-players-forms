import streamlit as st
import numpy as np
import pickle

# ================= CONFIG =================
st.set_page_config(page_title="IPL 2026 Predictor", page_icon="🏏", layout="wide")

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    with open("best_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ================= TITLE =================
st.markdown("<h1 style='text-align:center;'>🏏 IPL 2026 - Player Form Predictor</h1>", unsafe_allow_html=True)
st.divider()

# ================= INPUT =================
st.subheader("📊 Enter Player Stats")

col1, col2, col3 = st.columns(3)

with col1:
    runs = st.number_input("Runs", 0)
    balls = st.number_input("Balls", 1)
    fours = st.number_input("4s", 0)
    sixes = st.number_input("6s", 0)
    matches = st.number_input("Matches", 0)

with col2:
    innings = st.number_input("Innings", 0)
    not_out = st.number_input("Not Outs", 0)
    avg = st.number_input("Average", 0.0)
    strike_rate = st.number_input("Strike Rate", 0.0)
    high_score = st.number_input("Highest Score", 0)

with col3:
    fifty = st.number_input("50s", 0)
    hundred = st.number_input("100s", 0)
    ducks = st.number_input("Ducks", 0)

# ================= PREDICT =================
if st.button("🚀 Predict Form", use_container_width=True):

    input_data = np.array([[
        strike_rate, runs, balls, fours, sixes,
        avg, matches, innings, not_out,
        high_score, fifty, hundred, ducks
    ]])

    # DEBUG
    st.write("Input shape:", input_data.shape)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🔥 Player is IN FORM")
    else:
        st.error("❌ Player is NOT in form")

st.divider()
st.markdown("<p style='text-align:center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
