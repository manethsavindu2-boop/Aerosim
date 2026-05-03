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

# --- STEP 3: MODULES PAGE (MODULE 1 & 2 THEORY) ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    
    # --- MODULE 1: MATHEMATICS (දැනට පවතින කොටස) ---
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.markdown("#### ⚙️ Arithmetic & Algebra")
            st.write("* **BODMAS:** Brackets, Orders, Division, Multiplication, Addition, Subtraction.\n* **Compression Ratio:** $CR = (V_s + V_c) / V_c$")
        with t_col2:
            st.markdown("#### 📐 Geometry")
            st.write("* **Radius Based Area:** $\\pi r^2$\n* **Pythagoras:** $a^2 + b^2 = c^2$")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- MODULE 2: PHYSICS (නව සිද්ධාන්ත ඇතුළත් කොටස) ---
    elif mod == "Module 2":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📕 MODULE 02: PHYSICS (EASA PART 66)")
        
        theory_col1, theory_col2 = st.columns(2)
        
        with theory_col1:
            st.subheader("🚀 Statics & Kinetics")
            st.write("""
            * **Newton's 1st Law:** Inertia - A body remains at rest or uniform motion unless acted upon by a force.
            * **Newton's 2nd Law:** Force equals mass times acceleration ($F = m \\times a$).
            * **Newton's 3rd Law:** For every action, there is an equal and opposite reaction.
            * **Moment (Torque):** Force $\\times$ Perpendicular distance ($M = F \\times d$).
            """)
            
            st.subheader("🌡️ Thermodynamics")
            st.write("""
            * **Boyle's Law:** $P_1V_1 = P_2V_2$ (Constant Temperature).
            * **Charles's Law:** $V_1/T_1 = V_2/T_2$ (Constant Pressure).
            * **Heat Transfer:** Conduction, Convection, and Radiation.
            """)

        with theory_col2:
            st.subheader("💧 Fluid Dynamics & Aero")
            st.write("""
            * **Bernoulli's Principle:** As the speed of a moving fluid increases, the pressure within the fluid decreases. (Crucial for **LIFT**).
            * **Venturi Effect:** Reduction in fluid pressure that results when a fluid flows through a constricted section of a pipe.
            * **Atmospheric Pressure:** Standard Day = 1013.25 hPa (29.92 "Hg) at 15°C.
            """)
            
            st.subheader("⚙️ Matter & Energy")
            st.write("""
            * **Potential Energy:** $m \\times g \\times h$.
            * **Kinetic Energy:** $\\frac{1}{2} m \\times v^2$.
            * **Power:** Work done per unit time ($P = W / t$).
            """)

        st.write("---")
        st.subheader("🛠️ Quick Physics Reference")
        st.info("Module 2 provides the foundation for Module 8 (Aerodynamics) and Module 11/13 (Systems). Understanding Bernoulli and Newton is key to mastering flight physics.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3></div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()