import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURATION & THEME ---
st.set_page_config(page_title="Avionix Systems Pro", layout="wide", initial_sidebar_state="expanded")

# Aviation Wallpaper එක සහ ගැලපෙන වර්ණ සැකසීම
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
    
    /* Aviation / Cockpit Wallpaper */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Professional Font Styles */
    h1, h2, h3 { 
        font-family: 'Orbitron', sans-serif !important; 
        color: #00f2ff !important; /* Aero Cyan */
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    p, span, div, label { 
        font-family: 'JetBrains Mono', monospace !important; 
        color: #ffffff !important; 
        font-weight: 400;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(6, 12, 24, 0.95) !important;
        border-right: 1px solid #00f2ff;
    }

    /* Control Inputs */
    .stSlider, .stNumberInput, .stSelectbox {
        background: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 8px;
    }

    /* Tech Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #001f3f, #0074d9);
        color: white;
        border: 1px solid #00f2ff;
        border-radius: 2px;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
        height: 3em;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background: #00f2ff;
        color: black;
        box-shadow: 0px 0px 15px #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def change_page(page_name):
    st.session_state.page = page_name

# --- 1. OPENING PAGE (AVIATION LANDING) ---
if st.session_state.page == 'landing':
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("🛩️ AVIONIX SYSTEMS")
    st.subheader("AVIATION MAINTENANCE & ENGINEERING INTERFACE")
    
    st.write("""
    ### SYSTEMS STATUS: ONLINE
    Authorized access for Aircraft Engineers and EASA Part 66 Students only.
    """)
    
    if st.button("INITIALIZE DASHBOARD"):
        change_page('dashboard')

# --- 2. DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.sidebar.title("🎛️ FLIGHT COMPUTER")
    if st.sidebar.button("EXIT SYSTEM"): change_page('landing')
    
    st.title("✈️ CONTROL DASHBOARD")
    st.write("Professional analysis for aerospace calculations.")
    st.write("---")

    # Module Selection (1 to 14)
    selected_mod = st.sidebar.selectbox("SELECT EASA MODULE", [f"Module {i}" for i in range(1, 15)])
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header(f"ANALYSIS: {selected_mod}")
        
        # Calculations according to user's plan
        if selected_mod == "Module 1":
            st.subheader("Mathematics Data Stream")
            num = st.slider("Select Frequency Level", 0, 1000, 500)
            st.line_chart(np.random.randn(20, 1))
            st.info(f"Vector Resultant: {num * 0.88} (Calculated)")

        elif selected_mod == "Module 8":
            st.subheader("Aerodynamics Performance")
            vel = st.number_input("Input Velocity (knots)", value=200)
            lift = 0.5 * 1.225 * (vel**2) * 25 * 0.4
            st.metric("REAL-TIME LIFT", f"{round(lift, 2)} N")
            st.area_chart(np.random.randn(20, 1))

        else:
            st.write(f"Technical interface for {selected_mod} is being populated...")
            st.progress(40)
            # Small placeholder for aircraft visualization
            st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", width=80)

    with col2:
        st.header("⚙️ SYSTEM MONITOR")
        st.metric("OIL PRESSURE", "85 PSI", "STABLE")
        st.metric("EGT", "640 °C", "+5°C")
        
        st.write("---")
        st.header("⚠️ EMERGENCY")
        fail = st.selectbox("SIMULATE FAILURE:", ["Stall-alert", "Engine Heats", "Tail Damage"])
        
        if fail == "Stall-alert":
            st.error("SYMPTOMS: LOW SPEED / HIGH AOA")
            st.warning("ACTION: NOSE DOWN / FULL THRUST")
        elif fail == "Engine Heats":
            st.error("SYMPTOMS: HIGH EGT WARNING")
            st.warning("ACTION: REDUCE POWER / MONITOR TEMP")
        elif fail == "Tail Damage":
            st.error("SYMPTOMS: LOSS OF CONTROL")
            st.warning("ACTION: USE DIFFERENTIAL THRUST")

# --- FOOTER ---
st.sidebar.write("---")
st.sidebar.caption("ENGINEER: MANETH SAVINDU")
st.sidebar.caption("SYSTEM: AVIONIX v4.2")