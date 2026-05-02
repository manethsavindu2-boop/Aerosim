import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURATION & THEME ---
st.set_page_config(page_title="Avionix Systems Stealth", layout="wide", initial_sidebar_state="expanded")

# අතිශය අඳුරු Wallpaper එකක් සහ කළු පැහැති අකුරු (Black Fonts) සැකසීම
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
    
    /* Real Dark ISS/Space Wallpaper */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.95)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Main Headings - Glow Green */
    h1, h2, h3 { 
        font-family: 'Orbitron', sans-serif !important; 
        color: #39FF14 !important; 
        text-shadow: 0px 0px 8px rgba(57, 255, 20, 0.6);
    }

    /* Black Font for readability in Data Cards */
    p, span, div, label { 
        font-family: 'JetBrains Mono', monospace !important; 
        color: #000000 !important; /* කළු පැහැති අකුරු */
        font-weight: 600;
    }
    
    /* පද්ධතියේ පසුබිම් කොටස් සුදු/ලා වර්ණ ගැන්වීම (කළු අකුරු කැපී පෙනීමට) */
    .stMetric, .stSlider, .stSelectbox, .stNumberInput, div.stAlert {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 5px;
        padding: 15px !important;
        border: 2px solid #39FF14;
    }

    /* Sidebar - Ultra Dark with Neon Border */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 3px solid #39FF14;
    }
    
    /* Sidebar අකුරු පමණක් සුදු පැහැයෙන් (අඳුරු නිසා) */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #39FF14 !important;
    }

    /* Stealth Buttons */
    .stButton>button {
        background: #000000;
        color: #39FF14;
        border: 2px solid #39FF14;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #39FF14;
        color: #000000;
        box-shadow: 0px 0px 20px #39FF14;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def change_page(page_name):
    st.session_state.page = page_name

# --- 1. LANDING PAGE ---
if st.session_state.page == 'landing':
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("🛸 AVIONIX STEALTH CORE")
    
    # Landing page එකේ අකුරු කළු වීමට සුදු පැහැති box එකක් යෙදීම
    st.info("""
    ### [SYSTEM READY]
    **COMMANDER:** MANETH SAVINDU  
    **STATION:** ISS ORBITAL LAB  
    Click below to access the high-performance dashboard.
    """)
    
    if st.button("EXECUTE SYSTEM INITIALIZATION"):
        change_page('dashboard')

# --- 2. DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.sidebar.title("🛰️ ISS CONTROL")
    if st.sidebar.button("LOGOUT"): change_page('landing')
    
    st.title("✈️ MISSION CONTROL DASHBOARD")
    st.write("---")

    selected_mod = st.sidebar.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header(f"DATA ANALYTICS: {selected_mod}")
        
        if selected_mod == "Module 1":
            st.write("Processing Mathematical Logic Flows...")
            val = st.slider("Signal Threshold", 0, 500, 250)
            st.line_chart(np.random.randn(20, 1))
            st.success(f"OUTPUT DATA: {val * 1.22} (Black Font Enabled)")

        elif selected_mod == "Module 8":
            st.write("Simulating Supersonic Airflow...")
            mach = st.number_input("Mach Number", value=1.2)
            lift = 0.5 * 0.3 * (mach**2) * 20 * 0.7
            st.metric("CURRENT LIFT FORCE", f"{round(lift, 2)} kN")
            st.area_chart(np.random.randn(20, 1))

        else:
            st.write(f"Technical specifications for {selected_mod} loading...")
            st.progress(85)

    with col2:
        st.header("⚙️ MONITOR")
        st.metric("CABIN PRESSURE", "14.7 PSI", "STABLE")
        st.metric("CORE TEMP", "22°C", "NOMINAL")
        
        st.write("---")
        st.header("⚠️ ALERTS")
        fail = st.selectbox("SIMULATE ERROR:", ["None", "Stall-alert", "Engine Heats"])
        
        if fail == "Stall-alert":
            st.error("SYMPTOMS: LOW AIRSPEED | ACTION: NOSE DOWN")
        elif fail == "Engine Heats":
            st.error("SYMPTOMS: TEMP EXCEEDED | ACTION: CUT FUEL")

# --- FOOTER ---
st.sidebar.write("---")
st.sidebar.caption("SECURE CONNECTION: ACTIVE")
st.sidebar.caption("V5.0 STEALTH EDITION")