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

# --- STEP 3: MODULES PAGE ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    # --- MODULE 1 (STAYING THE SAME) ---
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.subheader("📚 Theory Facts")
            st.write("* **BODMAS:** Rules for solving expressions.  \n* **Compression Ratio:** $CR = (V_s + V_c) / V_c$.")
        with t_col2:
            st.subheader("📐 Geometry")
            st.write("* **Pythagoras:** $a^2 + b^2 = c^2$.  \n* **Radius:** Area = $\\pi r^2$.")
        st.write("---")
        c1, c2 = st.columns(2)
        with c1:
            rad = st.number_input("Input Radius ($r$ in cm):", value=5.0)
            st.info(f"Area: **{3.14159 * rad**2:.2f} cm²**")
        with c2:
            vs = st.number_input("Swept Volume ($V_s$):", value=500.0)
            vc = st.number_input("Clearance Volume ($V_c$):", value=50.0)
            st.success(f"CR: **{(vs + vc)/vc if vc > 0 else 0:.1f}:1**")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- MODULE 2 (ALL NEW PHYSICS THEORY & CALCS) ---
    elif mod == "Module 2":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📕 MODULE 02: PHYSICS")
        
        # Theory Section
        st.subheader("📚 Core Physics Theory")
        pt_col1, pt_col2 = st.columns(2)
        with pt_col1:
            st.markdown("#### ⚡ Statics & Dynamics")
            st.write("""
            * **Newton's 1st Law:** Objects stay at rest or in motion unless acted upon by a force.
            * **Newton's 2nd Law:** Force equals mass times acceleration ($F = ma$).
            * **Newton's 3rd Law:** For every action, there is an equal and opposite reaction.
            * **Stress & Strain:** Stress = Force/Area. Strain = Extension/Length.
            """)
        with pt_col2:
            st.markdown("#### 🌬️ Fluid Dynamics & Thermo")
            st.write("""
            * **Bernoulli's Principle:** As the velocity of a fluid increases, its pressure decreases (The basis of Lift).
            * **Boyle's Law:** Volume is inversely proportional to Pressure ($P_1V_1 = P_2V_2$).
            * **Charles's Law:** Volume is directly proportional to Temperature ($V/T = k$).
            * **Specific Gravity:** Density of substance / Density of water.
            """)

        st.write("---")
        
        # Calculations Section
        st.subheader("⚙️ Physics Simulation Tools")
        pc_col1, pc_col2 = st.columns(2)
        
        with pc_col1:
            st.markdown("#### 🏗️ Force & Pressure")
            mass_kg = st.number_input("Mass (kg):", value=10.0)
            accel_ms = st.number_input("Acceleration (m/s²):", value=9.81)
            st.success(f"Force (F): **{mass_kg * accel_ms:.2f} Newtons**")
            
            p_force = st.number_input("Applied Force (N):", value=100.0)
            p_area = st.number_input("Surface Area (m²):", value=1.0)
            st.info(f"Pressure (P): **{p_force / p_area if p_area > 0 else 0:.2f} Pa (N/m²)**")

        with pc_col2:
            st.markdown("#### 🧪 Gas Law Calculator")
            p1 = st.number_input("Initial Pressure (P1):", value=1.0)
            v1 = st.number_input("Initial Volume (V1):", value=10.0)
            v2 = st.number_input("Final Volume (V2):", value=5.0)
            p2 = (p1 * v1) / v2 if v2 > 0 else 0
            st.warning(f"Final Pressure (P2): **{p2:.2f} units**")
            
            st.markdown("#### 🌀 Density & Specific Gravity")
            d_mass = st.number_input("Object Mass (g):", value=100.0)
            d_vol = st.number_input("Object Volume (cm³):", value=50.0)
            st.info(f"Density: **{d_mass / d_vol if d_vol > 0 else 0:.2f} g/cm³**")

        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3></div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()