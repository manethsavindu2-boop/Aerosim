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
    st.markdown('<div class="info-panel"><h1 style="font-size: 45px;">WELCOME TO AVIONIX SYSTEMS</h1><p style="font-size: 20px;">The next generation of aerospace maintenance and technical simulation.</p></div>', unsafe_allow_html=True)
    if st.button("ENTER MISSION CONTROL"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD ---
elif st.session_state.page == 'dashboard':
    apply_avionix_design("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", overlay_opacity=0.6)
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1: st.title("🎛️ MISSION CONTROL DASHBOARD")
    with col_t2: st.markdown("""<div class="status-box"><span style='color: #00FF00;'>● SERVER STATUS: ONLINE</span><br><small>LATENCY: 24ms</small></div>""", unsafe_allow_html=True)
    st.write("---")
    st.markdown('<div class="info-panel"><h2>📘 EASA PART 66 GLOBAL STANDARDS</h2><p>Providing high-level technical simulation to bridge the gap between theory and practical engineering excellence.</p></div>', unsafe_allow_html=True)
    if st.button("PROCEED TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()

# --- STEP 3: MODULES PAGE ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS (EASA PART 66)")
        
        # --- THEORY SECTION ---
        st.subheader("📝 Key Theory Facts")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.markdown("#### ⚙️ Engine Compression Ratio Theory")
            st.write("""
            * **Definition:** The ratio of the maximum volume of the combustion chamber to its minimum volume.
            * **Formula:** $CR = \\frac{V_s + V_c}{V_c}$
            * *Where:* $V_s$ = Swept Volume, $V_c$ = Clearance Volume.
            * Higher ratios typically improve thermal efficiency but require high-octane fuel.
            """)
        
        with t_col2:
            st.markdown("#### 📐 Circle & Radius Theory")
            st.write("""
            * **Radius ($r$):** The distance from the center to any point on the circle.
            * **Diameter ($d$):** $2 \\times r$.
            * **Area:** $\\pi r^2$ (Used for piston area and hydraulic pressure calculations).
            * **Circumference:** $2\\pi r$.
            """)

        st.write("---")
        
        # --- CALCULATIONS SECTION ---
        st.subheader("⚙️ Essential Engineering Calculations")
        calc_col1, calc_col2 = st.columns(2)
        
        with calc_col1:
            st.markdown("#### 🏎️ Engine Compression Ratio Calc")
            v_swept = st.number_input("Swept Volume ($V_s$ in cc):", value=500.0)
            v_clear = st.number_input("Clearance Volume ($V_c$ in cc):", value=50.0)
            cr_result = (v_swept + v_clear) / v_clear if v_clear > 0 else 0
            st.success(f"Compression Ratio: **{cr_result:.1f} : 1**")

        with calc_col2:
            st.markdown("#### ⭕ Circle Properties (Based on Radius)")
            radius_in = st.number_input("Input Radius ($r$ in cm):", value=5.0)
            c_area = 3.14159 * (radius_in**2)
            c_circum = 2 * 3.14159 * radius_in
            st.info(f"Area: **{c_area:.2f} cm²**  \nCircumference: **{c_circum:.2f} cm**")

        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3></div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()