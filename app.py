import streamlit as st
import os
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="K-Quant Analytics | Lab", page_icon="📈", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    h1, h2, h3 { color: #00f2ff !important; }
    .stInfo { background-color: #161b22; border: 1px solid #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# --- AUTO-DETECT LOGO (Fix for your .png/.jpeg issue) ---
logo_path = None
for file in os.listdir("."):
    if file.lower().startswith("image") and file.lower().endswith((".png", ".jpg", ".jpeg", ".jfif")):
        logo_path = file
        break

# --- HEADER ---
col1, col2 = st.columns([1, 4])
with col1:
    if logo_path:
        st.image(logo_path, width=150)
    else:
        st.header("📊")

with col2:
    st.title("K-Quant Analytics")
    st.write("Founded by **Kaushlendra Yadav** | Bridging AI and Financial Markets")

st.divider()

# --- NEW "ABOUT US" SECTION (Replacing NTCC) ---
st.header("🏢 About Us")
st.info("""
**K-Quant Analytics** is a specialized research lab dedicated to the development of high-frequency trading (HFT) models and AI-driven quantitative strategies. 
Our mission is to replace subjective market intuition with rigorous statistical validation. 

Currently, we are executing an advanced project under the **NTCC Framework**, focusing on:
* **Hybrid Architectures:** Combining LSTM (Deep Learning) with traditional Mean Reversion models.
* **MT5 Integration:** Seamless execution of Python-based logic in live market environments.
* **Risk Management:** Prioritizing Capital Preservation through dynamic Sharpe Ratio optimization.
""")

# --- PROJECT DEMO ---
st.header("📺 Strategy Execution Demo")
# Video detection
if os.path.exists("demo.mp4"):
    st.video("demo.mp4")
else:
    st.warning("⚠️ 'demo.mp4' file not found in the folder.")

st.divider()

# --- HIRING SECTION ---
st.header("🚀 Join the Research Cohort")
t1, t2, t3, t4 = st.tabs(["Validation", "Deployment", "Analytics", "Scaling"])
with t1: st.write("Phase 1: 30-day strategy stress testing.")
with t2: st.write("Phase 2: Transition to AI Execution Bots.")
with t3: st.write("Phase 3: Live dashboarding of performance metrics.")
with t4: st.write("Phase 4: Full-time role with profit sharing.")

st.divider()

# --- CTA ---
st.link_button("🚀 Apply via Official Form", "https://bit.ly/4rizFx1")
st.write("**Contact:** +91 78188 26377 | kaushlendra30068@gmail.com")