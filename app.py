import streamlit as st

# 1. INITIAL CONFIGURATION
st.set_page_config(page_title="Avionix Systems Pro", layout="wide")

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'opening'

# 2. STEP 1: OPENING PAGE (Full Wallpaper)
if st.session_state.page == 'opening':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1517976487492-5750f3195933");
            background-size: cover;
            font-family: 'Courier New', monospace;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.title("🚀 AVIONIX SYSTEMS")
    st.subheader("ORBITAL COMMAND & ENGINEERING")
    if st.button("TAP TO ENTER DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# 3. STEP 2: DASHBOARD (Dark Aviation + Math Motion)
elif st.session_state.page == 'dashboard':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1436491865332-7a61a109c0f3");
            background-size: cover;
            font-family: 'Courier New', monospace;
            color: #FFFFFF;
        }
        .main { background: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 15px; }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("🛡️ ENGINEERING DASHBOARD")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### EASA PART-66 MISSIONS")
        st.write("Modules 1 - 14 Initialized")
        st.radio("CURRENT STATUS:", ["All Systems Go", "Awaiting Input"])
        
    with col2:
        st.markdown("### HIGH MATHEMATICAL MOTION")
        st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", caption="Quantum Dynamics Analysis")
        if st.button("OPEN ALL 14 MODULES"):
            st.session_state.page = 'module_page'
            st.rerun()

# 4. STEP 3: FULL 14 MODULE LIBRARY (Continuous Page)
elif st.session_state.page == 'module_page':
    st.markdown("<style>.stApp { background: #000000; font-family: 'Courier New', monospace; color: white; }</style>", unsafe_allow_html=True)
    st.title("🛰️ EASA PART-66: COMPLETE MODULE LIBRARY")
    
    # Continuous scrolling list of 14 modules
    module_list = [
        ("M1: Mathematics", "Arithmetic, Algebra, Geometry, and A/L prep."),
        ("M2: Physics", "Matter, Statics, Dynamics, and Thermodynamics."),
        ("M3: Electrical Fundamentals", "Electron theory, DC, and AC circuits."),
        ("M4: Electronic Fundamentals", "Semiconductors and Printed Circuit Boards."),
        ("M5: Digital Techniques", "Data buses, Fiber optics, and Logic gates."),
        ("M6: Materials & Hardware", "Aircraft metals, composites, and fasteners."),
        ("M7: Maintenance Practices", "Tools, safety, and engineering drawings."),
        ("M8: Basic Aerodynamics", "Airflow, atmosphere, and flight theory."),
        ("M9: Human Factors", "Social psychology, health, and error management."),
        ("M10: Aviation Legislation", "EASA regulatory framework and safety rules."),
        ("M11: Turbine Aeroplane Aerodynamics", "Structures and systems for turbine aircraft."),
        ("M12: Helicopter Aerodynamics", "Rotary wing theory and flight controls."),
        ("M13: Aircraft Aerodynamics & Systems", "Advanced avionics and airframes."),
        ("M14: Propulsion", "Turbine and rocket engine theory.")
    ]
    
    for title, desc in module_list:
        st.header(title)
        st.write(desc)
        st.markdown("---")
    
    if st.button("BACK TO COMMAND CENTER"):
        st.session_state.page = 'dashboard'
        st.rerun()