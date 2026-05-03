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
    st.markdown("""<div class="large-desc"><b>[ENGLISH]</b><br>EASA Part 66 is the common European standard for aircraft maintenance personnel...</div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("PROCEED TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULES PAGE (ALL MODULE 1 CALCULATIONS ADDED) ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS (EASA PART 66)")
        
        # --- Section 1: Theory ---
        st.subheader("💡 Core Theory Recap")
        st.write("Fundamental mathematical principles used in aviation engineering including Binary/Hexadecimal systems, Powers, and Logarithms.")
        
        # --- Section 2: Calculations Tools ---
        st.write("---")
        st.subheader("⚙️ Essential Aerospace Calculations")
        
        calc_col1, calc_col2 = st.columns(2)
        
        with calc_col1:
            # 1. Unit Converter (Imperial to Metric)
            st.markdown("#### 📏 Unit Conversion")
            option = st.selectbox("Type", ["Inches to mm", "Feet to Meters", "US Gallons to Liters", "Pounds (lb) to Kilograms (kg)"])
            val = st.number_input("Value to convert:", value=1.0, key="unit_val")
            if option == "Inches to mm": res = val * 25.4
            elif option == "Feet to Meters": res = val * 0.3048
            elif option == "US Gallons to Liters": res = val * 3.78541
            else: res = val * 0.453592
            st.success(f"Result: **{res:.4f}**")

            # 2. Aspect Ratio (Wing Design)
            st.markdown("#### ✈️ Wing Aspect Ratio")
            span = st.number_input("Wing Span (m):", value=10.0)
            area_w = st.number_input("Wing Area (m²):", value=15.0)
            ar = (span**2) / area_w if area_w > 0 else 0
            st.info(f"Aspect Ratio: **{ar:.2f}**")

        with calc_col2:
            # 3. Geometry: Volume of Cylinder (Fuel/Hydraulic Tanks)
            st.markdown("#### 🛢️ Cylinder Volume")
            radius = st.number_input("Radius (cm):", value=5.0)
            height = st.number_input("Height/Length (cm):", value=20.0)
            vol = 3.14159 * (radius**2) * height
            st.info(f"Total Volume: **{vol:.2f} cm³**")

            # 4. Compression Ratio (Engine Mathematics)
            st.markdown("#### 🏎️ Engine Compression Ratio")
            swept_vol = st.number_input("Swept Volume (V_s):", value=500.0)
            clear_vol = st.number_input("Clearance Volume (V_c):", value=50.0)
            cr = (swept_vol + clear_vol) / clear_vol if clear_vol > 0 else 0
            st.warning(f"Compression Ratio: **{cr:.1f} : 1**")

        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3>', unsafe_allow_html=True)
        st.line_chart(np.random.randn(20, 1))
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()