import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් සහ වර්ණ සැකසීමේ ශ්‍රිතය
def apply_custom_design(bg_url, text_color="white", shadow=True):
    shadow_css = "text-shadow: 2px 2px 8px rgba(0,0,0,0.8);" if shadow else ""
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* Normal Professional Font Type */
        * {{ 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; 
            color: {text_color} !important; 
            {shadow_css}
        }}
        .stButton>button {{
            background-color: rgba(255, 255, 255, 0.1);
            color: {text_color} !important;
            border: 2px solid {text_color};
            font-weight: bold;
            border-radius: 5px;
        }}
        .glass-panel {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.2);
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (ISS Wallpaper) ---
if st.session_state.page == 'master':
    # ISS Wallpaper - Black Font (පැහැදිලිව පෙනීමට shadow සහිතව)
    apply_custom_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "black")
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color: white;">PROJECT: AVIONIX SYSTEMS</h3>
        <p style="color: white;">Advanced aerospace maintenance and simulation platform. Developed for high-precision technical analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ACCESS DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (SR-71 BLACKBIRD Wallpaper) ---
elif st.session_state.page == 'dashboard':
    # SR-71 Blackbird Wallpaper - White Font
    apply_custom_design("https://images.unsplash.com/photo-1518364538800-6bae3c2ea0f2", "white")
    st.title("🎛️ TACTICAL DASHBOARD")
    
    st.sidebar.markdown("""
    **ENGINEER:** SAVINDU MANETH  
    **VERSION:** 1.0  
    **STATUS:** STEALTH MODE ACTIVE
    """)

    st.write("### SYSTEM ARCHITECTURE PLANS")
    
    # පින්තූර හතර (Jet Engine, Ladder, Aircraft, Flight Computer)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", caption="JET ENGINE", width=120)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3125/3125713.png", caption="LADDER STRATEGY", width=120)
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/723/723961.png", caption="AIRCRAFT MODEL", width=120)
    with col4:
        st.image("https://cdn-icons-png.flaticon.com/512/2014/2014521.png", caption="FLIGHT COMPUTER", width=120)

    st.write("---")
    if st.button("GO TO MODULES (1-14)"):
        st.session_state.page = 'modules'
        st.rerun()
    
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULE PAGES (FIGHTER JETS / BOEING Wallpaper) ---
elif st.session_state.page == 'modules':
    # Fighter Jet/Boeing Wallpaper - Light Blue Font
    apply_custom_design("https://images.unsplash.com/photo-1517976384346-3136801d605d", "#E0F7FA")
    st.title("📂 ENGINEERING MODULES")
    
    mod = st.selectbox("SELECT EASA MODULE", [f"Module {i}" for i in range(1, 15)])
    st.write(f"### Current Stream: {mod}")
    st.line_chart(np.random.randn(20, 1))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("CRASH DESCRIPTION PAGE"):
            st.session_state.page = 'failures'
            st.rerun()
    with col2:
        if st.button("RETURN TO DASHBOARD"):
            st.session_state.page = 'dashboard'
            st.rerun()

# --- STEP 4: FAILURE PAGE (AIRCRAFT CRASH Descriptions) ---
elif st.session_state.page == 'failures':
    # Crash Site Wallpaper - Emergency Red Font
    apply_custom_design("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957", "#FFBABA")
    st.title("⚠️ EMERGENCY FAILURE ANALYSIS")
    
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color: #FF3131;">REAL-LIFE CRASH DESCRIPTION: ENGINE STALL</h3>
        <p>Scenario: Uncontrolled compressor stall in a turbofan engine due to high Angle of Attack (AoA).</p>
        <p><b>Symptoms:</b> Fluctuating RPM, loud explosive noises, and sudden loss of thrust.</p>
        <hr>
        <h4 style="color: #FF3131;">WHAT DO YOU DO?</h4>
        <ol>
            <li><b>Aviate:</b> Stabilize the aircraft's pitch.</li>
            <li><b>Thrust:</b> Retard the throttle of the affected engine to idle.</li>
            <li><b>Monitor:</b> Check exhaust gas temperature (EGT) for fire.</li>
            <li><b>Communicate:</b> Notify ATC of emergency landing requirements.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("BACK TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()

# --- STEP 5: OBJECTIVES & SERVICE (LAST PAGE) ---
elif st.session_state.page == 'last':
    # Final Tech Wallpaper - Cyan Font
    apply_custom_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "#00E5FF")
    st.title("🎯 PROJECT OBJECTIVES & SERVICES")
    
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color: white;">Our Mission</h3>
        <p>To digitize EASA Part 66 modules and provide interactive aerospace simulation tools.</p>
        <hr>
        <h3 style="color: white;">Our Service</h3>
        <p>Aerospace consultancy, flight data logic building, and maintenance software support.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# Sidebar button for Objectives
if st.sidebar.button("ABOUT PROJECT"):
    st.session_state.page = 'last'
    st.rerun()