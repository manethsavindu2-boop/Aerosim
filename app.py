import streamlit as st
import pandas as pd
import numpy as np

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

# Navigation state initialization
if 'page' not in st.session_state:
    st.session_state.page = 'master'

# --- 2. DYNAMIC CSS FOR WALLPAPERS & BLACK FONTS ---
def set_bg(url, font_color="black"):
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@400;700&display=swap');
        
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('{url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        /* Heading style */
        .main-title {{
            font-family: 'Orbitron', sans-serif;
            color: #39FF14;
            text-align: center;
            text-shadow: 2px 2px 10px black;
            font-size: 55px;
        }}

        /* White transparent box for Black Fonts */
        .content-box {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 25px;
            border-radius: 15px;
            border: 3px solid #39FF14;
            color: black !important;
            font-family: 'JetBrains Mono', monospace;
            font-weight: bold;
        }}

        /* Force all text in widgets to black */
        p, span, label, .stMetric, [data-testid="stMetricValue"] {{
            color: black !important;
            font-weight: bold !important;
        }}
        
        .stButton>button {{
            background-color: #000000;
            color: #39FF14;
            border: 2px solid #39FF14;
            font-family: 'Orbitron', sans-serif;
            width: 100%;
            height: 50px;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (ISS WALLPAPER) ---
if st.session_state.page == 'master':
    # ISS Wallpaper
    set_bg("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072")
    
    st.markdown('<h1 class="main-title">🛰️ MASTER COMMAND</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="content-box">
            <h2 style="text-align: center; color: black;">SYSTEM INITIALIZATION</h2>
            <p><b>STATION:</b> INTERNATIONAL SPACE STATION (ISS)</p>
            <p><b>OBJECTIVE:</b> AEROSPACE DATA MANAGEMENT</p>
            <p>Welcome, Engineer. Access the flight dashboard for tactical analysis and module management.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("TAP TO ACCESS DASHBOARD"):
            st.session_state.page = 'dashboard'
            st.rerun()

# --- STEP 2: DASHBOARD (FIGHTER JET WALLPAPER) ---
elif st.session_state.page == 'dashboard':
    # Fighter Jet Wallpaper
    set_bg("https://images.unsplash.com/photo-1517976384346-3136801d605d?q=80&w=2036")
    
    st.sidebar.markdown("""
        <div style="background-color: black; padding: 10px; border-radius: 5px;">
            <h3 style="color: #39FF14;">🛠️ CORE CONTROL</h3>
        </div>
    """, unsafe_allow_html=True)
    
    if st.sidebar.button("RETURN TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

    st.markdown('<h1 class="main-title">✈️ TACTICAL DASHBOARD</h1>', unsafe_allow_html=True)
    
    # Module Selector
    st.sidebar.write("")
    selected_mod = st.sidebar.selectbox("SELECT MODULE (1-14)", [f"Module {i}" for i in range(1, 15)])
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="content-box">
            <h3>ANALYSIS: {selected_mod}</h3>
            <p>Processing propulsion and aerodynamic data flow for tactical aircraft.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.line_chart(np.random.randn(20, 1))

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.metric("AIRSPEED", "MACH 1.2", "NOMINAL")
        st.metric("ALTITUDE", "45,000 FT", "+200")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("")
        st.markdown(f"""
        <div style="background-color: black; color: #39FF14; padding: 10px; border-radius: 5px; text-align: center;">
            <b>VERSION 1.0</b><br>
            ENGINEER: MANETH SAVINDU
        </div>
        """, unsafe_allow_html=True)