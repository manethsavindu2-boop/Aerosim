import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් සහ සුදු වර්ණ අකුරු සැකසීමේ ශ්‍රිතය
def apply_avionix_design(bg_url, overlay_opacity=0.4):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,{overlay_opacity}), rgba(0,0,0,{overlay_opacity})), url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* සියලුම අකුරු සුදු පැහැයෙන් (Strong White Font) */
        * {{ 
            font-family: 'Segoe UI', Arial, sans-serif !important; 
            color: white !important; 
            text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
        }}
        .stButton>button {{
            background-color: rgba(255, 255, 255, 0.15);
            color: white !important;
            border: 2px solid white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }}
        .status-box {{
            background-color: rgba(0, 255, 0, 0.1);
            border: 1px solid #00FF00;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }}
        .info-panel {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 25px;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.2);
            margin-bottom: 20px;
        }}
        /* Sidebar අකුරුත් සුදු කිරීම */
        [data-testid="stSidebar"] * {{
            color: white !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (LIGHT VERSION) ---
if st.session_state.page == 'master':
    # ISS Wallpaper - High Brightness
    apply_avionix_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", overlay_opacity=0.2)
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="info-panel">
        <h1 style="font-size: 45px; color: white;">WELCOME TO AVIONIX SYSTEMS</h1>
        <p style="font-size: 20px; color: white;">The next generation of aerospace maintenance and technical simulation.</p>
        <hr style="border: 1px solid white;">
        <p style="color: white;">Current Status: <b>SYSTEMS ONLINE / LIGHT MODE ACTIVE</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ENTER MISSION CONTROL"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (SR-71 BLACKBIRD & CORRECTED ICONS) ---
elif st.session_state.page == 'dashboard':
    # ඔබ ලබාදුන් image_5d947e.png රූපය Dashboard Wallpaper ලෙස (SR-71)
    apply_avionix_design("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6f9Y98nOn9R1M9K_u9O2H8Y8O-Y6Fm9M2Gg&s", overlay_opacity=0.5)
    
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.title("🎛️ MISSION CONTROL DASHBOARD")
    with col_t2:
        # Server Status Panel
        st.markdown("""<div class="status-box"><span style='color: #00FF00;'>● SERVER STATUS: ONLINE</span><br><small>LATENCY: 24ms</small></div>""", unsafe_allow_html=True)

    st.write("---")

    # නිවැරදි කරන ලද 3D Icons (Turbofan, Fuselage, Avionics)
    st.subheader("🚀 CORE AIRCRAFT COMPONENTS")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211501.png", caption="TURBOFAN ENGINE UNIT", width=200)
    with c2:
        st.image("https://cdn-icons-png.flaticon.com/512/723/723961.png", caption="FUSELAGE & AIRFRAME", width=200)
    with c3:
        st.image("https://cdn-icons-png.flaticon.com/512/2014/2014521.png", caption="AVIONICS FLIGHT DECK", width=200)

    st.write("---")

    # Part 66 සහ Objectives පිළිබඳ දීර්ඝ විස්තරය
    st.markdown("""
    <div class="info-panel">
        <h3 style="color: #00E5FF;">📘 EASA PART 66 ENGINEERING STANDARDS</h3>
        <p style="text-align: justify; color: white;">
            EASA Part 66 යනු යුරෝපීය ගුවන් සේවා ආරක්ෂණ ඒජන්සිය (EASA) විසින් පනවනු ලබන ජාත්‍යන්තර ප්‍රමිතියකි. 
            මෙමගින් ගුවන් යානා නඩත්තු ඉංජිනේරුවෙකු සතු විය යුතු තාක්ෂණික නිපුනතාව සහ බලපත්‍ර අවශ්‍යතා තීරණය කරයි. 
            <b>Avionix Systems</b> හරහා අප බලාපොරොත්තු වන්නේ මෙම මොඩියුලයන් පිළිබඳ නිවැරදි අවබෝධයක් සිසුන් වෙත ලබාදීමයි.
        </p>
        <h3 style="color: #00E5FF;">🎯 OUR STRATEGIC OBJECTIVES</h3>
        <ul style="color: white;">
            <li><b>Educational Digitization:</b> තාක්ෂණික ඉගැන්වීම් ඩිජිටල්කරණය කිරීම.</li>
            <li><b>Safety First:</b> ගුවන් පද්ධතිවල ක්‍රියාකාරීත්වය සහ ආරක්ෂාව විශ්ලේෂණය කිරීම.</li>
            <li><b>Future Engineering:</b> අනාගත අභ්‍යවකාශ ඉංජිනේරුවන් සඳහා අවශ්‍ය මගපෙන්වීම ලබාදීම.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    if st.button("PROCEED TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()
    
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULES PAGE ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images.unsplash.com/photo-1517976384346-3136801d605d")
    st.title("📂 ENGINEERING MODULES")
    
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    st.write(f"### Loading Data for {mod}...")
    st.line_chart(np.random.randn(20, 1))
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()