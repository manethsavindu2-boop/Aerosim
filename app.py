import streamlit as st

# 1. INITIAL CONFIGURATION
st.set_page_config(page_title="Avionix Systems", layout="wide")

# Initialize session state to track which page we are on
if 'page' not in st.session_state:
    st.session_state.page = 'opening'

# 2. STEP 1: OPENING PAGE (Full Wallpaper + Tap Button)
if st.session_state.page == 'opening':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1517976487492-5750f3195933");
            background-size: cover;
            font-family: 'Courier New', Courier, monospace;
        }
        .enter-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.title("🚀 AVIONIX SYSTEMS")
    st.write("ORBITAL COMMAND & ENGINEERING SUITE")
    if st.button("TAP TO ENTER DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# 3. STEP 2: DASHBOARD (Dark Aviation Wallpaper + Module List)
elif st.session_state.page == 'dashboard':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1436491865332-7a61a109c0f3?q=80&w=2070");
            background-size: cover;
            font-family: 'Courier New', Courier, monospace;
            color: #FFFFFF;
        }
        .main { background: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 15px; }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("🛡️ ENGINEERING DASHBOARD")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### EASA PART-66 MODULES")
        # List of the first 7 modules as requested
        modules = ["M1: Mathematics", "M2: Physics", "M3: Electrical", "M4: Electronic", "M5: Digital", "M6: Materials", "M7: Maintenance"]
        selected_mod = st.radio("SELECT MISSION:", modules)
        
    with col2:
        st.markdown("### HIGH MATHEMATICAL MOTION")
        st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", caption="Quantum Dynamics Analysis")
        st.write("System Status: All 14 modules initialized. Currently viewing selected module data.")
        if st.button("OPEN MODULE PAGE"):
            st.session_state.page = 'module_page'
            st.rerun()

# elif st.session_state.page == 'module_page':
    st.markdown("<style>.stApp { background: #000000; font-family: 'Courier New', monospace; }</style>", unsafe_allow_html=True)
    st.title("🛰️ SYSTEM MODULES: 1 - 14")
    
    # First 7 Modules (Previously added)
    st.header("1. Mathematics")
    st.write("Algebra, Geometry, and A/L prep formulas.")
    
    # ... (Keep 2 through 7 here) ...

    # Adding the final 7 Modules
    st.header("8. Basic Aerodynamics")
    st.write("Atmospheric physics and airflow principles.")
    
    st.header("9. Human Factors")
    st.write("Human performance, social psychology, and safety.")
    
    st.header("10. Aviation Legislation")
    st.write("Regulatory frameworks and EASA rules.")
    
    st.header("11. Turbine Aeroplane Aerodynamics")
    st.write("Structures and systems for high-speed flight.")
    
    st.header("12. Helicopter Aerodynamics")
    st.write("Rotary wing theory and flight controls.")
    
    st.header("13. Aircraft Aerodynamics & Systems")
    st.write("Detailed avionics and airframe structures.")
    
    st.header("14. Propulsion")
    st.write("Turbine and Rocket engine theory (Propulsion).")
    
    if st.button("BACK TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun(). 

    