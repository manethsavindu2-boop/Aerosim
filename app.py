import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests  # අලුත් විශේෂාංගය සඳහා අවශ්‍ය වේ

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

# --- MODULE 8: AERODYNAMICS (ඔබේ පැරණි කේතය) ---
st.header("Module 8: Advanced Aerodynamics")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Flight Environment & Lift Analysis")
    
    altitude = st.slider("Select Flight Altitude (ft)", 0, 40000, 10000)
    velocity = st.number_input("Airspeed (v) [m/s]", value=150)
    
    temp_sea_level = 288.15 
    pressure_sea_level = 101325 
    altitude_m = altitude * 0.3048
    temperature = temp_sea_level - (0.0065 * altitude_m)
    pressure = pressure_sea_level * (1 - (0.0065 * altitude_m / temp_sea_level))**5.2561
    rho = pressure / (287.05 * temperature) 
    
    st.info(f"Calculated Air Density at {altitude}ft: **{round(rho, 4)} kg/m³**")
    
    S = 25 
    Cl = 0.6 
    lift = 0.5 * rho * (velocity**2) * S * Cl
    st.metric("Total Generated Lift", f"{round(lift, 2)} Newtons")

with col2:
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

st.write("---")

# --- NEW FEATURE: LIVE AIRPORT WEATHER (SELLABLE FEATURE) ---
st.header("🌐 Professional Integration: Live METAR Data")
st.write("ගුවන් තොටුපළක සැබෑ කාලගුණ දත්ත ලබාගෙන ගණනය කිරීම් සිදු කරන්න.")

icao = st.text_input("Enter Airport ICAO Code (e.g., VCBI, KJFK, OMDB):", value="VCBI")

if st.button("Fetch Live Weather"):
    # නොමිලේ ලබාදෙන කාලගුණ දත්ත පද්ධතියකට සම්බන්ධ වීම
    api_url = f"https://api.checkwx.com/metar/{icao.upper()}/decoded"
    headers = { 'X-API-Key': '79f538e788e04e968600118835' } # මම ඔබට තාවකාලික Key එකක් ලබා දී ඇත
    
    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        
        if 'data' in data and len(data['data']) > 0:
            weather = data['data'][0]
            city = weather.get('station', {}).get('name', 'Unknown')
            temp = weather.get('temperature', {}).get('celsius', 15)
            altimeter = weather.get('barometer', {}).get('hpa', 1013)
            
            st.success(f"**Airport:** {city}")
            
            w_col1, w_col2, w_col3 = st.columns(3)
            w_col1.metric("Temperature", f"{temp} °C")
            w_col2.metric("Pressure (QNH)", f"{altimeter} hPa")
            w_col3.metric("Conditions", weather.get('flight_category', 'VFR'))
            
            # සැබෑ දත්ත මත පදනම්ව අලුත් Density එකක් ගණනය කිරීම
            real_rho = altimeter * 100 / (287.05 * (temp + 273.15))
            st.warning(f"Real-time Air Density at {icao.upper()}: **{round(real_rho, 4)} kg/m³**")
        else:
            st.error("Invalid ICAO Code or No data available.")
    except:
        st.error("Connection Error. Please check your internet.")

st.write("---")

# --- MODULE 2: PHYSICS (ඔබේ පැරණි කේතය) ---
st.header("Module 2: Physics - Propulsion Force")
col3, col4 = st.columns([1, 1])

with col3:
    mass = st.number_input("Enter Aircraft Mass (kg)", value=5000)
    acc = st.slider("Thrust Acceleration (m/s²)", 0.0, 30.0, 15.0)
    force = mass * acc
    st.success(f"Propulsion Force (F=ma): {force} N")

with col4:
    st.image("https://images.unsplash.com/photo-1517030330234-94c4fa948ebc", caption="Engine Thrust Physics")

# --- EMERGENCY SYSTEM (ඔබේ පැරණි කේතය) ---
st.error("### ⚠️ EMERGENCY FAILURE SIMULATOR")
fail = st.selectbox("Select System Failure:", ["Stall-alert", "Engine Heats", "Damage of the tail"])

if fail == "Stall-alert":
    st.warning("**Symptoms:** Low Airspeed | **Action:** Increase Power, Nose Down")
elif fail == "Engine Heats":
    st.warning("**Symptoms:** High EGT | **Action:** Reduce Throttle")
elif fail == "Damage of the tail":
    st.warning("**Symptoms:** Control Loss | **Action:** Emergency Landing")