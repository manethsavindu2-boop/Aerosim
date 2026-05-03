import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් සහ සුදු වර්ණ අකුරු සැකසීමේ ශ්‍රිතය
def apply_avionix_design(bg_url):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* සියලුම අකුරු සුදු පැහැයෙන් (White Font) */
        * {{ 
            font-family: 'Segoe UI', Arial, sans-serif !important; 
            color: white !important; 
            text-shadow: 2px 2px 10px rgba(0,0,0,1);
        }}
        .stButton>button {{
            background-color: rgba(255, 255, 255, 0.1);
            color: white !important;
            border: 2px solid white;
            font-weight: bold;
            border-radius: 8px;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background-color: rgba(255, 255, 255, 0.3);
            border-color: #00E5FF;
        }}
        .glass-panel {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        /* Sidebar සැකසුම් */
        [data-testid="stSidebar"] {{
            background-color: rgba(0, 0, 0, 0.8);
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (ISS) ---
if st.session_state.page == 'master':
    apply_avionix_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa")
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="glass-panel">
        <h2 style="color: white;">AVIONIX SYSTEMS v1.0</h2>
        <p>Advanced aerospace maintenance simulation and engineering data hub.</p>
        <p>Current Status: <b>Ready for Takeoff</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ENTER MISSION CONTROL"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (YOUR SR-71 BLACKBIRD IMAGE) ---
elif st.session_state.page == 'dashboard':
    # මෙහිදී ඔබ ලබාදුන් පින්තූරය පසුබිමට එක් කර ඇත
    apply_avionix_design("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6f9Y98nOn9R1M9K_u9O2H8Y8O-Y6Fm9M2Gg&s")
    st.title("🎛️ MISSION DASHBOARD")
    
    st.sidebar.markdown("""
    ### ENGINEER PROFILE
    - **NAME:** SAVINDU MANETH
    - **AIRCRAFT:** SR-71 BLACKBIRD
    - **AUTH:** LEVEL 5 CLEARANCE
    """)

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
    if st.button("OPEN ENGINEERING MODULES"):
        st.session_state.page = 'modules'
        st.rerun()
    
    if st.button("BACK TO HOME"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULES PAGE ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images.unsplash.com/photo-1517976384346-3136801d605d")
    st.title("📂 EASA PART 66 MODULES")
    
    mod = st.selectbox("CHOOSE MODULE", [f"Module {i}" for i in range(1, 15)])
    st.write(f"### Loading Data for {mod}...")
    st.line_chart(np.random.randn(25, 2))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("CRASH LOGS"):
            st.session_state.page = 'failures'
            st.rerun()
    with col2:
        if st.button("DASHBOARD"):
            st.session_state.page = 'dashboard'
            st.rerun()

# --- STEP 4: FAILURE PAGE ---
elif st.session_state.page == 'failures':
    apply_avionix_design("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957")
    st.title("⚠️ EMERGENCY PROTOCOLS")
    
    st.markdown("""
    <div class="glass-panel">
        <h3 style="color: #FF5252;">AIRCRAFT FAILURE: ENGINE STALL</h3>
        <p>Description: Loss of airflow through the compressor blades resulting in explosive surges.</p>
        <hr>
        <h4>PROCEDURES:</h4>
        <ul>
            <li>Maintain Speed: Keep the nose down to prevent secondary stall.</li>
            <li>Power Control: Reduce throttle to idle on the failed unit.</li>
            <li>Relight: Attempt restart if altitude permits.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("BACK TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()

# --- STEP 5: OBJECTIVES PAGE ---
elif st.session_state.page == 'last':
    apply_avionix_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa")
    st.title("🎯 MISSION OBJECTIVES")
    
    st.markdown("""
    <div class="glass-panel">
        <h3>Primary Goals</h3>
        <p>1. Advanced simulation of EASA technical modules.</p>
        <p>2. Real-time flight logic visualization for trainee engineers.</p>
        <hr>
        <h3>Services</h3>
        <p>Full-stack aerospace consultancy and simulation design.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("MASTER RESET"):
        st.session_state.page = 'master'
        st.rerun()

# Sidebar summary button
if st.sidebar.button("QUICK SUMMARY"):
    st.session_state.page = 'last'
    st.rerun()