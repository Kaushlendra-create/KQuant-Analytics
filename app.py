import streamlit as st
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="K-Quant Analytics",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.main { 
    background-color: #0b0e14; 
    color: #d1d1d1; 
    font-family: 'Georgia', serif; 
}

.founder-text { 
    color: #c5a059; 
    font-size: 1.1rem; 
    letter-spacing: 2px; 
    text-transform: uppercase; 
    font-weight: 300; 
    margin-top: -5px; 
}

h1 { 
    color: #ffffff !important; 
    font-weight: 700; 
    letter-spacing: -1px; 
    font-family: 'Helvetica Neue', sans-serif; 
}

h2, h3 { 
    color: #c5a059 !important; 
    border-left: 3px solid #c5a059; 
    padding-left: 15px; 
    font-family: 'Helvetica Neue', sans-serif; 
    margin-top: 30px; 
}

.stMetric { 
    background-color: #161b22; 
    border: 1px solid #30363d; 
    padding: 15px; 
    border-radius: 4px; 
}

.job-box { 
    background-color: #161b22; 
    border: 1px solid #30363d; 
    padding: 30px; 
    border-radius: 6px; 
    margin-top: 20px; 
}
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

# ================= MARKET METRICS =================
m1, m2, m3, m4 = st.columns(4)
m1.metric("EUR/USD", "1.0845", "+0.19%")
m2.metric("GBP/USD", "1.2630", "-0.12%")
m3.metric("USD/JPY", "148.12", "+0.31%")
m4.metric("XAU/USD", "$2,034.50", "+0.60%")

st.divider()
# ================= PERFORMANCE DASHBOARD =================
st.header("Performance Dashboard")

if os.path.exists("dashboard.png"):
    st.image("Dashboard.png", caption="Weekly performance showing Win Rate, Sharpe Ratio, and Risk Metrics", use_column_width=True)
else:
    st.info("Dashboard image will be available soon.")

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

st.divider()

# ================= STRATEGY VIDEO =================
st.header("Strategy Development & Execution")
if os.path.exists("demo.mp4"):
    st.video("demo.mp4")
else:
    st.info("Strategy execution demonstration will be available soon.")

st.divider()

# ================= CAREER SECTION =================
st.header("Career Opportunities")
st.markdown("### Join Our Quantitative Research Team")

career_content = """
<div class="job-box">

<div style="color:#c5a059; font-size:0.85rem; font-weight:bold; text-transform:uppercase;">
Current Opening: Full-Time / Remote
</div>

<div style="color:#ffffff; font-size:1.8rem; font-weight:bold; margin-bottom:5px;">
Quantitative Analyst – FX Research
</div>

<p style="color:#8b949e;">
<b>Department:</b> Quantitative Research & Alpha Engineering
</p>

<hr style="border-color:#30363d; margin:20px 0;">

<h4 style="color:#c5a059;">Role Overview</h4>
<p style="line-height:1.6;">
We are seeking a disciplined and research-oriented Quantitative Analyst to contribute
to our Forex quantitative research operations. The role involves end-to-end strategy
research, including development, backtesting, performance evaluation, and refinement
of systematic trading strategies across multiple currency pairs.
</p>

<div style="background-color:#1a1f28; border:1px solid #30363d; padding:20px; border-radius:6px; margin-top:20px;">
<h4 style="color:#c5a059;">Perks & Growth</h4>
<ul style="line-height:1.8; color:#ffffff;">
<li>30-Day Paid Validation Phase</li>
<li>Monthly Stipend: ₹5000 (Validation Phase)</li>
<li>Long-term Quant Career Path</li>
<li>Capital scaling opportunities for consistent performers</li>
<li>Performance-based stipend hikes & profit sharing</li>
</ul>
</div>


<h4 style="color:#c5a059; margin-top:25px;">Key Responsibilities</h4>
<ul style="line-height:1.8;">
<li>Develop and research multiple Forex trading strategies across different currency pairs</li>
<li>Apply technical indicators, statistical methods, and machine learning models (e.g., LSTM)</li>
<li>Perform rigorous backtesting using historical market data</li>
<li>Evaluate strategies using Win Rate, Drawdown, Sharpe Ratio, Profit Factor, and risk metrics</li>
<li>Prepare dashboards and detailed monthly performance reports</li>
<li>Identify structural weaknesses in underperforming strategies and improve robustness</li>
<li>Develop a strong understanding of Forex sessions, kill zones, pips, lot sizing, volume, and risk management</li>
<li>Support deployment of validated strategies into live and funded trading environments</li>
</ul>

<h4 style="color:#c5a059; margin-top:25px;">Required Qualifications</h4>
<ul style="line-height:1.8;">
<li>Strong foundation in Mathematics, Probability, and Statistical Analysis</li>
<li>Solid understanding of Forex market structure and trading mechanics</li>
<li>Ability to design, analyze, and interpret quantitative backtests in Python;
 use of AI-assisted coding tools is permitted, with emphasis on conceptual understanding and result validation.</li>
<li>Familiarity with Sharpe ratio, drawdowns, and performance analytics</li>
<li>Research-driven mindset with patience and discipline</li>
</ul>

</div>
"""

st.markdown(career_content, unsafe_allow_html=True)

st.link_button(
    "Access Official Application Form",
    "https://bit.ly/4rizFx1",
    use_container_width=True
)

st.divider()

# ================= STRATEGIC ROADMAP =================
st.header("Institutional Scaling Roadmap")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Validation", "Deployment", "Analytics", "Scaling"]
)

with tab1:
    st.markdown("""
    **Phase 1: Research & Validation**

    • Identify statistically significant market inefficiencies  
    • Conduct multi-timeframe backtesting on historical data  
    • Validate strategies using institutional performance metrics  
    • Eliminate non-robust and curve-fitted models  
    """)

with tab2:
    st.markdown("""
    **Phase 2: Systematic Deployment**

    • Convert validated strategies into automated execution systems  
    • Integrate position sizing and capital allocation rules  
    • Ensure disciplined, rule-based trade execution  
    • Stress-test strategies across volatility regimes  
    """)

with tab3:
    st.markdown("""
    **Phase 3: Performance Analytics & Risk Monitoring**

    • Monitor live equity curves and trade behavior  
    • Track drawdowns, exposure, volatility, and risk concentration  
    • Detect performance decay and regime changes  
    • Refine strategies based on analytical insights  
    """)

with tab4:
    st.markdown("""
    **Phase 4: Institutional Scaling & Capital Growth**

    • Scale capital across uncorrelated strategies  
    • Expand research across FX, Metals, and other asset classes  
    • Optimize portfolio-level risk-adjusted returns  
    • Prepare infrastructure for prop and institutional capital  
    """)

st.divider()

# ================= FOOTER =================
st.write("**Contact:** kaushlendra30068@gmail.com | +91 78188 26377")
