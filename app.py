import streamlit as st
import pandas as pd
import numpy as np

# --- 1. පද්ධති සැකසුම් (SYSTEM CONFIG) ---
st.set_page_config(page_title="Avionix Systems v1.0", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'master'

# පසුබිම් සහ සුදු වර්ණ අකුරු සැකසීමේ ශ්‍රිතය
def apply_avionix_design(bg_url, overlay_opacity=0.5):
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
            background-color: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.2);
            margin-bottom: 25px;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE ---
if st.session_state.page == 'master':
    apply_avionix_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", overlay_opacity=0.2)
    st.title("🛰️ AVIONIX MASTER CORE")
    
    st.markdown("""
    <div class="info-panel">
        <h1 style="font-size: 45px;">WELCOME TO AVIONIX SYSTEMS</h1>
        <p style="font-size: 20px;">The next generation of aerospace maintenance and technical simulation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ENTER MISSION CONTROL"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (ISS WALLPAPER & MULTILINGUAL DESCRIPTION) ---
elif st.session_state.page == 'dashboard':
    # ISS Wallpaper for Dashboard
    apply_avionix_design("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", overlay_opacity=0.6)
    
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.title("🎛️ MISSION CONTROL DASHBOARD")
    with col_t2:
        st.markdown("""<div class="status-box"><span style='color: #00FF00;'>● SERVER STATUS: ONLINE</span><br><small>LATENCY: 24ms</small></div>""", unsafe_allow_html=True)

    st.write("---")

    # Multilingual Descriptions
    st.markdown("""
    <div class="info-panel">
        <h2 style="color: #00E5FF;">📘 EASA PART 66 & OBJECTIVES</h2>
        
        <p><b>[ENGLISH]</b><br>
        EASA Part 66 is the common European standard for aircraft maintenance personnel. Our objective is to provide high-level technical simulation to bridge the gap between theory and practical engineering excellence.</p>
        
        <p><b>[DEUTSCH - GERMAN]</b><br>
        EASA Part 66 ist der gemeinsame europäische Standard für Personal in der Luftfahrzeuginstandhaltung. Unser Ziel ist es, hochwertige technische Simulationen anzubieten, um die Lücke zwischen Theorie und praktischer technischer Exzellenz zu schließen.</p>
        
        <p><b>[ITALIANO - ITALIAN]</b><br>
        EASA Part 66 è lo standard europeo comune per il personale addetto alla manutenzione degli aeromobili. Il nostro obiettivo è fornire simulazioni tecniche di alto livello per colmare il divario tra teoria ed eccellenza ingegneristica pratica.</p>
        
        <p><b>[FRANÇAIS - FRENCH]</b><br>
        L'EASA Part 66 est la norme européenne commune pour le personnel de maintenance des aéronefs. Notre objectif est de fournir une simulation technique de haut niveau pour combler le fossé entre la théorie et l'excellence de l'ingénierie pratique.</p>
        
        <hr style="border: 1px solid rgba(255,255,255,0.3);">
        <h3 style="color: #00E5FF;">🎯 CORE MISSIONS</h3>
        <ul>
            <li><b>Innovation:</b> Pioneering new ways to learn aerospace modules.</li>
            <li><b>Precision:</b> Accurate data visualization for flight safety.</li>
            <li><b>Global Standards:</b> Aligning with international aviation regulations.</li>
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
    st.write(f"### Loading {mod} Data...")
    st.line_chart(np.random.randn(20, 1))
    
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()