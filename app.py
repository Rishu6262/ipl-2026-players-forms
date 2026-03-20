# import streamlit as st
# import numpy as np
# import pickle

# # ================= CONFIG =================
# st.set_page_config(page_title="IPL 2026 - Player Form Predictor", page_icon="🏏", layout="wide")

# # ================= LOAD MODEL =================
# @st.cache_resource
# def load_model():
#     with open("best_model.pkl", "rb") as f:
#         return pickle.load(f)

# model = load_model()

# # ================= TITLE =================
# st.markdown("<h1 style='text-align:center;'>🏏 IPL 2026 - Batsman Form Predictor</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center;'>Predict whether a player is in form using ML</p>", unsafe_allow_html=True)
# st.divider()

# # ================= INPUT =================
# st.subheader("📊 Enter Player Stats")

# col1, col2, col3 = st.columns(3)

# with col1:
#     sr = st.number_input("SR (Strike Rate Raw)", 0.0)
#     runs = st.number_input("Runs", 0)
#     balls = st.number_input("Balls", 1)
#     fours = st.number_input("4s", 0)
#     sixes = st.number_input("6s", 0)

# with col2:
#     avg = st.number_input("Average (AVG)", 0.0)
#     matches = st.number_input("Matches", 0)
#     innings = st.number_input("Innings", 0)
#     not_out = st.number_input("Not Outs", 0)
#     strike_rate = st.number_input("Strike Rate (SR calc)", 0.0)

# with col3:
#     high_score = st.number_input("Highest Score", 0)
#     fifty = st.number_input("50s", 0)
#     hundred = st.number_input("100s", 0)
#     ducks = st.number_input("Ducks", 0)

# # ================= PREDICT =================
# if st.button("🚀 Predict Form", use_container_width=True):

#     # 🔥 EXACT 14 FEATURES (MATCH TRAINING)
#     input_data = np.array([[
#         sr,
#         runs,
#         balls,
#         fours,
#         sixes,
#         avg,
#         matches,
#         innings,
#         not_out,
#         strike_rate,
#         high_score,
#         fifty,
#         hundred,
#         ducks
#     ]])

#     st.write("Input shape:", input_data.shape)

#     prediction = model.predict(input_data)[0]

#     if prediction == 1:
#         st.success("🔥 Player is IN FORM")
#     else:
#         st.error("❌ Player is NOT in form")

# st.divider()
# st.markdown("<p style='text-align:center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ================= CONFIG =================
st.set_page_config(page_title="IPL 2026 - Player Form Predictor", page_icon="🏏", layout="wide")

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    with open("best_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ================= LOAD DATA =================
@st.cache_data
def load_data():
    df = pd.read_csv("IPL2025Batters.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# 🔥 column name adjust if needed
PLAYER_COL = "Player" if "Player" in df.columns else "batter"

players = sorted(df[PLAYER_COL].dropna().unique())

# ================= TITLE =================
st.markdown("<h1 style='text-align:center;'>🏏 IPL 2026 - Batsman Form Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Select player and predict form using ML</p>", unsafe_allow_html=True)
st.divider()

# ================= PLAYER SELECT =================
player_name = st.selectbox("🔎 Select Player", players)

player_data = df[df[PLAYER_COL] == player_name].iloc[0]

# ================= INPUT =================
st.subheader("📊 Player Stats")

col1, col2, col3 = st.columns(3)

with col1:
    sr = st.number_input("SR (Raw)", value=float(player_data.get("SR", 0)))
    runs = st.number_input("Runs", value=int(player_data.get("Runs", 0)))
    balls = st.number_input("Balls", value=int(player_data.get("Balls", 1)))
    fours = st.number_input("4s", value=int(player_data.get("4s", 0)))
    sixes = st.number_input("6s", value=int(player_data.get("6s", 0)))

with col2:
    avg = st.number_input("Average", value=float(player_data.get("AVG", 0)))
    matches = st.number_input("Matches", value=int(player_data.get("Matches", 0)))
    innings = st.number_input("Innings", value=int(player_data.get("Innings", 0)))
    not_out = st.number_input("Not Outs", value=int(player_data.get("NO", 0)))
    strike_rate = st.number_input("Strike Rate", value=float(player_data.get("SR", 0)))

with col3:
    high_score = st.number_input("Highest Score", value=int(player_data.get("HS", 0)))
    fifty = st.number_input("50s", value=int(player_data.get("50s", 0)))
    hundred = st.number_input("100s", value=int(player_data.get("100s", 0)))
    ducks = st.number_input("Ducks", value=int(player_data.get("0", 0)))

# ================= PREDICT =================
if st.button("🚀 Predict Form", use_container_width=True):

    input_data = np.array([[
        sr,
        runs,
        balls,
        fours,
        sixes,
        avg,
        matches,
        innings,
        not_out,
        strike_rate,
        high_score,
        fifty,
        hundred,
        ducks
    ]])

    st.write("Input shape:", input_data.shape)

    prediction = model.predict(input_data)[0]

    st.subheader(f"📊 Player: {player_name}")

    if prediction == 1:
        st.success("🔥 Player is IN FORM")
    else:
        st.error("❌ Player is NOT in form")

st.divider()
st.markdown("<p style='text-align:center;'>Built with ❤️ using Streamlit & ML</p>", unsafe_allow_html=True)
