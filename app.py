import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURATION & THEME ---
st.set_page_config(page_title="Avionix Systems Pro", layout="wide", initial_sidebar_state="expanded")

# Coding type font and Dark Aviation Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;700&display=swap');
    
    * { font-family: 'Source Code Pro', monospace !important; }
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url('https://images.unsplash.com/photo-1559297434-2d8a134e042e');
        background-size: cover;
        color: #00FF41; /* Matrix Green */
    }
    .stButton>button {
        width: 100%;
        background-color: #1a1a1a;
        color: #00FF41;
        border: 1px solid #00FF41;
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
    st.title("🛰️ AVIONIX SYSTEMS")
    st.subheader("Next-Gen Aerospace Engineering Interface")
    st.write("Welcome to the core system. Prepare for EASA Part 66 Analysis.")
    
    if st.button("ENTER DASHBOARD"):
        change_page('dashboard')

# --- 2. DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.sidebar.title("🎛️ CONTROL CENTER")
    if st.sidebar.button("Home"): change_page('landing')
    
    st.title("✈️ ENGINEERING DASHBOARD")
    st.write("Select a module to begin technical calculations.")
    
    # Module Selection
    selected_mod = st.sidebar.selectbox("EASA PART 66 MODULES", 
                                       [f"Module {i}" for i in range(1, 15)])
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header(f"Analysis: {selected_mod}")
        
        if selected_mod == "Module 1":
            st.write("### Mathematics & Calculations")
            num1 = st.number_input("Input Data A", value=100)
            num2 = st.number_input("Input Data B", value=50)
            res = num1 * np.sin(num2)
            st.line_chart(np.random.randn(20, 2))
            st.success(f"Resultant Vector: {round(res, 4)}")
            
        elif selected_mod == "Module 2":
            st.write("### Physics & Propulsion")
            mass = st.slider("Aircraft Mass (kg)", 1000, 50000, 15000)
            force = mass * 9.81
            st.bar_chart(np.random.rand(10))
            st.info(f"Gravitational Force: {force} N")
            
        else:
            st.write(f"Advanced data visualization for {selected_mod} in progress...")
            st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", width=100) # Small 3D-like Aircraft icon

    with col2:
        st.header("System Status")
        st.metric("Core Temp", "42°C", "1.2°C")
        st.metric("Sync Status", "Online", "Secure")
        
        st.write("---")
        st.header("⚠️ EMERGENCY LOGS")
        fail = st.selectbox("Simulate Failure:", ["Stall-alert", "Engine Heats", "Tail Damage"])
        
        if fail == "Stall-alert":
            st.error("**SYMPTOMS:** Rapid airspeed drop, high AOA.")
            st.warning("**ACTION:** Push nose down, increase thrust.")
        elif fail == "Engine Heats":
            st.error("**SYMPTOMS:** High EGT, fire warning.")
            st.warning("**ACTION:** Retard throttle, activate extinguishers.")
        elif fail == "Tail Damage":
            st.error("**SYMPTOMS:** Unresponsive pitch/yaw.")
            st.warning("**ACTION:** Use differential thrust, emergency landing.")

# --- FOOTER ---
st.sidebar.write("---")
st.sidebar.caption("System: Avionix Pro v3.0")
st.sidebar.caption("Engineer: Maneth Savindu")