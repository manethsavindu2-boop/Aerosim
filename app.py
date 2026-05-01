import streamlit as st

# INITIAL SETTINGS
st.set_page_config(page_title="Avionix Systems Pro", layout="wide")

# GLOBAL FONT: Applying "Coding Type" font (Monospace) to everything
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
        .center-btn {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 70vh;
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

# --- STEP 2: DASHBOARD ---
elif st.session_state.page == 'step2':
    st.markdown(
        """
        <style>
        /* High-quality dark aviation background for the whole page */
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1559103816-9524679930f3?q=80&w=2070");
            background-size: cover;
            background-position: center;
        }
        /* Changing Dashboard font to Dark and removing the black box */
        h1, h2, h3, p, label, .stMarkdown {
            color: #1A1A1A !important;  /* Dark Charcoal font for clarity */
            font-weight: 700;
        }
        /* Ensuring the radio button text is also dark */
        .stWidget label {
            color: #1A1A1A !important;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("🛡️ MISSION CONTROL DASHBOARD")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### EASA PART-66 MODULES")
        # List of the first 7 modules for the dashboard view
        st.write("1. Mathematics")
        st.write("2. Physics")
        st.write("3. Electrical Fundamentals")
        st.write("4. Electronic Fundamentals")
        st.write("5. Digital Techniques")
        st.write("6. Materials & Hardware")
        st.write("7. Maintenance Practices")
        st.write("---")
        st.write("Modules 8-14 Initialized in Backend")
        
    with col2:
        st.markdown("### HIGH MATHEMATICAL MOTION")
        # A suitable aviation/engineering image to replace the old black one
        st.image("https://images.unsplash.com/photo-1559297434-2d8a134e0428?q=80&w=2070", caption="Aerospace Structural Analysis")
        
        if st.button("PROCEED TO ALL 14 MODULES"):
            st.session_state.page = 'step3'
            st.rerun()