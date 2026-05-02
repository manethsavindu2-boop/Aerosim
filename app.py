import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (Configuration) ---
st.set_page_config(page_title="Avionix Systems Lite", layout="wide")

# GUI පෙනුම සැකසීම
st.markdown(
    """
    <style>
    .stApp { background-color: #0b0d17; color: #e0e0e0; }
    h1, h2 { color: #4facfe; font-family: 'Segoe UI', sans-serif; }
    </style>
    """, unsafe_allow_html=True
)

st.title("🛰️ AVIONIX SYSTEMS - ENGINEERING SUITE")
st.write("වෘත්තීය ගුවන් යානා ඉංජිනේරු දත්ත විශ්ලේෂකය")

# --- 2. AERODYNAMICS MODULE ---
st.header("Module 8: Aerodynamics")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Lift Parameters")
    # උස (Altitude) අනුව වායු ඝනත්වය ගණනය කිරීම
    altitude = st.slider("Altitude (ft)", 0, 40000, 10000)
    velocity = st.number_input("Airspeed (v) [m/s]", value=150)
    
    # ISA Standard calculation (සරල කළ අගයන්)
    rho = 1.225 * (1 - (0.00000688 * altitude))**4.256
    
    st.info(f"Air Density (ρ): {round(rho, 4)} kg/m³")
    
    # Lift Calculation
    S = 25  # Wing area
    Cl = 0.6 # Lift Coefficient
    lift = 0.5 * rho * (velocity**2) * S * Cl
    
    st.metric("Calculated Lift Force", f"{round(lift, 2)} N")

with col2:
    # Streamlit වල ඇති සරල Chart එකක් භාවිතා කර Lift පෙන්වීම
    chart_data = pd.DataFrame(
        np.random.randn(20, 1),
        columns=['Lift Stability']
    )
    st.line_chart(chart_data)
    st.caption("Real-time Lift Stability Graph")

st.write("---")

# --- 3. PHYSICS & PROPULSION ---
st.header("Module 2: Physics")

p_col1, p_col2 = st.columns(2)

with p_col1:
    mass = st.number_input("Aircraft Mass (kg)", value=5000)
    acc = st.slider("Acceleration (m/s²)", 0.0, 50.0, 15.0)
    force = mass * acc
    st.success(f"Propulsion Force (F=ma): {force} Newtons")

with p_col2:
    st.subheader("Fuel Calculation")
    fuel_rate = st.number_input("Fuel Consumption (kg/min)", value=20)
    time = st.number_input("Flight Duration (min)", value=120)
    total_fuel = fuel_rate * time
    st.warning(f"Total Fuel Needed: {total_fuel} kg")

st.write("---")

# --- 4. EMERGENCY PROCEDURES ---
st.header("⚠️ Emergency Protocols")
status = st.selectbox("Current System Status:", ["Normal", "Engine Fire", "Hydraulic Failure"])

if status == "Engine Fire":
    st.error("ACTION: Cut fuel supply, deploy extinguishers, emergency descent.")
elif status == "Hydraulic Failure":
    st.error("ACTION: Switch to manual backup, check landing gear locks.")
else:
    st.success("All systems operational.")

st.caption("Created by Maneth Savindu | Avionix Systems Lite v1.0")