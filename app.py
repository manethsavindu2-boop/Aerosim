import streamlit as st

# 1. SETUP & FONT CONFIGURATION
st.set_page_config(page_title="Avionix Systems Pro", layout="wide")

# Applying the "Coding Type" Font (Courier New) globally
st.markdown(
    """
    <style>
    * {
        font-family: 'Courier New', Courier, monospace !important;
    }
    .stApp {
        background-color: #000000;
    }
    </style>
    """, unsafe_allow_html=True
)

if 'page' not in st.session_state:
    st.session_state.page = 'opening'

# 2. STEP 1: OPENING PAGE
if st.session_state.page == 'opening':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1517976487492-5750f3195933");
            background-size: cover;
            background-position: center;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.title("🚀 AVIONIX SYSTEMS")
    st.write("ORBITAL COMMAND & ENGINEERING")
    # Tap to enter the dashboard as requested
    if st.button("TAP TO ENTER DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# 3. STEP 2: DASHBOARD
elif st.session_state.page == 'dashboard':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1436491865332-7a61a109c0f3");
            background-size: cover;
            color: #FFFFFF;
        }
        .main-content {
            background: rgba(0, 0, 0, 0.8);
            padding: 25px;
            border-radius: 15px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    with st.container():
        st.title("🛡️ ENGINEERING DASHBOARD")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### EASA PART-66 MODULES")
            st.write("Select a module to view system facts.")
            # Modules 1-14 selection list
            module_choice = st.radio("SELECT MISSION:", [f"Module {i}" for i in range(1, 15)])
            
        with col2:
            # High mathematical motion imagery
            st.markdown("### HIGH MATHEMATICAL MOTION")
            st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", caption="Quantum Dynamics & System Facts")
            if st.button("CONTINUE TO MODULE PAGES"):
                st.session_state.page = 'module_page'
                st.rerun()

# 4. STEP 3: CONTINUOUS MODULE PAGE (1-14)
elif st.session_state.page == 'module_page':
    st.title("🛰️ EASA PART-66: FULL LIBRARY")
    
    # Descriptions for all 14 modules in a continuous scrolling format
    modules_data = {
        "1": "Mathematics: Arithmetic, Algebra, and Geometry (A/L Prep).",
        "2": "Physics: Matter, Statics, Dynamics, and Thermodynamics.",
        "3": "Electrical Fundamentals: Electron theory and DC circuits.",
        "4": "Electronic Fundamentals: Semiconductors and logic gates.",
        "5": "Digital Techniques: Electronic Instrument Systems.",
        "6": "Materials & Hardware: Aircraft materials and hardware.",
        "7": "Maintenance Practices: Engineering drawings and safety.",
        "8": "Basic Aerodynamics: Atmosphere and airflow theory.",
        "9": "Human Factors: Psychology and safety management.",
        "10": "Aviation Legislation: Regulatory framework and rules.",
        "11": "Turbine Aeroplane Aerodynamics: Systems and structures.",
        "12": "Helicopter Aerodynamics: Rotary wing theory.",
        "13": "Aircraft Aerodynamics & Systems: Avionics and structures.",
        "14": "Propulsion: Turbine and Rocket engine theory."
    }

    for num, desc in modules_data.items():
        st.header(f"Module {num}")
        st.write(desc)
        st.markdown("---")
        
    if st.button("BACK TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()