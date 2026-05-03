import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් සහ සුදු වර්ණ අකුරු සැකසීමේ ශ්‍රිතය
def apply_avionix_design(bg_url, overlay_opacity=0.5):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,{overlay_opacity}), rgba(0,0,0,{overlay_opacity})), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* සියලුම අකුරු සුදු පැහැයෙන් */
        * {{ 
            font-family: 'Segoe UI', Arial, sans-serif !important; 
            color: white !important; 
            text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
        }}
        .stButton>button {{
            background-color: rgba(255, 255, 255, 0.15);
            color: white !important;
            border: 2px solid white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }}
        .status-box {{
            background-color: rgba(0, 255, 0, 0.1);
            border: 1px solid #00FF00;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }}
        .info-panel {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.2);
            margin-bottom: 25px;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE ---
if st.session_state.page == 'master':
    apply_avionix_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", overlay_opacity=0.2)
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="info-panel">
        <h1 style="font-size: 45px;">WELCOME TO AVIONIX SYSTEMS</h1>
        <p style="font-size: 20px;">The next generation of aerospace maintenance and technical simulation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ENTER MISSION CONTROL"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD ---
elif st.session_state.page == 'dashboard':
    apply_avionix_design("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", overlay_opacity=0.6)
    
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.title("🎛️ MISSION CONTROL DASHBOARD")
    with col_t2:
        st.markdown("""<div class="status-box"><span style='color: #00FF00;'>● SERVER STATUS: ONLINE</span><br><small>LATENCY: 24ms</small></div>""", unsafe_allow_html=True)

    st.write("---")
    st.markdown('<div class="info-panel">', unsafe_allow_html=True)
    st.header("📘 EASA PART 66 & OBJECTIVES")
    st.subheader("[ENGLISH]")
    st.write("EASA Part 66 is the common European standard for aircraft maintenance personnel.")
    st.write("---")
    st.subheader("🎯 CORE MISSIONS")
    st.write("* **Innovation:** Pioneering new ways to learn aerospace modules.")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("PROCEED TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()
    
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULES PAGE (DARK AIRLINE WALLPAPER) ---
elif st.session_state.page == 'modules':
    # මෙහිදී සියලුම Module පිටු සඳහා Dark Airline Wallpaper එකක් යොදා ඇත
    dark_airline_url = "https://images.unsplash.com/photo-1559156102-60adff591fc9?q=80&w=2070&auto=format&fit=crop"
    apply_avionix_design(dark_airline_url, overlay_opacity=0.7)
    
    st.title("📂 ENGINEERING MODULES")
    
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    st.markdown(f"""
    <div class="info-panel">
        <h2>{mod} - Technical Analysis</h2>
        <p>Currently displaying maintenance parameters and system telemetry for {mod}.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.line_chart(np.random.randn(20, 1))
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()