import streamlit as st

# This is your secret key. You can change this to anything you want!
ACCESS_KEY = "AVIONIX-2026-PRO"

st.sidebar.title("🔐 Secure Login")
user_input = st.sidebar.text_input("Enter Access Key", type="password")

if user_input == ACCESS_KEY:
    # --- IF THE PASSWORD IS CORRECT, SHOW THE APP ---
    st.title("🛡️ Avionix Systems")
    st.subheader("Advanced Aerospace Simulation Suite")
    
    st.image("https://images.unsplash.com/photo-1517976487492-5750f3195933", 
             caption="Systems Online: Engineering the Future of Flight",
             use_container_width=True)
    
    st.success("Welcome back, Engineer. All modules are unlocked.")
    
    # You can add your Lift, Drag, and Thrust sliders here later!

else:
    # --- IF THE PASSWORD IS WRONG OR EMPTY, SHOW THIS ---
    st.title("🚀 Avionix Systems")
    st.error("Access Denied.")
    st.info("This is a premium engineering suite for EASA Part-66 students.")
    st.write("To purchase your access key, please contact: manethsavindu2@gmail.com")