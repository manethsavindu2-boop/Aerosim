import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURATION & THEME ---
st.set_page_config(page_title="Avionix Systems Pro", layout="wide", initial_sidebar_state="expanded")

# වෘත්තීය Aerospace Wallpaper එකක් සහ වර්ණ සැකසීම
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
    
    /* මුළු පිටුවේම පසුබිම (Wallpaper) */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.8)), 
                    url('https://images.unsplash.com/photo-1464039397811-476f652a343b?q=80&w=2068&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* අකුරු වර්ග සහ වර්ණ (Font types and Colors) */
    h1, h2, h3 { 
        font-family: 'Orbitron', sans-serif !important; 
        color: #00e5ff !important; /* Electric Cyan */
        text-shadow: 0px 0px 10px #00e5ff;
    }

    p, span, div, label { 
        font-family: 'JetBrains Mono', monospace !important; 
        color: #d1d1d1 !important; 
    }

    /* Sidebar පෙනුම */
    [data-testid="stSidebar"] {
        background-color: rgba(10, 15, 30, 0.9) !important;
        border-right: 1px solid #00e5ff;
    }

    /* බොත්තම් (Buttons) */
    .stButton>button {
        background: rgba(0, 229, 255, 0.1);
        color: #00e5ff;
        border: 2px solid #00e5ff;
        border-radius: 5px;
        font-family: 'Orbitron', sans-serif;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #00e5ff;
        color: black;
        box-shadow: 0px 0px 20px #00e5ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def change_page(page_name):
    st.session_state.page = page_name

# --- 1. OPENING PAGE (LANDING) ---
if st.session_state.page == 'landing':
    st.title("🛰️ AVIONIX SYSTEMS PRO")
    st.subheader("ADVANCED AEROSPACE ENGINEERING INTERFACE")
    
    st.write("""
    ### SYSTEM STATUS: READY
    This platform is designed for EASA Part 66 technical analysis and aerodynamic simulations.
    """)
    
    if st.button("INITIALIZE SYSTEM"):
        change_page('dashboard')

# --- 2. DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.sidebar.title("🛠️ AVIONIX CORE")
    if st.sidebar.button("LOGOUT"): change_page('landing')
    
    st.title("✈️ CONTROL DASHBOARD")
    st.write("---")

    # Module Selector
    selected_mod = st.sidebar.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header(f"DATA STREAM: {selected_mod}")
        
        # මොඩියුලයට අනුව වෙනස් වන ගණනය කිරීම් (Calculations)
        if selected_mod == "Module 1":
            st.subheader("Arithmetic & Geometry")
            val = st.slider("Input Frequency", 0, 100, 50)
            st.line_chart(np.random.randn(20, 1))
            st.info(f"Computed Logic Variance: {val * 1.5}")
            
        elif selected_mod == "Module 8":
            st.subheader("Aerodynamics & Lift Analysis")
            velocity = st.number_input("Velocity (m/s)", value=250)
            lift = 0.5 * 1.225 * (velocity**2) * 25 * 0.6
            st.metric("TOTAL LIFT", f"{round(lift, 2)} N", delta="STABLE")
            st.area_chart(np.random.randn(20, 2))
            
        else:
            st.write(f"Advanced engineering specs for {selected_mod} are loading...")
            st.progress(65)

    with col2:
        st.header("⚡ UNIT MONITOR")
        st.metric("O2 LEVELS", "98%", "NORMAL")
        st.metric("FUEL FLOW", "240 kg/h", "-2%")
        
        st.write("---")
        st.header("⚠️ FAILURE LOG")
        fail = st.selectbox("SIMULATE FAILURE:", ["Stall-alert", "Engine Heats", "Tail Damage"])
        
        if fail == "Stall-alert":
            st.error("SYMPTOMS: LOW AIRSPEED | ACTION: NOSE DOWN")
        elif fail == "Engine Heats":
            st.error("SYMPTOMS: HIGH EGT | ACTION: REDUCE THRUST")
        elif fail == "Tail Damage":
            st.error("SYMPTOMS: YAW INSTABILITY | ACTION: EMERGENCY LANDING")

# --- FOOTER ---
st.sidebar.write("---")
st.sidebar.caption("ENGINEER: MANETH SAVINDU")
st.sidebar.caption("VERSION: 4.0.1 PRO")