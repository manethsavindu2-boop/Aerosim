import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURATION ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'step1'

# එක් එක් පිටුවට ගැලපෙන පරිදි Styles වෙනස් කරන Function එක
def apply_design(bg_url, font_color="black"):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* Font types set to clean professional style as requested */
        * {{ font-family: 'Arial', sans-serif !important; color: {font_color} !important; }}
        
        .stButton>button {{
            background-color: rgba(0,0,0,0.8);
            color: #39FF14 !important;
            border: 2px solid #39FF14;
            border-radius: 4px;
        }}
        .description-card {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            color: black !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (ISS) ---
if st.session_state.page == 'step1':
    apply_design("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", "black")
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="description-card">
        <h3>Our Project: Avionix Systems</h3>
        <p>This site is dedicated to aerospace engineering simulations and flight safety analysis.</p>
        <p><b>Note:</b> Access restricted to authorized personnel.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ACCESS DASHBOARD"):
        st.session_state.page = 'step2'
        st.rerun()

# --- STEP 2: DASHBOARD (SR-71 BLACKBIRD) ---
elif st.session_state.page == 'step2':
    apply_design("https://images.unsplash.com/photo-1518364538800-6bae3c2ea0f2", "white")
    st.title("🎛️ SYSTEM DASHBOARD")
    
    st.sidebar.write("### Developer: Savindu Maneth")
    st.sidebar.write("### Version: 1.0")
    st.sidebar.write("### Description: High-altitude tactical monitoring.")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### Aircraft Project Plans")
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", caption="Engine Logic", width=150)
        st.write("Plan: Jet Engine Ladder Strategy")
    with col2:
        if st.button("GO TO MODULES (1-14)"):
            st.session_state.page = 'step3'
            st.rerun()
    
    if st.button("BACK TO MASTER PAGE"):
        st.session_state.page = 'step1'
        st.rerun()

# --- STEP 3: MODULE PAGES (FIGHTER JETS / BOEING) ---
elif st.session_state.page == 'step3':
    apply_design("https://images.unsplash.com/photo-1517976384346-3136801d605d", "white")
    st.title("📂 AEROSPACE MODULES")
    
    selected_mod = st.selectbox("CHOOSE MODULE", [f"Module {i}" for i in range(1, 15)])
    st.write(f"Displaying technical data for {selected_mod}...")
    st.line_chart(np.random.randn(20, 1))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("VIEW CRASH DESCRIPTIONS"):
            st.session_state.page = 'step4'
            st.rerun()
    with col2:
        if st.button("BACK TO DASHBOARD"):
            st.session_state.page = 'step2'
            st.rerun()

# --- STEP 4: SPECIAL PAGE (ENGINE FAILURES & CRASHES) ---
elif st.session_state.page == 'step4':
    # Aircraft Crash Site Wallpaper
    apply_design("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957", "#FF3131")
    st.title("⚠️ CRASH ANALYSIS & ENGINE FAILURES")
    
    st.markdown("""
    <div class="description-card">
        <h3>Crash Description: Boeing 737 Engine Stall</h3>
        <p><b>Event:</b> During takeoff, Engine 1 experienced a severe compressor stall.</p>
        <p><b>Symptoms:</b> Loud banging noises, visible flames from exhaust, and loss of thrust.</p>
        <hr>
        <h4>What do you do? (Action Protocol)</h4>
        <ol>
            <li><b>Aviate:</b> Maintain control and airspeed.</li>
            <li><b>Identify:</b> Confirm which engine has failed using EGT and RPM gauges.</li>
            <li><b>Isolate:</b> Close fuel valves for the failed engine.</li>
            <li><b>Communicate:</b> Declare Emergency (Mayday) to ATC.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b3/Engine_failure.jpg", caption="Real-life Engine Failure Analysis", width=500)
    
    if st.button("BACK TO PREVIOUS PAGE"):
        st.session_state.page = 'step3'
        st.rerun()

# --- STEP 5: OBJECTIVES & SERVICE (LAST PAGE) ---
elif st.session_state.page == 'step5' or st.sidebar.button("VIEW OBJECTIVES"):
    apply_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", "#00E5FF")
    st.title("🎯 OUR OBJECTIVES & SERVICES")
    
    st.markdown("""
    <div class="description-card">
        <h3>Our Objectives</h3>
        <p>1. To provide professional-grade aerospace technical documentation.</p>
        <p>2. To assist EASA Part 66 students in understanding module complexities.</p>
        <p>3. To simulate emergency flight scenarios for better safety awareness.</p>
        <hr>
        <h3>Our Service</h3>
        <p>Providing simulation tools, technical flight computer logic, and aerospace consultancy services.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'step1'
        st.rerun()
        