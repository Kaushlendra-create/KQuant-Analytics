import streamlit as st
import os
import base64
import yfinance as yf
from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go
from supabase import create_client, Client
import datetime as dt
import resend
# 1. PAGE CONFIG (Sabse Pehle)
st.set_page_config(
    page_title="K-Quant Analytics",
    layout="wide"
)

# 2. SUPABASE CONNECTION (Ye missing tha, isliye error aa raha tha)
# Isko yahan dalne se neeche ke saare functions ise pehchan lenge
url = "https://hxgsrterljeziyyqsyht.supabase.co"
key = "sb_publishable_Wyi6YHhFdiFIoKge9n4aoQ_dbmwjy-u"
supabase: Client = create_client(url, key)

# 3. EMAIL CONFIG
resend.api_key = "re_3dDVUfh4_P8SDAsLpTiDRoHjQg826TyC8"

# --- SESSION STATE INITIALIZATION ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""

# --- EMAIL FUNCTION ---
def send_welcome_email(user_email, username):
    try:
        resend.Emails.send({
            "from": "K-Quant Terminal <onboarding@resend.dev>", 
            "to": user_email,
            "subject": "Institutional Access Granted | Welcome to K-Quant Terminal",
            "html": f"""
            <div style="font-family: Arial, sans-serif; background-color: #0b0e14; color: #ffffff; padding: 30px; border: 1px solid #c5a059; border-radius: 10px;">
                <h1 style="color: #c5a059; border-bottom: 1px solid #c5a059; padding-bottom: 10px;">K-QUANT ANALYTICS</h1>
                <p style="font-size: 16px;">Dear <b>{username}</b>,</p>
                <p>Welcome to the inner circle of K-Quant Analytics. Your institutional access to our <b>Asset Frameworks</b> has been successfully provisioned.</p>
                <h3 style="color: #c5a059;">Your Quant Access Includes:</h3>
                <ul>
                    <li><strong>Agile-Five Ultra:</strong> Live Strategy Monitoring.</li>
                    <li><strong>Alpha-Gen v5.0:</strong> Institutional Research Modules.</li>
                    <li><strong>Risk Engineering:</strong> Systematic Backtesting Reports.</li>
                </ul>
                <p style="background-color: #161b22; padding: 15px; border-left: 4px solid #c5a059;">
                    <i>"In the world of trading, data is the weapon, but logic is the shield."</i>
                </p>
                <p>Log in to your terminal now to explore our proprietary models.</p>
                <hr style="border: 0; border-top: 1px solid #30363d; margin: 20px 0;">
                <p style="font-size: 12px; color: #8b949e;">Founded by Kaushlendra | Quantitative Research & Risk Engineering</p>
            </div>
            """
        })
        return True
    except Exception as e:
        print(f"Email Error: {e}")
        return False

# --- AUTH FUNCTIONS ---
def signup_user(email, username, password):
    try:
        data = {"email": email, "username": username, "password": password}
        supabase.table("profiles").insert(data).execute()
        send_welcome_email(email, username)
        return True
    except Exception as e:
        st.error(f"Signup Error: {e}")
        return False

def login_user(username, password):
    try:
        res = supabase.table("profiles").select("*").eq("username", username).eq("password", password).execute()
        return len(res.data) > 0
    except Exception as e:
        return False

def get_pdf_download_link(pdf_file):
    if os.path.exists(pdf_file):
        with open(pdf_file, "rb") as f:
            bytes_data = f.read()
        b64 = base64.b64encode(bytes_data).decode()
        return f'''
        <a href="data:application/octet-stream;base64,{b64}" download="{pdf_file}" 
           style="text-decoration: none;">
           <button style="background-color: #c5a059; color: white; padding: 12px 24px; 
           border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 100%;">
           📥 Download Full Whitepaper (PDF)
           </button>
        </a>
        '''
    else:
        return "⚠️ File missing on server."

# --- UI COMPONENTS ---
def auth_ui():
    st.markdown("""
        <div style='text-align: center; padding-bottom: 20px;'>
            <h1 style='color: #c5a059; font-family: "Helvetica Neue", sans-serif; letter-spacing: 3px;'>
                WELCOME TO K-QUANT TERMINAL
            </h1>
            <p style='color: #8b949e; font-size: 1.1rem;'>Institutional Grade Quantitative Research & Execution</p>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔐 Secure Login", "📝 Create Account"])
    
    with tab1:
        u_name = st.text_input("Username", key="l_user")
        u_pass = st.text_input("Password", type="password", key="l_pass")
        if st.button("Sign In", use_container_width=True):
            if login_user(u_name, u_pass):
                st.session_state['logged_in'] = True
                st.session_state['user_name'] = u_name
                st.rerun()
            else:
                st.error("Invalid Username or Password")

    with tab2:
        s_email = st.text_input("Email Address")
        s_user = st.text_input("Choose Username")
        s_pass = st.text_input("Set Password", type="password")
        if st.button("Register Now", use_container_width=True):
            if signup_user(s_email, s_user, s_pass):
                st.balloons()
                st.success(f"Welcome {s_user}! Account created & email sent. Please Login.")
            else:
                st.error("Registration failed. Username might exist.")

# ================= PAGE CONTROL LOGIC =================
if not st.session_state.get('logged_in', False):
    auth_ui()
    st.stop()
else:
    # --- DASHBOARD START ---
    if st.sidebar.button("Log Out"):
        st.session_state['logged_in'] = False
        st.rerun()
    
    st.sidebar.success(f"Welcome, {st.session_state['user_name']}!")
    st_autorefresh(interval=30000, key="datarefresh")

    # --- YAHAN SE AAPKA BAAKI CSS AUR DASHBOARD CHALEGA ---
    st.markdown("<style>.main { background-color: #0b0e14; }</style>", unsafe_allow_html=True)
    # (Baki ka dashboard code jo aapne likha tha yahan aayega...)
    # ================= CUSTOM CSS =================
    st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #d1d1d1; font-family: 'Georgia', serif; }
    .founder-text { color: #c5a059; font-size: 1.1rem; letter-spacing: 2px; text-transform: uppercase; font-weight: 300; margin-top: -5px; }
    h1 { color: #ffffff !important; font-weight: 700; letter-spacing: -1px; font-family: 'Helvetica Neue', sans-serif; }
    h2, h3 { color: #c5a059 !important; border-left: 3px solid #c5a059; padding-left: 15px; font-family: 'Helvetica Neue', sans-serif; margin-top: 30px; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 4px; }
    .job-box { background-color: #161b22; border: 1px solid #30363d; padding: 30px; border-radius: 6px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

    # ================= HEADER =================
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("image.jpeg"):
            st.image("image.jpeg", width=110)
        else:
            st.subheader("K-QUANT")

    with col2:
        st.markdown("<h1>K-QUANT ANALYTICS</h1>", unsafe_allow_html=True)
        st.markdown("<div class='founder-text'>Founded by Kaushlendra </div>", unsafe_allow_html=True)
        st.write("Quantitative Research, Risk Engineering & Automated Trading")

    st.divider()

    # ================= LIVE MARKET METRICS =================
    def get_live_price(ticker):
        try:
            data = yf.Ticker(ticker).history(period="1d", interval="1m")
            latest_price = data['Close'].iloc[-1]
            prev_close = data['Open'].iloc[0]
            change = ((latest_price - prev_close) / prev_close) * 100
            return f"{latest_price:.4f}", f"{change:+.2f}%"
        except:
            return "N/A", "0.00%"

    m1, m2, m3, m4 = st.columns(4)
    eurusd_p, eurusd_c = get_live_price("EURUSD=X")
    gbpusd_p, gbpusd_c = get_live_price("GBPUSD=X")
    usdjpy_p, usdjpy_c = get_live_price("USDJPY=X")
    xauusd_p, xauusd_c = get_live_price("GC=F")

    m1.metric("EUR/USD", eurusd_p, eurusd_c)
    m2.metric("GBP/USD", gbpusd_p, gbpusd_c)
    m3.metric("USD/JPY", usdjpy_p, usdjpy_c)
    m4.metric("XAU/USD", f"${xauusd_p}", xauusd_c)

    if st.button('🔄 Refresh Prices'):
        st.rerun()

    # ================= LIVE STRATEGY MONITORING =================
    st.subheader(" Live Strategy Execution: Agile-Five Ultra")
    try:
        ticker_eur = yf.Ticker("EURUSD=X")
        data_eur = ticker_eur.history(period="1d", interval="1m")
        if not data_eur.empty:
            with st.expander("📊 View Live EURUSD Candlestick Chart", expanded=False):
                fig = go.Figure(data=[go.Candlestick(
                    x=data_eur.index, open=data_eur['Open'], high=data_eur['High'],
                    low=data_eur['Low'], close=data_eur['Close'],
                    increasing_line_color='#00ff00', decreasing_line_color='#ff0000'
                )])
                fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False, height=400)
                st.plotly_chart(fig, use_container_width=True)
                st.caption("Live Candlestick Feed (1M Interval).")
        else:
            st.warning("Waiting for EUR/USD market data...")
    except Exception as e:
        st.error(f"Strategy Monitor Error: {e}")

    st.divider()

    # ================= LEAD MAGNET =================
    st.header("Institutional Research Access")
    with st.container():
        st.markdown("Want to dive deep into our **HMM & Kalman Filter** framework? Enter your email to receive the whitepaper.")
        col_e1, col_e2 = st.columns([2, 1])
        with col_e1:
            user_email = st.text_input("Enter Email Address", placeholder="quant.researcher@example.com")
        with col_e2:
            st.write("##")
            if st.button("Get Whitepaper Access"):
                if "@" in user_email:
                    pdf_filename = "Brochure.pdf.pdf"
                    if os.path.exists(pdf_filename):
                        st.success("Access Granted! Click below to download.")
                        st.markdown(get_pdf_download_link(pdf_filename), unsafe_allow_html=True)
                    else:
                        st.error("Whitepaper file not found on server.")
                else:
                    st.warning("Please enter a valid email address.")

    st.divider()

  
    # ================= ABOUT =================
    st.header("About K-Quant Analytics")
    st.markdown("""
K-Quant Analytics is a proprietary quantitative research firm focused on the systematic
research, evaluation, and deployment of data-driven trading strategies within the global
Forex market.

We conduct in-depth research across multiple currency pairs by developing diverse
strategies using technical indicators, statistical formulas, historical price data,
and machine learning models such as Long Short-Term Memory (LSTM) networks.
Each strategy undergoes rigorous backtesting to evaluate win rate, drawdown,
Sharpe ratio, profit factor, and overall risk efficiency.

Rather than frequently changing strategy logic, we emphasize deep analytical
understanding. When performance falls below expectations, we identify structural
weaknesses and refine parameters while preserving the core strategy framework.
Strategies that demonstrate consistent, risk-adjusted performance are gradually
transitioned into live execution and deployed across multiple funded accounts.
""")
    st.markdown("""
**Performance Optimization & Monitoring**

- **Quantitative Strategy Research** – Multi-strategy development using technical,
statistical, and machine learning methodologies  
- **Systematic Backtesting & Evaluation** – Robust performance analysis with
institutional-grade metrics and reporting  
- **Risk & Execution Discipline** – Strong focus on Forex market structure, sessions,
kill zones, position sizing, and capital protection  
""")


    # ================= VIDEO =================
    st.header("Strategy Development & Execution")
    with st.expander("▶️ Watch Execution Demo", expanded=True):
        if os.path.exists("demo.mp4"): st.video("demo.mp4")
        else: st.warning("demo.mp4 not found.")

    # ================= CAREERS =================
    st.header("Career Opportunities")
    st.markdown(career_content if 'career_content' in locals() else "Quantitative Analyst Openings - Apply Below", unsafe_allow_html=True)
    st.link_button("Apply Now", "https://bit.ly/4rizFx1", use_container_width=True)



    # ================= FOOTER =================
    st.divider()
    st.write("**Contact:** kaushlendra30068@gmail.com | +91 78188 26377")