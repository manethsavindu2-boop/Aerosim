import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Avionix Systems Pro", layout="wide")

# GUI පෙනුම සැකසීම
st.markdown(
    """
    <style>
    * { font-family: 'Courier New', Courier, monospace !important; }
    .stApp { background-color: #000000; color: white; }
    </style>
    """, unsafe_allow_html=True
)

st.title("🛰️ AVIONIX SYSTEMS - ADVANCED ENGINEERING INTERFACE")

# --- MODULE 8: AERODYNAMICS ---
st.header("Module 8: Advanced Aerodynamics")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Flight Environment & Lift Analysis")
    
    # පියාසර උස සහ වේගය ඇතුළත් කිරීම
    altitude = st.slider("Select Flight Altitude (ft)", 0, 40000, 10000)
    velocity = st.number_input("Airspeed (v) [m/s]", value=150)
    
    # වායු ඝනත්වය ගණනය කිරීම (ISA Model)
    temp_sea_level = 288.15 
    pressure_sea_level = 101325 
    altitude_m = altitude * 0.3048
    temperature = temp_sea_level - (0.0065 * altitude_m)
    pressure = pressure_sea_level * (1 - (0.0065 * altitude_m / temp_sea_level))**5.2561
    rho = pressure / (287.05 * temperature) 
    
    st.info(f"Calculated Air Density at {altitude}ft: **{round(rho, 4)} kg/m³**")
    
    # Lift Calculation: L = 1/2 * rho * v^2 * S * Cl
    S = 25 
    Cl = 0.6 
    lift = 0.5 * rho * (velocity**2) * S * Cl
    st.metric("Total Generated Lift", f"{round(lift, 2)} Newtons")

with col2:
    # සජීවී Gauge දර්ශකය නිර්මාණය කිරීම
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw={'projection': 'polar'})
    val = min(lift/200000, 1.0) 
    ax.set_facecolor('#000000')
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.barh(0, val * np.pi, color='lime', height=0.5)
    ax.set_ylim(-1, 1)
    ax.set_yticklabels([])
    ax.set_title("LIFT FORCE INTENSITY", color='white', pad=20)
    
    st.pyplot(fig)
    st.image("https://images.unsplash.com/photo-1460186136353-977e9d6085a1", caption="3D Aerodynamic Analysis")

st.write("---")

# --- MODULE 2: PHYSICS ---
st.header("Module 2: Physics - Propulsion Force")

col3, col4 = st.columns([1, 1])

with col3:
    mass = st.number_input("Enter Aircraft Mass (kg)", value=5000)
    acc = st.slider("Thrust Acceleration (m/s²)", 0.0, 30.0, 15.0)
    force = mass * acc
    st.success(f"Propulsion Force (F=ma): {force} N")

with col4:
    st.image("https://images.unsplash.com/photo-1517030330234-94c4fa948ebc", caption="Engine Thrust Physics")

st.write("---")

# --- EMERGENCY SYSTEM ---
st.error("### ⚠️ EMERGENCY FAILURE SIMULATOR")
fail = st.selectbox("Select System Failure:", ["Stall-alert", "Engine Heats", "Damage of the tail"])

if fail == "Stall-alert":
    st.warning("**Symptoms:** Low Airspeed | **Action:** Increase Power, Nose Down")
elif fail == "Engine Heats":
    st.warning("**Symptoms:** High EGT | **Action:** Reduce Throttle")
elif fail == "Damage of the tail":
    st.warning("**Symptoms:** Control Loss | **Action:** Emergency Landing")