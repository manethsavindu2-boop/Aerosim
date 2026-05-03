import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් සහ වර්ණ සැකසීමේ CSS ශ්‍රිතය
def apply_final_design(bg_url, text_color="white"):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* ඉතා පිරිසිදු සාමාන්‍ය අකුරු (Normal Font) */
        * {{ 
            font-family: 'Segoe UI', Arial, sans-serif !important; 
            color: {text_color} !important; 
        }}
        .stButton>button {{
            background-color: rgba(255, 255, 255, 0.1);
            color: {text_color} !important;
            border: 2px solid {text_color};
            font-weight: bold;
            border-radius: 5px;
            width: 100%;
        }}
        .glass-card {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 25px;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (ISS) ---
if st.session_state.page == 'master':
    # ISS Wallpaper - Black Font (පැහැදිලිව පෙනෙන පරිදි)
    apply_final_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "black")
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: white;">PROJECT: AVIONIX SYSTEMS</h3>
        <p style="color: white;">A specialized platform for aerospace maintenance, simulation, and high-altitude technical data analysis.</p>
        <p style="color: white;"><b>Location:</b> ISS Orbital Node</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ACCESS DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (SR-71 BLACKBIRD) ---
elif st.session_state.page == 'dashboard':
    # SR-71 Blackbird Wallpaper - White Font
    apply_final_design("https://images.unsplash.com/photo-1518364538800-6bae3c2ea0f2", "white")
    st.title("🎛️ MISSION DASHBOARD")
    
    st.sidebar.markdown("""
    **DEVELOPER:** SAVINDU MANETH  
    **VERSION:** 1.0  
    **SYSTEM:** SR-71 STEALTH CORE
    """)

    st.write("### CORE ARCHITECTURE PLANS")
    
    # පින්තූර හතර (Jet Engine, Ladder, Aircraft, Flight Computer)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", caption="JET ENGINE", width=110)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3125/3125713.png", caption="LADDER SYSTEM", width=110)
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/723/723961.png", caption="AIRCRAFT MODEL", width=110)
    with col4:
        st.image("https://cdn-icons-png.flaticon.com/512/2014/2014521.png", caption="FLIGHT COMPUTER", width=110)

    st.write("---")
    if st.button("PROCEED TO MODULES (1-14)"):
        st.session_state.page = 'modules'
        st.rerun()
    
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULE PAGES (FIGHTER JET / BOEING) ---
elif st.session_state.page == 'modules':
    # Fighter Jet/Boeing Wallpaper - Light Cyan Font
    apply_final_design("https://images.unsplash.com/photo-1517976384346-3136801d605d", "#E0F7FA")
    st.title("📂 ENGINEERING MODULES")
    
    selected_mod = st.selectbox("CHOOSE EASA MODULE", [f"Module {i}" for i in range(1, 15)])
    st.write(f"### Analyzing data for {selected_mod}...")
    st.line_chart(np.random.randn(20, 1))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("VIEW CRASH ANALYSIS"):
            st.session_state.page = 'failures'
            st.rerun()
    with col2:
        if st.button("BACK TO DASHBOARD"):
            st.session_state.page = 'dashboard'
            st.rerun()

# --- STEP 4: FAILURE PAGE (CRASH DESCRIPTIONS) ---
elif st.session_state.page == 'failures':
    # Crash Site Wallpaper - Red Alert Font
    apply_final_design("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957", "#FFBABA")
    st.title("⚠️ EMERGENCY FAILURE ANALYSIS")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #FF3131;">CASE STUDY: TURBOFAN ENGINE STALL</h3>
        <p><b>Description:</b> Rapid engine surge leading to compressor stall and power fluctuation.</p>
        <p><b>Symptoms:</b> Visible fire from exhaust, loud popping, and airframe vibration.</p>
        <hr>
        <h4 style="color: #FF3131;">WHAT DO YOU DO?</h4>
        <ol>
            <li><b>Aviate:</b> Maintain aircraft control and airspeed.</li>
            <li><b>Throttle:</b> Move the affected engine's throttle to IDLE.</li>
            <li><b>Isolate:</b> Shut down the engine if symptoms persist.</li>
            <li><b>Land:</b> Initiate emergency descent and communicate with ATC.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("BACK TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()

# --- STEP 5: OBJECTIVES & SERVICE (LAST PAGE) ---
elif st.session_state.page == 'last':
    apply_final_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "#00E5FF")
    st.title("🎯 PROJECT OBJECTIVES & SERVICES")
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: white;">Our Objectives</h3>
        <p>1. Provide professional maintenance simulation tools.</p>
        <p>2. Educate on EASA Part 66 technical standards.</p>
        <p>3. Simulate real-world flight failure scenarios.</p>
        <hr>
        <h3 style="color: white;">Our Service</h3>
        <p>We offer technical flight consultancy, engine logic simulation, and aerospace data visualization.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("RETURN TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# Sidebar Shortcut for Last Page
if st.sidebar.button("VIEW PROJECT SUMMARY"):
    st.session_state.page = 'last'
    st.rerun()