import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් රූප සහ මෝස්තර සැකසීමේ ශ්‍රිතය (CSS Function)
def set_design(bg_url, text_color="white"):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* සාමාන්‍ය අකුරු වර්ගය - කොළ පැහැය භාවිතා කර නැත */
        * {{ 
            font-family: 'Segoe UI', Arial, sans-serif !important; 
            color: {text_color} !important; 
        }}
        
        .stButton>button {{
            background-color: rgba(255, 255, 255, 0.2);
            color: {text_color} !important;
            border: 2px solid {text_color};
            font-weight: bold;
            border-radius: 8px;
        }}
        
        .info-card {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 20px;
            border-radius: 12px;
            border: 1px solid {text_color};
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (ISS Wallpaper) ---
if st.session_state.page == 'master':
    # ISS Wallpaper - කළු අකුරු (Black fonts) ඔබ ඉල්ලූ පරිදි
    set_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "black")
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="info-card">
        <h3 style="color: black;">PROJECT: AVIONIX SYSTEMS</h3>
        <p style="color: black;">This is a high-performance aerospace maintenance simulation and engineering data platform.</p>
        <p style="color: black;"><b>Developed by:</b> Savindu Maneth</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ACCESS DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (SR-71 BLACKBIRD) ---
elif st.session_state.page == 'dashboard':
    # Blackbird Wallpaper - සුදු අකුරු සමඟ (කොළ නැත)
    set_design("https://images.unsplash.com/photo-1518364538800-6bae3c2ea0f2", "white")
    st.title("🎛️ SYSTEM DASHBOARD")
    
    st.sidebar.markdown(f"""
    **Developer:** Savindu Maneth  
    **Version:** 1.0  
    **Project:** Avionix Suite
    """)

    st.write("### TACTICAL SYSTEM PLANS")
    
    # පින්තූර හතර පෙන්වන ආකාරය (Jet Engine, Ladder, Aircraft, Flight Computer)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", caption="1. JET ENGINE PLAN", width=120)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3125/3125713.png", caption="2. LADDER STRATEGY", width=120)
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/723/723961.png", caption="3. AIRCRAFT MODEL", width=120)
    with col4:
        st.image("https://cdn-icons-png.flaticon.com/512/2014/2014521.png", caption="4. FLIGHT COMPUTER", width=120)

    st.write("---")
    if st.button("GO TO MODULES (1-14)"):
        st.session_state.page = 'modules'
        st.rerun()
    
    if st.button("BACK TO MASTER PAGE"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULE PAGES (FIGHTER JETS / BOEING) ---
elif st.session_state.page == 'modules':
    # Fighter Jet Wallpaper
    set_design("https://images.unsplash.com/photo-1517976384346-3136801d605d", "white")
    st.title("📂 AEROSPACE MODULES")
    
    selected_mod = st.selectbox("CHOOSE EASA MODULE", [f"Module {i}" for i in range(1, 15)])
    st.write(f"Technical Data Analysis for {selected_mod}...")
    st.line_chart(np.random.randn(20, 1))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("CRASH ANALYSIS PAGE"):
            st.session_state.page = 'failures'
            st.rerun()
    with col2:
        if st.button("RETURN TO DASHBOARD"):
            st.session_state.page = 'dashboard'
            st.rerun()

# --- STEP 4: FAILURE PAGE (AIRCRAFT CRASH DESCRIPTIONS) ---
elif st.session_state.page == 'failures':
    # Emergency Wallpaper - තද අළු/රතු පැහැති පෙනුම
    set_design("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957", "#FFBABA")
    st.title("⚠️ EMERGENCY & CRASH ANALYSIS")
    
    st.markdown("""
    <div class="info-card">
        <h3>SCENARIO: BOEING 737 ENGINE FAILURE</h3>
        <p><b>Description:</b> Engine 2 experienced a sudden compressor stall during cruise.</p>
        <p><b>Symptoms:</b> Airframe vibration, exhaust gas temp increase, and power loss.</p>
        <hr>
        <h4>WHAT DO YOU DO?</h4>
        <ol>
            <li>Identify the failed engine using N1 and N2 gauges.</li>
            <li>Cut fuel supply to the affected engine to prevent fire.</li>
            <li>Initiate drift-down procedure to a safe altitude.</li>
            <li>Declare emergency and divert to the nearest airfield.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("BACK TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()

# --- STEP 5: OBJECTIVES & SERVICE (LAST PAGE) ---
elif st.session_state.page == 'last':
    # Global Tech Wallpaper
    set_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "#E0F7FA")
    st.title("🎯 PROJECT OBJECTIVES & SERVICES")
    
    st.markdown("""
    <div class="info-card">
        <h3>Our Objectives</h3>
        <p>1. Provide professional maintenance simulation data.</p>
        <p>2. Document aircraft crash scenarios for safety training.</p>
        <p>3. Assist in EASA Part 66 module preparations.</p>
        <hr>
        <h3>Our Service</h3>
        <p>We offer technical consultancy, flight system logic, and simulation support.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("BACK TO MASTER CORE"):
        st.session_state.page = 'master'
        st.rerun()

# Sidebar button for Objectives
if st.sidebar.button("VIEW PROJECT GOALS"):
    st.session_state.page = 'last'
    st.rerun()