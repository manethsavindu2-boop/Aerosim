import streamlit as st
import pandas as pd
import numpy as np

# 1. SETUP & GLOBAL FONT
st.set_page_config(page_title="Avionix Systems Pro", layout="wide")

# Global Monospace "Coding Type" Font
st.markdown(
    """
    <style>
    * { font-family: 'Courier New', Courier, monospace !important; }
    .stApp { background-color: #000000; }
    </style>
    """, unsafe_allow_html=True
)

if 'page' not in st.session_state:
    st.session_state.page = 'step1'

# --- STEP 1: OPENING PAGE ---
if st.session_state.page == 'step1':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa");
            background-size: cover;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.title("🚀 AVIONIX SYSTEMS")
    st.subheader("ORBITAL COMMAND INTERFACE")
    if st.button("TAP TO ENTER DASHBOARD"):
        st.session_state.page = 'step2'
        st.rerun()

# --- STEP 2: DASHBOARD (DARK FONT) ---
elif st.session_state.page == 'step2':
    st.markdown(
        """
        <style>
        .stApp { background-image: url("https://images.unsplash.com/photo-1534067783941-51c9c23ecefd"); background-size: cover; }
        /* Dark font as requested */
        .main-container, p, h1, h2, h3, li, span, label { color: #1A1A1A !important; font-weight: bold; }
        </style>
        """, unsafe_allow_html=True
    )
    st.title("🛡️ MISSION CONTROL DASHBOARD")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### EASA PART-66 MODULES")
        st.write("1. Mathematics\n2. Physics\n3. Electrical\n4. Electronics\n5. Digital Tech\n6. Materials\n7. Maintenance\n... and more")
    with col2:
        st.markdown("### HIGH MATHEMATICAL MOTION")
        st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", caption="Quantum Motion Analysis")
        if st.button("PROCEED TO MODULES"):
            st.session_state.page = 'step3'
            st.rerun()

# --- STEP 3: 14 MODULES + CALCULATORS + FAILURES ---
elif st.session_state.page == 'step3':
    st.title("🛰️ SYSTEM MODULES: 1 - 14")
    
    # --- MODULE 1: MATHEMATICS ---
    st.header("Module 1: Mathematics")
    val = st.slider("Input Variable (x) for Graph", 1, 100, 50)
    chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['Thrust Velocity'])
    st.line_chart(chart_data) # Graph as requested
    st.image("https://images.unsplash.com/photo-1569154941061-e231b4725ef1", width=300, caption="3D Aircraft Geometry")
    st.markdown("---")

    # --- MODULE 2: PHYSICS ---
    st.header("Module 2: Physics")
    st.write("Relavan calculations with interactive physics engine.")
    st.image("https://images.unsplash.com/photo-1460186136353-977e9d6085a1", width=300, caption="3D Aerodynamic Model")
    st.markdown("---")

    # (Repeat for 3-13... placeholders used for space)
    st.write("Modules 3-13 Initialized...")
    st.markdown("---")

    # --- MODULE 14: PROPULSION ---
    st.header("Module 14: Propulsion")
    st.write("Rocket and Turbine propulsion dynamics.")
    
    # --- LAST STEP: ENGINE FAILURES ---
    st.error("### ⚠️ SYSTEM FAILURE SIMULATOR")
    failure = st.selectbox("Select Failure Type:", ["Stall-alert", "Engine Heat", "Damage of the tail"])
    
    if failure == "Stall-alert":
        st.warning("SYMPTOMS: Low airspeed, buffeting, nose-heavy pitch.")
        st.info("ACTION: Decrease angle of attack, apply full power immediately.")
    elif failure == "Engine Heat":
        st.warning("SYMPTOMS: EGT/TIT gauge in RED, smoke, loss of thrust.")
        st.info("ACTION: Retard throttle, check fuel flow, activate extinguisher if fire occurs.")
    elif failure == "Damage of the tail":
        st.warning("SYMPTOMS: Yaw instability, loss of pitch control.")
        st.info("ACTION: Maintain high speed, use differential engine power for steering.")

    if st.button("BACK TO DASHBOARD"):
        st.session_state.page = 'step2'
        st.rerun()