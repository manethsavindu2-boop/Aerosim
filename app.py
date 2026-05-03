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
        .large-desc {{
            font-size: 20px !important;
            line-height: 1.6;
            margin-bottom: 20px;
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
    with col_t1:
        st.title("🎛️ MISSION CONTROL DASHBOARD")
    with col_t2:
        st.markdown("""<div class="status-box"><span style='color: #00FF00;'>● SERVER STATUS: ONLINE</span><br><small>LATENCY: 24ms</small></div>""", unsafe_allow_html=True)
    st.write("---")
    st.markdown('<div class="info-panel">', unsafe_allow_html=True)
    st.header("📘 EASA PART 66 & GLOBAL OBJECTIVES")
    st.markdown("""<div class="large-desc"><b>[ENGLISH]</b><br>EASA Part 66 is the common European standard for aircraft maintenance personnel... (English/German/French/Russian/Japanese/Chinese Text)</div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("PROCEED TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULES PAGE (MODULE 1 THEORY ADDED) ---
elif st.session_state.page == 'modules':
    # Module 2 හි තිබූ එම Wallpaper එකම මෙහිදී ස්ථාවරව භාවිතා කර ඇත
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS (EASA PART 66)")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("💡 Key Theory Facts")
            st.write("""
            * **Arithmetic:** Basic operations, fractions, decimals, and percentages.
            * **Algebra:** Linear equations, indices, and powers ($10^n$).
            * **Geometry:** Calculation of Area (Circle: $\pi r^2$, Triangle: $1/2 bh$) and Volume (Cylinder: $\pi r^2 h$).
            * **Trigonometry:** Sine, Cosine, and Tangent rules for structural analysis.
            """)
        
        with col2:
            st.subheader("⚙️ Technical Calculations")
            # Converter Tool
            inch_val = st.number_input("Unit Conversion (Inches to mm):", value=1.0)
            st.write(f"Result: **{inch_val * 25.4:.2f} mm**")
            
            # Area Tool
            rad_val = st.number_input("Cylinder Piston Area (Radius in cm):", value=0.0)
            st.write(f"Area: **{3.14159 * (rad_val**2):.2f} cm²**")
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3>', unsafe_allow_html=True)
        st.line_chart(np.random.randn(20, 1))
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()