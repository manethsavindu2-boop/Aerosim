import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURATION ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

# Navigation Logic
if 'page' not in st.session_state:
    st.session_state.page = 'step1'

# Global Styles (Coding font & Dynamic CSS)
def apply_styles(bg_url, text_color="#000000"):
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;700&display=swap');
        
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        * {{ font-family: 'Source Code Pro', monospace !important; color: {text_color} !important; }}
        
        .stButton>button {{
            background-color: rgba(0,0,0,0.8);
            color: #39FF14 !important;
            border: 2px solid #39FF14;
            border-radius: 0px;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (ISS) ---
if st.session_state.page == 'step1':
    apply_styles("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", "#000000")
    st.title("🛰️ AVIONIX MASTER CORE")
    st.write("---")
    st.write("PROJECT: AVIONIX SYSTEMS")
    st.write("DESCRIPTION: Advanced orbital maintenance and aerospace analysis platform.")
    if st.button("ACCESS DASHBOARD"):
        st.session_state.page = 'step2'
        st.rerun()

# --- STEP 2: DASHBOARD (SR-71 BLACKBIRD) ---
elif st.session_state.page == 'step2':
    apply_styles("https://images.pivtotal.com/6000/6002.jpg", "#39FF14") # Neon green for Blackbird
    st.title("🎛️ SYSTEM DASHBOARD")
    st.sidebar.write("### DEVELOPER: SAVINDU MANETH")
    st.sidebar.write("### VERSION: 1.0")
    st.sidebar.write("DESCRIPTION: High-altitude tactical monitoring and engineering suite.")
    
    st.write("### MISSION CONTROL")
    col1, col2 = st.columns(2)
    with col1:
        st.write("PLAN: Jet Engine Schematic")
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", width=100)
    with col2:
        if st.button("GO TO MODULES (1-14)"):
            st.session_state.page = 'step3'
            st.rerun()
    if st.button("MASTER PAGE"):
        st.session_state.page = 'step1'
        st.rerun()

# --- STEP 3: MODULE PAGES (FIGHTER JETS/BOEING) ---
elif st.session_state.page == 'step3':
    apply_styles("https://images.unsplash.com/photo-1517976384346-3136801d605d", "#FFFFFF")
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("CHOOSE MODULE", [f"Module {i}" for i in range(1, 15)])
    
    st.write(f"### {mod} Analysis Stream")
    st.line_chart(np.random.randn(10, 1))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("GO TO FAILURE ANALYSIS"):
            st.session_state.page = 'step4'
            st.rerun()
    with col2:
        if st.button("BACK TO DASHBOARD"):
            st.session_state.page = 'step2'
            st.rerun()

# --- STEP 4: ENGINE FAILURES (CRASH SITE/ENGINE) ---
elif st.session_state.page == 'step4':
    apply_styles("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957", "#FF3131") # Red for emergency
    st.title("⚠️ EMERGENCY PROTOCOLS")
    fail = st.selectbox("SELECT FAILURE TYPE", ["Stall-alert", "Engine Heat", "Tail Damage"])
    
    st.error(f"FAILURE DETECTED: {fail}")
    st.write("SYMPTOMS: Loss of lift, EGT increase, Yaw instability.")
    st.write("REMEDY: Execute manual backup system and initiate emergency descent.")
    
    st.write("### HISTORICAL DATA (CRASH ANALYSIS)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b3/Engine_failure.jpg", width=300)
    
    if st.button("PREVIOUS PAGE"):
        st.session_state.page = 'step3'
        st.rerun()

# --- STEP 5: OBJECTIVES & SERVICE ---
elif st.session_state.page == 'step5' or st.sidebar.button("ABOUT PROJECT"):
    apply_styles("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "#00E5FF")
    st.title("🎯 PROJECT OBJECTIVES")
    st.write("1. Provide accurate aerospace engineering data.")
    st.write("2. Simulate real-time flight failures.")
    st.write("3. Support EASA Part 66 training modules.")
    st.write("---")
    st.write("SERVICE: Orbital Support & Aerospace Consultancy.")
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'step1'
        st.rerun()

# Fixed bottom version
st.sidebar.write("---")
st.sidebar.caption("AVIONIX SYSTEMS V1.0 | MANETH SAVINDU")