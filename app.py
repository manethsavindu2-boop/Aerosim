import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURATION & THEME ---
st.set_page_config(page_title="Avionix Systems Ultra", layout="wide", initial_sidebar_state="expanded")

# ඉතා අඳුරු (Dark) ISS/Fighter Jet Wallpaper එක සහ Stealth වර්ණ සැකසීම
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
    
    /* Dark Space/ISS/Jet Wallpaper */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.9)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Fighter Jet HUD (Head-Up Display) Colors */
    h1, h2, h3 { 
        font-family: 'Orbitron', sans-serif !important; 
        color: #39FF14 !important; /* Neon Green / HUD Color */
        text-shadow: 0px 0px 12px rgba(57, 255, 20, 0.7);
        letter-spacing: 2px;
    }

    p, span, div, label { 
        font-family: 'JetBrains Mono', monospace !important; 
        color: #00d4ff !important; /* Tactical Blue */
        font-weight: 500;
    }

    /* Dark Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(5, 5, 5, 0.98) !important;
        border-right: 2px solid #39FF14;
    }

    /* Metrics and Inputs */
    [data-testid="stMetricValue"] {
        color: #39FF14 !important;
        font-family: 'Orbitron', sans-serif;
    }

    /* Stealth Buttons */
    .stButton>button {
        background: transparent;
        color: #39FF14;
        border: 2px solid #39FF14;
        border-radius: 0px; /* Sharp edges for military look */
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        transition: 0.5s;
    }
    .stButton>button:hover {
        background: rgba(57, 255, 20, 0.2);
        box-shadow: 0px 0px 20px #39FF14;
        color: #ffffff;
    }

    /* Progress bar color */
    .stProgress > div > div > div > div {
        background-color: #39FF14;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def change_page(page_name):
    st.session_state.page = page_name

# --- 1. OPENING PAGE (STEALTH ENTRANCE) ---
if st.session_state.page == 'landing':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.title("⚡ AVIONIX STEALTH CORE")
    st.subheader("INTERNAL SYSTEMS : ISS COMMAND CENTER")
    
    col_l, col_r = st.columns([2,1])
    with col_l:
        st.write("""
        ### [SYSTEMS CHECK: OK]
        ### [ENCRYPTION: ACTIVE]
        Welcome, Engineer. Accessing orbital maintenance and aerodynamics database.
        """)
        if st.button("INITIALIZE INTERFACE"):
            change_page('dashboard')

# --- 2. DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.sidebar.title("🛰️ COMMAND PANEL")
    if st.sidebar.button("TERMINATE SESSION"): change_page('landing')
    
    st.title("🛸 MISSION DASHBOARD")
    st.write("---")

    # Module Selection (1 to 14)
    selected_mod = st.sidebar.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header(f"SYSTEM DATA: {selected_mod}")
        
        if selected_mod == "Module 1":
            st.subheader("Engineering Mathematics")
            st.write("Processing vector analysis and trigonometric data...")
            num = st.slider("Signal Gain", 0, 100, 75)
            st.line_chart(np.random.randn(25, 1))
            st.info(f"CALCULATED LOGIC: {hex(num * 10)}")

        elif selected_mod == "Module 8":
            st.subheader("Aerodynamics Flow")
            st.write("Simulating airflow over airfoil surfaces...")
            vel = st.number_input("Mach Velocity", value=0.85)
            lift = 0.5 * 0.413 * (vel**2) * 30 * 0.5 # Using altitude density
            st.metric("CURRENT LIFT FORCE", f"{round(lift, 2)} kN")
            st.area_chart(np.random.randn(15, 1))

        else:
            st.write(f"Secure data for {selected_mod} is being decrypted...")
            st.progress(70)
            st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", width=60)

    with col2:
        st.header("🛡️ CORE MONITOR")
        st.metric("OXYGEN LEVEL", "100%", "OPTIMAL")
        st.metric("HULL INTEGRITY", "99.4%", "SECURE")
        
        st.write("---")
        st.header("❗ CRITICAL ALERTS")
        fail = st.selectbox("FAILURE SIMULATION:", ["None", "Stall-alert", "Engine Overheat"])
        
        if fail == "Stall-alert":
            st.error(">>> WARNING: ANGLE OF ATTACK CRITICAL")
            st.warning(">>> ACTION: APPLY NOSE DOWN MOMENT")
        elif fail == "Engine Overheat":
            st.error(">>> ALERT: TURBINE TEMP EXCEEDED")
            st.warning(">>> ACTION: REDUCE FUEL FLOW")

# --- FOOTER ---
st.sidebar.write("---")
st.sidebar.caption("OPERATOR: MANETH SAVINDU")
st.sidebar.caption("STATION: LEO-AVIONIX-01")