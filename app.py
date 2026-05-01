import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Avionix Systems Pro - Advanced", layout="wide")

st.markdown(
    """
    <style>
    * { font-family: 'Courier New', Courier, monospace !important; }
    .stApp { background-color: #000000; color: white; }
    </style>
    """, unsafe_allow_html=True
)

st.title("🛰️ AVIONIX SYSTEMS - ADVANCED ENGINEERING INTERFACE")

# --- ADVANCED MODULE 8: AERODYNAMICS WITH LIVE GAUGES ---
st.header("Module 8: Advanced Aerodynamics")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Real-time Lift & Density Calculator")
    
    # ADVANCED INPUTS
    altitude = st.slider("Select Flight Altitude (ft)", 0, 40000, 10000)
    velocity = st.number_input("Airspeed (v) [m/s]", value=150)
    
    # MATH: Calculating Air Density based on Altitude (Troposphere model)
    # This is a professional-grade calculation
    temp_sea_level = 288.15 # Kelvin
    pressure_sea_level = 101325 # Pascals
    altitude_m = altitude * 0.3048
    temperature = temp_sea_level - (0.0065 * altitude_m)
    pressure = pressure_sea_level * (1 - (0.0065 * altitude_m / temp_sea_level))**5.2561
    rho = pressure / (287.05 * temperature) # Final Air Density
    
    st.info(f"Calculated Air Density at {altitude}ft: **{round(rho, 4)} kg/m³**")
    
    # LIFT CALCULATION
    S = 25 # Wing Area
    Cl = 0.6 # Coefficient of Lift
    lift = 0.5 * rho * (velocity**2) * S * Cl
    st.metric("Total Generated Lift", f"{round(lift, 2)} Newtons")

with col2:
    # 2. ADVANCED UI: VISUAL GAUGE FOR LIFT
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw={'projection': 'polar'})
    
    # Creating a simple Gauge look
    val = min(lift/200000, 1.0) # Normalizing for the gauge
    ax.set_facecolor('#000000')
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.barh(0, val * np.pi, color='lime', height=0.5)
    ax.set_ylim(-1, 1)
    ax.set_yticklabels([])
    ax.set_title("LIFT FORCE INTENSITY", color='white', pad=20)
    
    st.pyplot(fig)
    st.image("https://images.unsplash.com/photo-1460186136353-977e9d6085a1", caption="3D Aerodynamic Flow Analysis")

st.write("---")

# --- ADVANCED MODULE 2: PHYSICS (FORCE VECTORS) ---
st.header("Module 2: Advanced Physics - Force Vectors")

col3, col4 = st.columns([1, 1])

with col3:
    mass = st.number_input("Enter Aircraft Gross Mass (kg)", value=5000)
    acc = st.slider("Thrust Acceleration (m/s²)", 0.0, 30.0, 15.0)
    force = mass * acc
    st.success(f"Propulsion Force: {force} N")

with col4:
    # 3D Photo for Physics Module
    st.image("https://images.unsplash.com/photo-1517030330234-94c4fa948ebc", caption="Engine Thrust Physics Vector")

# --- EMERGENCY SYSTEM (SAME AS BEFORE) ---
st.error("### ⚠️ EMERGENCY FAILURE SIMULATOR")
fail = st.selectbox("Select System Failure:", ["Stall-alert", "Engine Heats", "Damage of the tail"])

if fail == "Stall-alert":
    st.warning("**Symptoms:** Low Airspeed, High AoA | **Action:** Increase Power, Pitch Down")
elif fail == "Engine Heats":
    st.warning("**Symptoms:** EGT Redline, Smoke | **Action:** Throttle Idle, Check Fire Suppressor")