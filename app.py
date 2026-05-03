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
    st.markdown('<div class="info-panel"><h2>📘 EASA PART 66 GLOBAL STANDARDS</h2><p>Our objective is to provide high-level technical simulation to bridge the gap between theory and practical engineering excellence.</p></div>', unsafe_allow_html=True)
    if st.button("PROCEED TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()

# --- STEP 3: MODULES PAGE (MODULE 1 COMPLETE THEORY & CALCULATIONS) ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS")
        
        # --- THEORY SECTION ---
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.subheader("📝 Arithmetic & Algebra Theory")
            st.write("""
            * **Order of Ops (BODMAS):** Bracket, Of, Division, Multiplication, Addition, Subtraction.
            * **Powers of 10:** Used for Scientific Notation ($3.2 \\times 10^5$).
            * **Logarithms:** Inverse of indices. If $10^2 = 100$, then $\\log_{10}(100) = 2$.
            * **Binary System:** Base-2 system (0 and 1) used in digital aircraft computers.
            """)
        
        with t_col2:
            st.subheader("📐 Geometry & Trigonometry")
            st.write("""
            * **Pythagoras Theorem:** $a^2 + b^2 = c^2$ (Used for structural stress analysis).
            * **Circle Geometry:** Circumference = $2\\pi r$, Area = $\\pi r^2$.
            * **Trig Ratios:** $\\sin \\theta = O/H$, $\\cos \\theta = A/H$, $\\tan \\theta = O/A$.
            * **Volumes:** Cylinder = $\\pi r^2 h$, Sphere = $\\frac{4}{3} \\pi r^3$.
            """)

        st.write("---")
        
        # --- CALCULATIONS SECTION ---
        st.subheader("⚙️ Interactive Engineering Tools")
        calc_col1, calc_col2 = st.columns(2)
        
        with calc_col1:
            st.markdown("#### 📏 Unit Converter")
            val = st.number_input("Input Value:", value=1.0)
            unit_op = st.selectbox("Convert From:", ["Inches to mm", "Gallons to Liters", "PSI to Bar"])
            if unit_op == "Inches to mm": res = val * 25.4
            elif unit_op == "Gallons to Liters": res = val * 3.785
            else: res = val * 0.0689
            st.success(f"Output: **{res:.2f}**")

        with calc_col2:
            st.markdown("#### 📐 Pythagoras Calculator")
            side_a = st.number_input("Side A length:", value=3.0)
            side_b = st.number_input("Side B length:", value=4.0)
            hypo = np.sqrt(side_a**2 + side_b**2)
            st.info(f"Hypotenuse (C): **{hypo:.2f}**")

        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3></div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()