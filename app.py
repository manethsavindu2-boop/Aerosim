import streamlit as st

# --- SECURITY SETUP ---
ACCESS_KEY = "AVIONIX-2026-PRO"

# Setup page layout
st.set_page_config(page_title="Avionix Orbital", page_icon="🚀", layout="wide")

# Custom CSS for the SpaceX "Hatch" Login (White Background)
if 'verified' not in st.session_state:
    st.session_state['verified'] = False

if not st.session_state['verified']:
    st.markdown(
        """
        <style>
        .stApp {{
            background-color: #FFFFFF;
        }}
        .main-container {{
            text-align: center;
            padding: 50px;
        }}
        input {{
            border: 2px solid #000000 !important;
            border-radius: 5px !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.image("https://www.spacex.com/static/images/share.jpg", width=300) # SpaceX Logo
    st.title("🚀 AVIONIX SYSTEMS | ORBITAL COMMAND")
    st.subheader("EASA PART-66 | GRADE 11 ENGINEERING SUITE")
    st.write("SECURE ACCESS REQUIRED. PLEASE ENTER YOUR DIGITAL HATCH KEY.")
    
    user_input = st.text_input("Enter Access Key", type="password", key="login_key")
    
    if st.button("OPEN HATCH"):
        if user_input == ACCESS_KEY:
            st.session_state['verified'] = True
            st.rerun()
        else:
            st.error("ACCESS DENIED: INCORECT KEY.")
            
else:
    # --- LOGGED IN AREA (SpaceX Dark Theme) ---
    st.markdown(
        """
        <style>
        .stApp {{
            background-color: #000000;
            color: #FFFFFF;
            font-family: 'Avenir', sans-serif;
        }}
        .metric-container {{
            background-color: #1A1A1A;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #333333;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # NAVIGATION MENU
    st.sidebar.title("👨‍🚀 Orbital Menu")
    app_mode = st.sidebar.radio("Mission Control:", ["Dashboard", "Module 1: Mathematics", "Module 14: Propulsion"])
    
    if st.sidebar.button("Logout"):
        st.session_state['verified'] = False
        st.rerun()

    if app_mode == "Dashboard":
        # --- HEADER SECTION ---
        st.title("🛡️ MISSION CONTROL DASHBOARD")
        st.markdown("---")
        
        # --- TOP STATS (Rocket Readiness) ---
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Payload Status", value="DEPLOYED", delta="Falcon 9")
        with col2:
            st.metric(label="EASA Modules Loaded", value="14 Active")
        with col3:
            st.metric(label="Network Status", value="STARLINK UP")

        st.markdown("### 🛠️ Quick Access Modules")
        
        # --- NAVIGATION CARDS ---
        row1_col1, row1_col2 = st.columns(2)
        
        with row1_col1:
            st.info("#### 🔢 Module 1: Mathematics")
            st.write("A/L Prep and Arithmetic tools.")
            if st.button("Open Mathematics"):
                st.write("Select 'Module 1' from the sidebar.")

        with row1_col2:
            st.success("#### 🚀 Module 14: Propulsion")
            st.write("Jet Engine Theory & Thrust Dynamics.")
            if st.button("Open Propulsion"):
                st.write("Select 'Module 14' from the sidebar.")

        st.markdown("---")
        st.write("© 2026 Avionix Systems Engineering. Designed for Grade 11 & EASA Part-66 Students.")

    elif app_mode == "Module 1: Mathematics":
        st.title("🔢 Module 1: Mathematics")
        st.write("Mathematical tools will be loaded here.")
        
    elif app_mode == "Module 14: Propulsion":
        st.title("🚀 Module 14: Propulsion")
        st.write("Jet and Rocket engine details will be loaded here.")