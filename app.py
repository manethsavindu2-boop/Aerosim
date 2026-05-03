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

# --- STEP 3: MODULES PAGE (ALL CALCULATIONS & THEORY) ---
elif st.session_state.page == 'modules':
    # Module 2 wallpaper used as fixed background for modules
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS")
        
        # --- THEORY SECTION ---
        st.subheader("📚 Important Theory Facts")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.markdown("#### ⚙️ Arithmetic & Algebra")
            st.write("""
            * **BODMAS:** The sequence for solving expressions (Brackets, Orders, Division, Multiplication, Addition, Subtraction).
            * **Indices & Powers:** Rules for $a^m \\times a^n = a^{m+n}$ and $(a^m)^n = a^{mn}$.
            * **Compression Ratio:** Fundamental for thermal efficiency; higher ratios require better fuels to prevent 'knocking'.
            """)
        
        with t_col2:
            st.markdown("#### 📐 Geometry & Trigonometry")
            st.write("""
            * **Pythagoras Theorem:** $a^2 + b^2 = c^2$. Essential for finding lengths in airframe structures.
            * **Radius Properties:** The radius is used to calculate Piston Area, Cylinder Volume, and Hydraulic force.
            * **Trigonometry:** SOH-CAH-TOA rules apply to lift and drag vector analysis.
            """)

        st.write("---")
        
        # --- CALCULATIONS SECTION ---
        st.subheader("⚙️ Essential Aerospace Calculations")
        
        # Row 1: Compression Ratio and Unit Conversion
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 🏎️ Engine Compression Ratio")
            vs = st.number_input("Swept Volume ($V_s$ in cc):", value=500.0)
            vc = st.number_input("Clearance Volume ($V_c$ in cc):", value=50.0)
            st.info(f"Compression Ratio: **{(vs + vc) / vc if vc > 0 else 0:.1f} : 1**")
        with c2:
            st.markdown("#### 📏 Imperial to Metric Converter")
            val = st.number_input("Value:", value=1.0)
            unit = st.selectbox("Convert:", ["Inches to mm", "Gallons to Liters", "Feet to Meters"])
            if "Inches" in unit: res = val * 25.4
            elif "Gallons" in unit: res = val * 3.785
            else: res = val * 0.3048
            st.success(f"Converted Value: **{res:.2f}**")

        # Row 2: Radius-based Geometry and Pythagoras
        st.write("---")
        c3, c4 = st.columns(2)
        with c3:
            st.markdown("#### ⭕ Circle Properties (Radius Based)")
            rad = st.number_input("Input Radius ($r$ in cm):", value=5.0)
            st.info(f"Area: **{3.14159 * rad**2:.2f} cm²**  \nCircumference: **{2 * 3.14159 * rad:.2f} cm**")
        with c4:
            st.markdown("#### 📐 Pythagoras (Triangle Analysis)")
            side_a = st.number_input("Base length (a):", value=3.0)
            side_b = st.number_input("Height length (b):", value=4.0)
            st.warning(f"Hypotenuse (c): **{np.sqrt(side_a**2 + side_b**2):.2f}**")

        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3></div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()