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
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE (LIGHT VERSION) ---
if st.session_state.page == 'master':
    apply_avionix_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", overlay_opacity=0.2)
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="info-panel">
        <h1 style="font-size: 45px;">AVIONIX SYSTEMS</h1>
        <p style="font-size: 20px;">Precision Engineering & Aerospace Simulation Portal</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ENTER DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: UPDATED DASHBOARD (ISS WALLPAPER & AIRCRAFT PARTS) ---
elif st.session_state.page == 'dashboard':
    # Dashboard එක සඳහා ISS Wallpaper එකක් භාවිතා කර ඇත
    apply_avionix_design("https://images.unsplash.com/photo-1541185933-ef5d8ed016c2", overlay_opacity=0.5)
    
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.title("🎛️ MISSION CONTROL DASHBOARD")
    with col_t2:
        # Server Status පැනලය
        st.markdown("""<div class="status-box"><span style='color: #00FF00;'>● SERVER STATUS: ONLINE</span><br><small>LATENCY: 24ms</small></div>""", unsafe_allow_html=True)

    st.write("---")

    # ගුවන් යානා කොටස් 3 (3D Style Icons)
    st.subheader("🚀 CORE AIRCRAFT COMPONENTS")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/2805/2805901.png", caption="TURBOFAN ENGINE UNIT", width=200)
    with c2:
        st.image("https://cdn-icons-png.flaticon.com/512/3211/3211475.png", caption="FUSELAGE & AIRFRAME", width=200)
    with c3:
        st.image("https://cdn-icons-png.flaticon.com/512/1022/1022321.png", caption="AVIONICS FLIGHT DECK", width=200)

    st.write("---")

    # EASA Part 66 සහ Objectives පිළිබඳ දීර්ඝ විස්තරය
    st.markdown("""
    <div class="info-panel">
        <h3 style="color: #00E5FF;">📘 EASA PART 66 ENGINEERING STANDARDS</h3>
        <p style="text-align: justify;">
            EASA Part 66 යනු යුරෝපීය ගුවන් සේවා ආරක්ෂණ ඒජන්සිය (European Union Aviation Safety Agency) විසින් නිකුත් කරනු ලබන, 
            ගුවන් යානා නඩත්තු ඉංජිනේරුවෙකු (Aircraft Maintenance Engineer) වීමට අවශ්‍ය මූලික බලපත්‍ර ප්‍රමිතියයි. මෙහිදී ගණිතය (Module 1), 
            භෞතික විද්‍යාව (Module 2), සහ විදුලි ඉංජිනේරු විද්‍යාව වැනි විෂයයන් 17ක් පමණ ආවරණය කෙරේ. <b>Avionix Systems</b> හරහා 
            අප බලාපොරොත්තු වන්නේ මෙම සංකීර්ණ මොඩියුලයන් තාක්ෂණික සිමියුලේෂන් (Simulations) මගින් වඩාත් සරලව ඉගෙනීමට පහසුකම් සැලසීමයි.
        </p>
        <h3 style="color: #00E5FF;">🎯 OUR STRATEGIC OBJECTIVES</h3>
        <ul>
            <li><b>Educational Digitization:</b> ගුවන් යානා තාක්ෂණික පාඩම් ඩිජිටල්කරණය කර පහසුවෙන් ලබාදීම.</li>
            <li><b>Safety First:</b> ගුවන් යානා අනතුරු (Crashes) විශ්ලේෂණය කර ඒවා වළක්වා ගන්නා ආකාරය ඉගැන්වීම.</li>
            <li><b>Innovation:</b> ශ්‍රී ලංකාව තුළ අභ්‍යවකාශ තාක්ෂණය පිළිබඳ උනන්දුවක් දක්වන තරුණ පරපුරට අවශ්‍ය මගපෙන්වීම ලබාදීම.</li>
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
    st.write(f"### Accessing technical data for {mod}...")
    st.line_chart(np.random.randn(20, 1))
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()