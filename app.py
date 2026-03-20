# # import streamlit as st
# # import numpy as np
# # import pickle

# # # ================= CONFIG =================
# # st.set_page_config(page_title="IPL 2026 - Player Form Predictor", page_icon="🏏", layout="wide")

# # # ================= LOAD MODEL =================
# # @st.cache_resource
# # def load_model():
# #     with open("best_model.pkl", "rb") as f:
# #         return pickle.load(f)

# # model = load_model()

# # # ================= TITLE =================
# # st.markdown("<h1 style='text-align:center;'>🏏 IPL 2026 - Batsman Form Predictor</h1>", unsafe_allow_html=True)
# # st.markdown("<p style='text-align:center;'>Predict whether a player is in form using ML</p>", unsafe_allow_html=True)
# # st.divider()

# # # ================= INPUT =================
# # st.subheader("📊 Enter Player Stats")

# # col1, col2, col3 = st.columns(3)

# # with col1:
# #     sr = st.number_input("SR (Strike Rate Raw)", 0.0)
# #     runs = st.number_input("Runs", 0)
# #     balls = st.number_input("Balls", 1)
# #     fours = st.number_input("4s", 0)
# #     sixes = st.number_input("6s", 0)

# # with col2:
# #     avg = st.number_input("Average (AVG)", 0.0)
# #     matches = st.number_input("Matches", 0)
# #     innings = st.number_input("Innings", 0)
# #     not_out = st.number_input("Not Outs", 0)
# #     strike_rate = st.number_input("Strike Rate (SR calc)", 0.0)

# # with col3:
# #     high_score = st.number_input("Highest Score", 0)
# #     fifty = st.number_input("50s", 0)
# #     hundred = st.number_input("100s", 0)
# #     ducks = st.number_input("Ducks", 0)

# # # ================= PREDICT =================
# # if st.button("🚀 Predict Form", use_container_width=True):

# #     # 🔥 EXACT 14 FEATURES (MATCH TRAINING)
# #     input_data = np.array([[
# #         sr,
# #         runs,
# #         balls,
# #         fours,
# #         sixes,
# #         avg,
# #         matches,
# #         innings,
# #         not_out,
# #         strike_rate,
# #         high_score,
# #         fifty,
# #         hundred,
# #         ducks
# #     ]])

# #     st.write("Input shape:", input_data.shape)

# #     prediction = model.predict(input_data)[0]

# #     if prediction == 1:
# #         st.success("🔥 Player is IN FORM")
# #     else:
# #         st.error("❌ Player is NOT in form")

# # st.divider()
# # st.markdown("<p style='text-align:center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
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
# st.markdown("<p style='text-align:center;'>Enter player details manually and predict form</p>", unsafe_allow_html=True)
# st.divider()

# # ================= PLAYER NAME =================
# player_name = st.text_input("✍️ Enter Player Name")

# # ================= INPUT =================
# st.subheader("📊 Enter Player Stats")

# col1, col2, col3 = st.columns(3)

# with col1:
#     sr = st.number_input("SR (Raw)", min_value=0.0, value=140.0)
#     runs = st.number_input("Runs", min_value=0, value=300)
#     balls = st.number_input("Balls", min_value=1, value=200)
#     fours = st.number_input("4s", min_value=0, value=30)
#     sixes = st.number_input("6s", min_value=0, value=10)

# with col2:
#     avg = st.number_input("Average (AVG)", min_value=0.0, value=35.0)
#     matches = st.number_input("Matches", min_value=0, value=10)
#     innings = st.number_input("Innings", min_value=0, value=10)
#     not_out = st.number_input("Not Outs", min_value=0, value=2)
#     strike_rate = st.number_input("Strike Rate", min_value=0.0, value=140.0)

# with col3:
#     high_score = st.number_input("Highest Score", min_value=0, value=80)
#     fifty = st.number_input("50s", min_value=0, value=3)
#     hundred = st.number_input("100s", min_value=0, value=0)
#     ducks = st.number_input("Ducks", min_value=0, value=1)

# # ================= PREDICT =================
# if st.button("🚀 Predict Form", use_container_width=True):

#     if player_name.strip() == "":
#         st.warning("⚠️ Please enter player name")
#     else:
#         input_data = np.array([[
#             sr,
#             runs,
#             balls,
#             fours,
#             sixes,
#             avg,
#             matches,
#             innings,
#             not_out,
#             strike_rate,
#             high_score,
#             fifty,
#             hundred,
#             ducks
#         ]])

#         st.write("Input shape:", input_data.shape)

#         prediction = model.predict(input_data)[0]

#         st.subheader(f"📊 Player: {player_name}")

#         if prediction == 1:
#             st.success("🔥 Player is IN FORM")
#         else:
#             st.error("❌ Player is NOT in form")

# st.divider()
# st.markdown("<p style='text-align:center;'>Built with ❤️ using Streamlit & ML</p>", unsafe_allow_html=True)

import streamlit as st
import base64

# ================= BACKGROUND FUNCTION =================
def set_bg():
    with open("bg.jpg", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(f"""
    <style>

    /* 🔥 Background Image */
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
                    url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 🔥 Text visible */
    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}

    /* 🔥 Button style */
    .stButton>button {{
        background: linear-gradient(90deg, #ff416c, #ff4b2b);
        color: white;
        border-radius: 10px;
        font-size: 18px;
    }}

    .stButton>button:hover {{
        transform: scale(1.05);
        box-shadow: 0px 0px 15px #ff4b2b;
    }}

    /* 🔥 Input boxes */
    input {{
        border-radius: 10px !important;
    }}

    /* 🔥 Sidebar */
    [data-testid="stSidebar"] {{
        background: rgba(0,0,0,0.6);
    }}

    </style>
    """, unsafe_allow_html=True)

# APPLY BACKGROUND
set_bg()
