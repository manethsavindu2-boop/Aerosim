import streamlit as st

# Your secret access key
ACCESS_KEY = "AVIONIX-2026-PRO"

# Setup page layout
st.set_page_config(page_title="Avionix Systems Pro", page_icon="🚀", layout="wide")

# Sidebar for Login and Navigation
st.sidebar.title("🔐 Secure Access")
user_input = st.sidebar.text_input("Enter Access Key", type="password")

if user_input == ACCESS_KEY:
    st.sidebar.success("Verified Engineer")
    
    # NAVIGATION MENU
    st.sidebar.title("🛠️ Engineering Menu")
    app_mode = st.sidebar.selectbox("Choose a Module:", 
        ["Dashboard", "Module 1: Mathematics", "Module 2: Physics", "Engine Failure Diagnosis"])

    # --- DASHBOARD ---
    if app_mode == "Dashboard":
        st.title("🛡️ Avionix Systems: Engineering Suite")
        st.subheader("Welcome back, Engineer. All systems are online.")
        st.image("https://images.unsplash.com/photo-1517976487492-5750f3195933", use_container_width=True)
        st.info("Select a module from the sidebar to begin your calculations or diagnosis.")

    # --- MODULE 1: MATHEMATICS ---
    elif app_mode == "Module 1: Mathematics":
        st.title("🔢 Module 1: Mathematics (EASA Part-66)")
        st.subheader("Binary to Decimal Converter")
        binary_val = st.text_input("Enter Binary Number (e.g., 1010):", "0")
        try:
            decimal_val = int(binary_val, 2)
            st.metric("Decimal Equivalent", decimal_val)
        except ValueError:
            st.error("Please enter a valid binary number (only 0s and 1s).")

    # --- MODULE 2: PHYSICS ---
    elif app_mode == "Module 2: Physics":
        st.title("📚 Module 2: Physics (Matter & Statics)")
        col1, col2 = st.columns(2)
        with col1:
            mass = st.number_input("Mass (kg)", value=1.0)
            volume = st.number_input("Volume (m³)", value=1.0)
        with col2:
            if volume > 0:
                density = mass / volume
                st.metric("Density", f"{density} kg/m³")
        st.info("Formula: Density = Mass / Volume")

    # --- ENGINE FAILURE DIAGNOSIS ---
    elif app_mode == "Engine Failure Diagnosis":
        st.title("🔥 Engine Failure Diagnosis & Action")
        failure = st.selectbox("Select Observed Failure:", ["None", "Flameout", "Compressor Stall", "FOD"])
        
        if failure == "Flameout":
            st.error("⚠️ FLAMEOUT DETECTED")
            st.write("**Symptoms:** Rapid RPM drop, EGT decrease.")
            st.write("**Standard Action:** Check fuel flow, attempt relight if within altitude envelope.")
        elif failure == "Compressor Stall":
            st.warning("⚠️ COMPRESSOR STALL")
            st.write("**Symptoms:** Loud bangs, vibration, high EGT.")
            st.write("**Standard Action:** Retard throttle, monitor temperatures.")

else:
    # LOCK SCREEN
    st.title("🚀 Avionix Systems")
    st.error("Access Denied.")
    st.info("This is a premium suite for EASA Part-66 students.")
    st.write("To purchase your 2026 Access Key, contact: **manethsavindu2@gmail.com**")