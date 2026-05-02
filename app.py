import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# --- 1. පද්ධති සැකසුම් (Configuration) ---
st.set_page_config(page_title="Avionix Systems Pro", layout="wide")

# GUI පෙනුම සහ අකුරු සැකසීම
st.markdown(
    """
    <style>
    * { font-family: 'Courier New', Courier, monospace !important; }
    .stApp { background-color: #000000; color: white; }
    </style>
    """, unsafe_allow_html=True
)

st.title("🛰️ AVIONIX SYSTEMS - ADVANCED ENGINEERING INTERFACE")

# --- 2. LIVE AIRPORT WEATHER (අලුත් විශේෂාංගය) ---
st.header("🌐 Professional Integration: Live METAR Data")
st.write("ඕනෑම ගුවන් තොටුපළක සැබෑ කාලගුණ දත්ත ලබාගෙන ගණනය කිරීම් සිදු කරන්න.")

icao = st.text_input("Enter Airport ICAO Code (e.g., VCBI, KJFK, OMDB):", value="VCBI")

# මූලික අගයන් (Default values)
current_rho = 1.225 

if st.button("Fetch Live Weather"):
    api_url = f"https://api.checkwx.com/metar/{icao.upper()}/decoded"
    headers = { 'X-API-Key': '79f538e788e04e968600118835' } 
    
    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        
        if 'data' in data and len(data['data']) > 0:
            weather = data['data'][0]
            city = weather.get('station', {}).get('name', 'Unknown Station')
            temp = weather.get('temperature', {}).get('celsius', 15)
            altimeter = weather.get('barometer', {}).get('hpa', 1013)
            
            st.success(f"**Airport identified:** {city}")
            
            w_col1, w_col2, w_col3 = st.columns(3)
            w_col1.metric("Temperature", f"{temp} °C")
            w_col2.metric("Pressure (QNH)", f"{altimeter} hPa")
            w_col3.metric("Conditions", weather.get('flight_category', 'VFR'))
            
            # සැබෑ දත්ත මත වායු ඝනත්වය ගණනය කිරීම
            current_rho = altimeter * 100 / (287.05 * (temp + 273.15))
            st.session_state['rho'] = current_rho
            st.info(f"Real-time Air Density calculated: **{round(current_rho, 4)} kg/m³**")
        else:
            st.error("Invalid ICAO Code. Please try VCBI for Katunayake.")
    except:
        st.error("Connection Error. Check your internet.")

st.write("---")

# --- 3. AERODYNAMICS ANALYSIS ---
st.header("Module 8: Aerodynamics Analysis")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Lift Calculation")
    # පෙර ගණනය කළ rho අගය භාවිතා කිරීම
    rho_to_use = st.session_state.get('rho', 1.225)
    velocity = st.slider("Airspeed (v) [m/s]", 0, 300, 150)
    S = 25  # Wing Area
    Cl = 0.6 # Lift Coefficient
    
    lift = 0.5 * rho_to_use * (velocity**2) * S * Cl
    st.metric("Total Generated Lift", f"{round(lift, 2)} Newtons")
    st.caption(f"Using Air Density: {round(rho_to_use, 4)} kg/m³")

with col2:
    # Lift Gauge එක නිර්මාණය
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw={'projection': 'polar'})
    gauge_val = min(lift/200000, 1.0)
    ax.set_facecolor('#000000')
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.barh(0, gauge_val * np.pi, color='lime', height=0.5)
    ax.set_ylim(-1, 1)
    ax.set_yticklabels([])
    ax.set_title("LIFT FORCE INTENSITY", color='white')
    st.pyplot(fig)

st.write("---")

# --- 4. PHYSICS & EMERGENCY ---
st.header("Module 2: Physics & Emergency")
p_col1, p_col2 = st.columns(2)

with p_col1:
    mass = st.number_input("Aircraft Mass (kg)", value=5000)
    acc = st.slider("Acceleration (m/s²)", 0.0, 30.0, 10.0)
    st.success(f"Propulsion Force (F=ma): {mass * acc} N")

with p_col2:
    fail = st.selectbox("Simulate System Failure:", ["None", "Stall-alert", "Engine Overheat"])
    if fail == "Stall-alert":
        st.warning("⚠️ Warning: Increase power and lower the nose!")
    elif fail == "Engine Overheat":
        st.error("⚠️ Danger: Reduce throttle immediately!")

st.write("---")
st.caption("Developed by Maneth Savindu - Avionix Systems v2.0")