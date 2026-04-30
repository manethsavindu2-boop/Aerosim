import streamlit as st
import pandas as pd
import numpy as np

# 1. Professional Page Setup
st.set_page_config(
    page_title="Avionix Systems | Flight Suite",
    page_icon="🚀",
    layout="wide"
)

# 2. Branding & Professional Image
st.title("🛡️ Avionix Systems")
st.subheader("Advanced Aerospace Simulation & Engineering Suite")

# This adds a professional aerospace image from a public URL
st.image("https://images.unsplash.com/photo-1517976487492-5750f3195933?auto=format&fit=crop&q=80&w=2000", 
         caption="Avionix Systems: Engineering the Future of Flight", 
         use_container_width=True)

st.markdown("---")

# 3. Organizing Your 3 Separate Modules into Tabs
tab1, tab2, tab3 = st.tabs([
    "✈️ Module 1: Thrust vs Drag", 
    "⚖️ Module 2: Lift vs Weight", 
    "🚨 Emergency: Engine Failure"
])

# --- MODULE 1: THRUST vs DRAG ---
with tab1:
    st.header("Propulsion & Aerodynamics")
    col1, col2 = st.columns(2)
    
    with col1:
        thrust = st.slider("Engine Thrust (N)", 0, 20000, 10000)
        drag_coeff = st.slider("Drag Coefficient", 0.01, 0.10, 0.04)
    
    with col2:
        net_force = thrust - (thrust * drag_coeff) # Simplified logic
        st.metric("Net Propulsive Force", f"{net_force} N")
        st.info("EASA Module 1 Logic: Calculating force vectors.")

# --- MODULE 2: LIFT vs WEIGHT ---
with tab2:
    st.header("Atmospheric Lift Analysis")
    st.write("Determine the stall speed and takeoff requirements.")
    
    weight = st.number_input("Aircraft Mass (kg)", value=1500)
    velocity = st.slider("Airspeed (knots)", 0, 300, 120)
    
    # Simple Lift Logic
    lift = (velocity**2) * 0.1 # Placeholder for your lift formula
    if lift > weight:
        st.success(f"LIFT ({lift:.0f} N) > WEIGHT ({weight} N): AIRCRAFT IS AIRBORNE")
    else:
        st.warning(f"Insufficient Lift: Increase velocity to exceed {weight} N")

# --- MODULE 3: ENGINE FAILURE ---
with tab3:
    st.header("Emergency Procedures Training")
    st.error("Simulate Critical System Failures")
    
    if st.button("INITIATE ENGINE FAILURE"):
        st.snow() # Visual effect
        st.error("CRITICAL: THRUST REDUCED TO 0%")
        st.write("EASA Training Protocol: Identify Glide Ratio and best landing site.")

# 4. Sidebar for Business Info (The "Millionaire" Touch)
st.sidebar.title("Avionix Systems")
st.sidebar.write("**Developer:** Maneth Savindu")
st.sidebar.write("**Version:** 1.0.0 Stable")
st.sidebar.markdown("---")
st.sidebar.info("For Enterprise Licensing, contact: manethsavindu2@gmail.com")
