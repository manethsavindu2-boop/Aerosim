import streamlit as st

# INITIAL SETTINGS
st.set_page_config(page_title="Avionix Systems Pro", layout="wide")

# GLOBAL FONT: Monospace "Coding Type" font
st.markdown(
    """
    <style>
    * {
        font-family: 'Courier New', Courier, monospace !important;
    }
    </style>
    """, unsafe_allow_html=True
)

# Page Navigation Logic
if 'page' not in st.session_state:
    st.session_state.page = 'step1'

# --- STEP 1: OPENING PAGE ---
if st.session_state.page == 'step1':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa");
            background-size: cover;
            background-position: center;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.title("🚀 AVIONIX SYSTEMS")
    st.subheader("ORBITAL COMMAND INTERFACE")
    
    # Mention tap to enter as requested in document
    if st.button("TAP TO ENTER DASHBOARD"):
        st.session_state.page = 'step2'
        st.rerun()

# --- STEP 2: DASHBOARD (Font Changed to Dark) ---
elif st.session_state.page == 'step2':
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1534067783941-51c9c23ecefd");
            background-size: cover;
        }
        /* Target the main text to be dark as requested */
        .main-container, p, h1, h2, h3, .stMarkdown, .stText {
            color: #1A1A1A !important; 
            font-weight: bold;
        }
        /* Adjusting button visibility on dark-font dashboard */
        .stButton>button {
            color: #FFFFFF !important;
            background-color: #1A1A1A !important;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("🛡️ MISSION CONTROL DASHBOARD")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### EASA PART-66 MODULES")
        # List of modules from document
        st.write("1. Mathematics")
        st.write("2. Physics")
        st.write("3. Electrical")
        st.write("4. Electronics")
        st.write("5. Digital Tech")
        st.write("6. Materials")
        st.write("7. Maintenance")
        st.write("... and 7 more.")
        
    with col2:
        st.markdown("### HIGH MATHEMATICAL MOTION")
        # High math/physics image as requested
        st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", caption="Quantum Motion Analysis")
        if st.button("PROCEED TO MODULES"):
            st.session_state.page = 'step3'
            st.rerun()

# --- STEP 3: ONE PAGE CONTINUOUS MODULES ---
elif st.session_state.page == 'step3':
    st.markdown("<style>.stApp { background: #000000; color: #FFFFFF; }</style>", unsafe_allow_html=True)
    st.title("🛰️ SYSTEM MODULES: 1 - 14")
    st.info("Continuous scrolling engineering data enabled.")
    
    modules = [
        "Mathematics (A/L Prep)", "Physics (EASA)", "Electrical Fundamentals", 
        "Electronic Fundamentals", "Digital Techniques", "Materials & Hardware", 
        "Maintenance Practices", "Basic Aerodynamics", "Human Factors", 
        "Aviation Legislation", "Turbine Aeroplane Aerodynamics", 
        "Helicopter Aerodynamics", "Aircraft Aerodynamics & Systems", "Propulsion"
    ]

    for index, name in enumerate(modules, start=1):
        st.header(f"Module {index}: {name}")
        st.write(f"System facts and engineering logic for {name} initialized.")
        st.markdown("---")
    
    if st.button("BACK TO DASHBOARD"):
        st.session_state.page = 'step2'
        st.rerun()