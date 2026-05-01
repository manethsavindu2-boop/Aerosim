import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIGURATION & CODING FONT ---
st.set_page_config(page_title="Avionix Systems Pro", layout="wide")

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
        .stApp { 
            background-image: url("https://images.unsplash.com/photo-1534067783941-51c9c23ecefd"); 
            background-size: cover; 
        }
        h1, h2, h3, p, span, li, label { 
            color: #1A1A1A !important; 
            font-weight: bold; 
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.title("🛡️ MISSION CONTROL DASHBOARD")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### EASA PART-66 MODULES")
        st.write("1. Mathematics\n2. Physics\n3. Electrical\n4. Electronics\n5. Digital Tech\n6. Materials\n7. Maintenance\n8. Aerodynamics\n... and 6 more")
    with col2:
        st.markdown("### HIGH MATHEMATICAL MOTION")
        st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb")
        if st.button("PROCEED TO MODULES"):
            st.session_state.page = 'step3'
            st.rerun()

# --- STEP 3: 14 MODULES WITH USER INPUT CALCULATORS ---
elif st.session_state.page == 'step3':
    st.markdown("<style>.stApp { background: #000000; color: white; }</style>", unsafe_allow_html=True)
    st.title("🛰️ SYSTEM MODULES: 1 - 14")

    # MODULE 1: MATHEMATICS (Quadratic Calculator)
    with st.expander("Module 1: Mathematics - Quadratic Solver", expanded=True):
        st.write("Enter coefficients for $ax^2 + bx + c = 0$")
        colA, colB, colC = st.columns(3)
        a = colA.number_input("Input a", value=1.0)
        b = colB.number_input("Input b", value=5.0)
        c = colC.number_input("Input c", value=6.0)
        
        # Graph logic
        x = np.linspace(-10, 10, 100)
        y = a*x**2 + b*x + c
        st.line_chart(pd.DataFrame({'Y-Axis': y}, index=x))
        st.image("https://images.unsplash.com/photo-1569154941061-e231b4725ef1", width=300, caption="3D Aircraft Geometry")

    # MODULE 2: PHYSICS (Force Calculator)
    with st.expander("Module 2: Physics - Force (F=ma)"):
        mass = st.number_input("Enter Mass (kg)", value=1200)
        acc = st.number_input("Enter Acceleration (m/s²)", value=9.8)
        st.success(f"Calculated Force: {mass * acc} Newtons")
        st.image("https://images.unsplash.com/photo-1460186136353-977e9d6085a1", width=300, caption="3D Aerodynamic Physics")

    # MODULE 3: ELECTRICAL (Ohm's Law)
    with st.expander("Module 3: Electrical - Ohm's Law"):
        current = st.number_input("Enter Current (I)", value=2.0)
        resistance = st.number_input("Enter Resistance (R)", value=10.0)
        st.success(f"Voltage (V): {current * resistance} Volts")

    # MODULE 8: BASIC AERODYNAMICS (Lift Calculator)
    with st.expander("Module 8: Basic Aerodynamics - Lift"):
        velocity = st.slider("Velocity (v)", 0, 300, 150)
        rho = 1.225 # Air density
        S = 25 # Wing area
        Cl = 0.5 # Lift coefficient
        lift = 0.5 * rho * (velocity**2) * S * Cl
        st.metric("Total Lift Force", f"{round(lift, 2)} N")
        st.write("Dynamic Lift Curve:")
        st.line_chart(np.random.randn(20, 1)) # Simulated motion graph

    # --- FINAL STEP: ENGINE FAILURES ---
    st.markdown("---")
    st.error("### ⚠️ EMERGENCY FAILURE SIMULATOR (LAST STEP)")
    failure_type = st.selectbox("Select Failure Simulation:", ["Stall-alert", "Engine Heats", "Damage of the tail"])
    
    if failure_type == "Stall-alert":
        st.warning("**Symptoms:** Buffeting (shaking), low airspeed, nose pitch down.")
        st.info("**Corrective Action:** Decrease angle of attack, apply full power.")
    elif failure_type == "Engine Heats":
        st.warning("**Symptoms:** EGT gauge in RED, smoke, smell of burning oil.")
        st.info("**Corrective Action:** Reduce throttle, monitor oil pressure, prepare for shutdown.")
    elif failure_type == "Damage of the tail":
        st.warning("**Symptoms:** Yaw/Pitch instability, loss of control surface response.")
        st.info("**Corrective Action:** Maintain airspeed, use differential engine power to steer.")

    if st.button("BACK TO DASHBOARD"):
        st.session_state.page = 'step2'
        st.rerun()
        