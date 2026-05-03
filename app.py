import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් සහ වර්ණ සැකසීමේ ශ්‍රිතය
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
    
    # --- MODULE 1 (MATHEMATICS) ---
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.subheader("📚 Theory Facts")
            st.write("* **BODMAS:** Order of ops.\n* **Indices:** Powers of numbers.\n* **Compression Ratio:** $CR = (V_s + V_c) / V_c$.")
        with t_col2:
            st.subheader("📐 Geometry")
            st.write("* **Pythagoras:** $a^2 + b^2 = c^2$.\n* **Radius:** Area = $\pi r^2$.")
        st.write("---")
        c1, c2 = st.columns(2)
        with c1:
            vs = st.number_input("Swept Volume:", value=500.0)
            vc = st.number_input("Clearance Volume:", value=50.0)
            st.info(f"CR: **{(vs + vc) / vc if vc > 0 else 0:.1f}:1**")
        with c2:
            rad = st.number_input("Radius (cm):", value=5.0)
            st.info(f"Area: **{3.14 * rad**2:.2f} cm²**")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- MODULE 2 (PHYSICS) ---
    elif mod == "Module 2":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📕 MODULE 02: PHYSICS")
        pt_col1, pt_col2 = st.columns(2)
        with pt_col1:
            st.subheader("🏃 Dynamics")
            st.write("* **Newton's Laws:** 1st, 2nd ($F=ma$), and 3rd.\n* **Work:** Force $\\times$ Distance.")
        with pt_col2:
            st.subheader("💨 Fluid & Heat")
            st.write("* **Bernoulli:** Lift Principle.\n* **Gas Laws:** Boyle's ($P_1V_1=P_2V_2$).")
        st.write("---")
        pc1, pc2 = st.columns(2)
        with pc1:
            mass = st.number_input("Mass (kg):", value=10.0)
            acc = st.number_input("Acc (m/s²):", value=9.8)
            st.success(f"Force: **{mass*acc:.2f} N**")
        with pc2:
            f_p = st.number_input("Force (N):", value=100.0)
            a_p = st.number_input("Area (m²):", value=2.0)
            st.warning(f"Pressure: **{f_p/a_p if a_p > 0 else 0:.2f} Pa**")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- MODULE 3 (ELECTRICAL FUNDAMENTALS) ---
    elif mod == "Module 3":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("⚡ MODULE 03: ELECTRICAL FUNDAMENTALS")
        
        # Electrical Theory
        st.subheader("📚 Key Electrical Theory")
        et_col1, et_col2 = st.columns(2)
        with et_col1:
            st.markdown("#### ⚡ DC Circuits & Ohm's Law")
            st.write("""
            * **Ohm's Law:** Voltage ($V$) equals Current ($I$) times Resistance ($R$). ($V = I \\times R$)
            * **Kirchhoff’s Laws:** Current entering a junction equals current leaving (KCL).
            * **Series Circuit:** Total Resistance $R_t = R_1 + R_2 + R_3$.
            * **Parallel Circuit:** $1/R_t = 1/R_1 + 1/R_2 + 1/R_3$.
            """)
        with et_col2:
            st.markdown("#### 🔋 Power & Capacitance")
            st.write("""
            * **Electrical Power:** Measured in Watts ($W$). $P = V \\times I$ or $P = I^2 \\times R$.
            * **Capacitance:** Ability to store charge ($Q = C \\times V$).
            * **Magnetism:** Relationship between electricity and magnetic fields (Inductance).
            """)

        st.write("---")
        st.subheader("⚙️ Essential Electrical Calculations")
        ec1, ec2 = st.columns(2)
        
        with ec1:
            st.markdown("#### 🛠️ Ohm's Law & Power")
            v_in = st.number_input("Voltage (V):", value=28.0) # Aircraft standard DC
            r_in = st.number_input("Resistance (Ω):", value=4.0)
            current = v_in / r_in if r_in > 0 else 0
            power = v_in * current
            st.success(f"Current (I): **{current:.2f} A** | Power (P): **{power:.2f} W**")

        with ec2:
            st.markdown("#### 🔌 Resistors in Parallel")
            r1 = st.number_input("R1 (Ω):", value=10.0)
            r2 = st.number_input("R2 (Ω):", value=10.0)
            r_total = (r1 * r2) / (r1 + r2) if (r1 + r2) > 0 else 0
            st.info(f"Total Parallel Resistance: **{r_total:.2f} Ω**")

        st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3></div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()