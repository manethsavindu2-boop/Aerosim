import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# CSS මගින් එක් එක් පිටුවට අදාළ Wallpaper සහ Styles සැකසීම
def apply_page_style(bg_url, font_color="white"):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* සාමාන්‍ය අකුරු වර්ගය */
        * {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; color: {font_color} !important; }}
        
        .stButton>button {{
            background-color: rgba(255, 255, 255, 0.1);
            color: {font_color} !important;
            border: 2px solid {font_color};
            border-radius: 5px;
            font-weight: bold;
        }}
        
        .info-box {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            border: 1px solid {font_color};
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (ISS Wallpaper) ---
if st.session_state.page == 'master':
    # ISS Wallpaper
    apply_page_style("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "white")
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="info-box">
        <h3>PROJECT: AVIONIX SYSTEMS</h3>
        <p>This is an advanced aerospace engineering and flight safety simulation platform.</p>
        <p><b>Status:</b> Orbital Link Active (ISS Station)</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ACCESS DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (SR-71 BLACKBIRD) ---
elif st.session_state.page == 'dashboard':
    # SR-71 Blackbird Wallpaper
    apply_page_style("https://images.unsplash.com/photo-1518364538800-6bae3c2ea0f2", "#39FF14")
    st.title("🎛️ SYSTEM DASHBOARD")
    
    st.sidebar.markdown(f"""
    **Developer:** Savindu Maneth  
    **Version:** 1.0  
    **Project:** Avionix Stealth Suite
    """)
    
    st.markdown("""
    <div class="info-box">
        <p>High-altitude tactical monitoring and flight computer interface active.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Jet Engine Schematic (Project Plan)")
        # Engine schematic icon
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", width=150)
    with col2:
        if st.button("GO TO MODULES (1-14)"):
            st.session_state.page = 'modules'
            st.rerun()
    
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULE PAGES (FIGHTER JETS / BOEING) ---
elif st.session_state.page == 'modules':
    # Fighter Jet / Boeing Mix Wallpaper
    apply_page_style("https://images.unsplash.com/photo-1517976384346-3136801d605d", "white")
    st.title("📂 ENGINEERING MODULES")
    
    mod = st.selectbox("SELECT EASA MODULE", [f"Module {i}" for i in range(1, 15)])
    
    st.write(f"### {mod} Analysis Active")
    st.line_chart(np.random.randn(15, 1))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ENGINE FAILURE ANALYSIS"):
            st.session_state.page = 'failures'
            st.rerun()
    with col2:
        if st.button("GO TO DASHBOARD"):
            st.session_state.page = 'dashboard'
            st.rerun()

# --- STEP 4: SPECIAL FAILURE PAGE (AIRCRAFT CRASH) ---
elif st.session_state.page == 'failures':
    # Dark Emergency Wallpaper
    apply_page_style("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957", "#FF3131")
    st.title("⚠️ EMERGENCY & CRASH ANALYSIS")
    
    st.markdown("""
    <div class="info-box">
        <h3>REAL-LIFE FAILURE DESCRIPTION</h3>
        <p><b>Scenario:</b> Uncontrolled Engine Stall and Hydraulic Failure.</p>
        <p><b>Symptoms:</b> Rapid loss of altitude, unresponsive control surfaces, and fire warnings in Engine 2.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("ACTION PROTOCOL: WHAT TO DO?")
    st.write("1. **Level the Wings:** Immediately try to regain aerodynamic stability.")
    st.write("2. **Engine Restart:** If possible, attempt a relight or shut down the affected engine to prevent fire.")
    st.write("3. **Mayday Call:** Notify Air Traffic Control (ATC) of the emergency status.")
    st.write("4. **Glide Management:** Identify the nearest suitable landing strip or open field.")

    st.write("### CRASH SITE SIMULATION DATA")
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b3/Engine_failure.jpg", width=400)
    
    if st.button("BACK TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()

# --- STEP 5: OBJECTIVES & SERVICE (LAST PAGE) ---
elif st.session_state.page == 'last':
    # ISS or Global Connectivity Wallpaper
    apply_page_style("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "#00E5FF")
    st.title("🎯 PROJECT OBJECTIVES & SERVICES")
    
    st.markdown("""
    <div class="info-box">
        <h3>Our Objectives</h3>
        <ul>
            <li>To provide high-fidelity aerospace data visualizations.</li>
            <li>To enhance EASA Part 66 learning through simulation.</li>
            <li>To document critical flight safety protocols.</li>
        </ul>
        <h3>Our Service</h3>
        <p>We provide aerospace consultancy, simulation logic building, and tactical engineering data analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("RETURN TO MASTER CORE"):
        st.session_state.page = 'master'
        st.rerun()

# Sidebar button for Last Page
if st.sidebar.button("VIEW PROJECT OBJECTIVES"):
    st.session_state.page = 'last'
    st.rerun()