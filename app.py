import streamlit as st
import os
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="K-Quant Analytics | Quantitative Research Lab", layout="wide")

# --- CUSTOM CSS FOR INSTITUTIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e0e0; }
    h1, h2, h3 { color: #00f2ff !important; font-family: 'Helvetica Neue', Arial, sans-serif; }
    .stInfo { background-color: #161b22; border: 1px solid #30363d; color: #c9d1d9; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; background-color: transparent; border-bottom: 2px solid #30363d; color: #8b949e; }
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #00f2ff !important; color: #00f2ff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- AUTO-DETECT LOGO ---
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
        st.subheader("K-QUANT")

with col2:
    st.title("K-Quant Analytics")
    st.write("Founded by **Kaushlendra Yadav** | Proprietary Quantitative Research & Algorithmic Trading")

st.divider()

# --- PROFESSIONAL ABOUT US SECTION ---
st.header("About K-Quant Analytics")
st.info("""
K-Quant Analytics is a premier proprietary quantitative research firm dedicated to achieving superior risk-adjusted returns through mathematical rigor and computational intelligence. We specialize in bridging the gap between classical financial theory and cutting-edge Machine Learning to capture structural market inefficiencies.

**Core Pillars of Excellence:**
* **Quantitative Alpha Generation:** Deploying advanced Deep Learning architectures to identify high-probability patterns in financial data.
* **Systematic Execution Framework:** Low-latency infrastructure bridging analytical environments with institutional execution platforms.
* **Risk Engineering:** Prioritizing capital preservation through rigorous portfolio optimization and volatility management.
""")

# --- STRATEGY DEMO ---
st.header("Strategy Execution Analysis")
if os.path.exists("demo.mp4"):
    st.video("demo.mp4")
else:
    st.warning("Strategy validation video (demo.mp4) not found in directory.")

st.divider()

# --- STRATEGIC ROADMAP ---
st.header("KQuant Insight: Strategic Roadmap")
t1, t2, t3, t4 = st.tabs(["Phase 1: Validation", "Phase 2: Deployment", "Phase 3: Analytics", "Phase 4: Scaling"])

with t1: 
    st.markdown("""
    **Strategy Validation**
    * Identification of high-alpha market inefficiencies.
    * Parameter optimization and statistical robustness testing.
    * Performance Target: Win-Rate > 50% with optimized Sharpe Ratio.
    """)

with t2: 
    st.markdown("""
    **Algorithmic Deployment**
    * Integration of validated strategies into automated execution systems.
    * Transition to risk oversight and execution monitoring protocols.
    """)

with t3: 
    st.markdown("""
    **Performance Analytics**
    * Real-time monitoring of live equity curves and risk metrics.
    * Key Indicators: Max Drawdown, Sortino Ratio, and Profit Factor.
    """)

with t4: 
    st.markdown("""
    **Institutional Scaling**
    * Formal induction into the core Quantitative Research team.
    * Strategic capital allocation and performance-based equity models.
    """)

st.divider()

# --- CONTACT / CALL TO ACTION ---
st.link_button("Access Official Application Form", "https://bit.ly/4rizFx1")
st.write("**Contact:** kaushlendra30068@gmail.com | +91 78188 26377")