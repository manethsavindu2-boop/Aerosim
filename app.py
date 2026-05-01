import streamlit as st
import math

# 1. SETUP & SECURITY (The Foundation)
ACCESS_KEY = "AVIONIX-2026-PRO"

st.set_page_config(page_title="Avionix SR-71 Pro", layout="wide")

st.sidebar.title("🔐 Secure Access")
user_input = st.sidebar.text_input("Enter Access Key", type="password")

# 2. CHECK THE KEY
if user_input == ACCESS_KEY:
    st.sidebar.success("Engineer Verified")
    
    # 3. NAVIGATION MENU
    st.sidebar.title("🛠️ Navigation")
    app_mode = st.sidebar.selectbox("Choose Module:", ["Dashboard", "Module 14: Propulsion"])

    # --- THE MASTER PAGE (SR-71 DESIGN) ---
    if app_mode == "Dashboard":
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://r.jina.ai/i/6ef2482283084334a179374026600989");
                background-attachment: fixed;
                background-size: cover;
            }}
            .main {{
                background: rgba(0, 0, 0, 0.7); 
                color: white;
                padding: 30px;
                border-radius: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        st.title("🦅 AVIONIX | SR-71 STRATEGIC COMMAND")
        st.subheader("Advanced Aerospace Engineering Suite")
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("System Speed", "Mach 3.2+")
        with col2:
            st.metric("Status", "Operational")
        with col3:
            st.metric("Altitude", "85,000 ft")

        st.info("Welcome, Engineer. Select a module from the sidebar to begin.")

    # --- MODULE 14: PROPULSION ---
    elif app_mode == "Module 14: Propulsion":
        st.title("🚀 Module 14: Propulsion Systems")
        st.write("Current Focus: Jet Engine Theory & Thrust")
        st.image("https://images.unsplash.com/photo-1544725176-7c40e5a71c5e", caption="Turbine Engine Analysis", width=500)
        # We can add thrust calculators here next!

else:
    # THIS SHOWS IF THE KEY IS WRONG OR EMPTY
    st.title("🚀 Avionix Systems")
    st.error("Access Denied. Enter your security key in the sidebar.")
    st.write("Contact: manethsavindu2@gmail.com")