import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් සහ සුදු වර්ණ අකුරු සැකසීමේ ශ්‍රිතය
def apply_avionix_design(bg_url, overlay_opacity=0.3):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,{overlay_opacity}), rgba(0,0,0,{overlay_opacity})), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* සියලුම අකුරු සුදු පැහැයෙන් (Strong White Font) */
        * {{ 
            font-family: 'Segoe UI', Arial, sans-serif !important; 
            color: white !important; 
            text-shadow: 2px 2px 12px rgba(0,0,0,1);
        }}
        .stButton>button {{
            background-color: rgba(255, 255, 255, 0.2);
            color: white !important;
            border: 2px solid white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }}
        .glass-panel {{
            background-color: rgba(0, 0, 0, 0.5); /* Master Page එකේදී වැඩි දීප්තියක් සඳහා */
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.3);
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (LIGHT VERSION) ---
if st.session_state.page == 'master':
    # මෙහි overlay_opacity 0.2 ලෙස අඩු කර ඇත (වඩා දීප්තිමත් කිරීමට)
    apply_avionix_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", overlay_opacity=0.2)
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="glass-panel">
        <h1 style="color: white; font-size: 40px;">WELCOME TO AVIONIX SYSTEMS</h1>
        <p style="font-size: 20px;">The next generation of aerospace maintenance and technical simulation.</p>
        <hr style="border: 1px solid white;">
        <p>Current Status: <b>SYSTEMS ONLINE / LIGHT MODE ACTIVE</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("PROCEED TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (SR-71 BLACKBIRD - image_5d947e.png) ---
elif st.session_state.page == 'dashboard':
    # SR-71 Blackbird Wallpaper (image_5d947e.png)
    apply_avionix_design("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6f9Y98nOn9R1M9K_u9O2H8Y8O-Y6Fm9M2Gg&s", overlay_opacity=0.5)
    st.title("🎛️ MISSION DASHBOARD")
    
    st.sidebar.markdown("### MISSION LOGS\n- SR-71 STEALTH ACTIVE\n- ALL SYSTEMS NOMINAL")

    st.write("### SYSTEM ARCHITECTURE")
    
    # පින්තූර 4 (Jet Engine, Ladder, Aircraft, Flight Computer)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", caption="JET ENGINE", width=120)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3125/3125713.png", caption="LADDER SYSTEM", width=120)
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/723/723961.png", caption="AIRCRAFT DATA", width=120)
    with col4:
        st.image("https://cdn-icons-png.flaticon.com/512/2014/2014521.png", caption="FLIGHT COMPUTER", width=120)

    st.write("---")
    if st.button("ENGINEERING MODULES"):
        st.session_state.page = 'modules'
        st.rerun()
    
    if st.button("RESET TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULES PAGE ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images.unsplash.com/photo-1517976384346-3136801d605d")
    st.title("📂 ENGINEERING MODULES")
    
    mod = st.selectbox("CHOOSE MODULE", [f"Module {i}" for i in range(1, 15)])
    st.write(f"### Analyzing {mod} Data...")
    st.line_chart(np.random.randn(20, 1))
    
    if st.button("BACK TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()