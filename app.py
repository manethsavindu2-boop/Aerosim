import streamlit as st

# Page configuration (මෙය සැමවිටම මුලින්ම තිබිය යුතුය)
st.set_page_config(page_title="Avionix Master Core", layout="wide")

# Session state initialization (පිටු අතර මාරුවීම සඳහා)
if 'page' not in st.session_state:
    st.session_state.page = 'master'

# --- BACKGROUND HELPER FUNCTION ---
def set_module_background(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-attachment: fixed;
            background-size: cover;
        }}
        .main {{
            background-color: rgba(0, 0, 0, 0.7); /* අකුරු කියවීමට පහසු වන ලෙස අඳුරු ස්ථරයක් */
            color: white;
            padding: 2rem;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- MASTER PAGE ---
if st.session_state.page == 'master':
    # මෙහි කිසිදු Wallpaper වෙනසක් සිදු නොවේ (මුල් පෙනුම එලෙසම පවතී)
    st.title("🛰️ AVIONIX MASTER CORE")
    st.header("WELCOME TO AVIONIX SYSTEMS")
    st.write("The next generation of aerospace maintenance and technical simulation.")
    
    if st.button("ENTER MISSION CONTROL"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- DASHBOARD ---
elif st.session_state.page == 'dashboard':
    # මෙහිද Wallpaper වෙනසක් සිදු නොවේ
    st.title("🎛️ MISSION CONTROL DASHBOARD")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Module 01: Mathematics"):
            st.session_state.page = 'module_01'
            st.rerun()
    with col2:
        if st.button("Module 02: Physics"):
            st.session_state.page = 'module_02'
            st.rerun()

# --- MODULE 01 (Aerospace Wallpaper ඇතුළත් කර ඇත) ---
elif st.session_state.page == 'module_01':
    # ISS Wallpaper for Module 01
    set_module_background("https://images-assets.nasa.gov/image/iss067e357555/iss067e357555~orig.jpg")
    
    st.header("📘 EASA PART 66 - MODULE 01")
    st.subheader("[ENGLISH] - Mathematics")
    st.write("Arithmetic, Algebra, and Geometry fundamentals for Aircraft Maintenance.")
    
    if st.button("Back to Dashboard"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- MODULE 02 (Aerospace Wallpaper ඇතුළත් කර ඇත) ---
elif st.session_state.page == 'module_02':
    # Another Aerospace Wallpaper for Module 02
    set_module_background("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg")
    
    st.header("📕 EASA PART 66 - MODULE 02")
    st.subheader("[ENGLISH] - Physics")
    st.write("Statics, Dynamics, and Thermodynamics in Aviation.")
    
    if st.button("Back to Dashboard"):
        st.session_state.page = 'dashboard'
        st.rerun()