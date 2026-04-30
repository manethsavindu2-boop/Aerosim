import streamlit as st

# Your secret key
ACCESS_KEY = "AVIONIX-2026-PRO"

st.sidebar.title("🔐 Secure Login")
user_input = st.sidebar.text_input("Enter Access Key", type="password")

if user_input == ACCESS_KEY:
    st.title("🛡️ Avionix Systems")
    st.success("Welcome back, Engineer. All modules are unlocked.")
    
    # --- NEW MODULE: AERODYNAMICS CALCULATOR ---
    st.header("✈️ Aerodynamics Module (EASA Part-66)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Parameters")
        velocity = st.slider("Airspeed (m/s)", 0, 300, 150)
        air_density = 1.225  # kg/m^3 at sea level
        wing_area = st.number_input("Wing Area (m²)", value=25.0)
        cl = st.slider("Coefficient of Lift (Cl)", 0.0, 2.0, 0.5)

    # Physics Formula: Lift = 0.5 * rho * v^2 * Area * Cl
    lift_force = 0.5 * air_density * (velocity**2) * wing_area * cl

    with col2:
        st.subheader("Results")
        st.metric("Generated Lift", f"{round(lift_force, 2)} Newtons")
        if lift_force > 10000:
            st.info("Status: Sufficient Lift for Takeoff")
        else:
            st.warning("Status: Low Speed - Increase Velocity")

else:
    st.title("🚀 Avionix Systems")
    st.error("Access Denied. Please enter your key in the sidebar.")