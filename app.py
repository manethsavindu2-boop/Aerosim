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
        /* විස්තරය විශාල කර පෙන්වීමට අලුත් class එකක් */
        .large-desc {{
            font-size: 20px !important;
            line-height: 1.6;
            margin-bottom: 20px;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- STEP 1: MASTER PAGE ---
if st.session_state.page == 'master':
    apply_avionix_design("https://images.unsplash.com/photo-1451187580459-43490279c0fa", overlay_opacity=0.2)
    st.title("🛰️ AVIONIX MASTER CORE")
    st.markdown('<div class="info-panel"><h1 style="font-size: 45px;">WELCOME TO AVIONIX SYSTEMS</h1><p style="font-size: 20px;">The next generation of aerospace maintenance and technical simulation.</p></div>', unsafe_allow_html=True)
    if st.button("ENTER MISSION CONTROL"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- STEP 2: DASHBOARD (විස්තරය භාෂා 6 කින් සහ විශාලව) ---
elif st.session_state.page == 'dashboard':
    apply_avionix_design("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", overlay_opacity=0.6)
    
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.title("🎛️ MISSION CONTROL DASHBOARD")
    with col_t2:
        st.markdown("""<div class="status-box"><span style='color: #00FF00;'>● SERVER STATUS: ONLINE</span><br><small>LATENCY: 24ms</small></div>""", unsafe_allow_html=True)

    st.write("---")
    st.markdown('<div class="info-panel">', unsafe_allow_html=True)
    st.header("📘 EASA PART 66 & GLOBAL OBJECTIVES")
    
    # භාෂා 6 කින් විස්තරය (විශාල අකුරින්)
    st.markdown("""
    <div class="large-desc">
        <b>[ENGLISH]</b><br>
        EASA Part 66 is the common European standard for aircraft maintenance personnel. Our objective is to provide high-level technical simulation to bridge the gap between theory and practical engineering excellence.<br><br>
        <b>[DEUTSCH - GERMAN]</b><br>
        EASA Part 66 ist der gemeinsame europäische Standard für Personal in der Luftfahrzeuginstandhaltung. Unser Ziel ist es, hochwertige technische Simulationen anzubieten, um die Lücke zwischen Theorie und praktischer technischer Exzellenz zu schließen.<br><br>
        <b>[FRANÇAIS - FRENCH]</b><br>
        L'EASA Part 66 est la norme européenne commune pour le personnel de maintenance des aéronefs. Notre objectif est de fournir une simulation technique de haut niveau pour combler le fossé entre la théorie et l'excellence en ingénierie pratique.<br><br>
        <b>[РУССКИЙ - RUSSIAN]</b><br>
        EASA Part 66 — это единый европейский стандарт для персонала по техническому обслуживанию воздушных судов. Наша цель — обеспечить высокоуровневое техническое моделирование, чтобы восполнить пробел между теорией и практическим инженерным мастерством.<br><br>
        <b>[日本語 - JAPANESE]</b><br>
        EASA Part 66は、航空機整備士のための共通の欧州標準規格です。当社の目標は、高度な技術シミュレーションを提供し、理論と実技の卓越したエンジニアリングの間のギャップを埋めることです。<br><br>
        <b>[中文 - CHINESE]</b><br>
        EASA Part 66 是飞机维修人员的通用欧洲标准。我们的目标是提供高水平的技术仿真，以弥补理论与实际工程卓越表现之间的差距。
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("🎯 CORE MISSIONS")
    st.write("* **Innovation:** Pioneering new ways to learn aerospace modules.")
    st.write("* **Precision:** Accurate data visualization for flight safety.")
    st.write("* **Global Standards:** Aligning with international aviation regulations.")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("PROCEED TO MODULES"):
        st.session_state.page = 'modules'
        st.rerun()
    if st.button("BACK TO MASTER"):
        st.session_state.page = 'master'
        st.rerun()

# --- STEP 3: MODULES PAGE ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    # --- MODULE 1 (MATHEMATICS) START ---
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS")
        
        # Theory Section
        st.subheader("📚 Key Mathematical Theory")
        t_col1, t_col2 = st.columns(2)
        
        with t_col1:
            st.markdown("#### 🔢 Arithmetic & Algebra")
            st.write("""
            * **BODMAS/PEMDAS:** The order of operations: Brackets, Orders, Division/Multiplication, Addition/Subtraction.
            * **Indices:** Rules for powers. E.g., $a^m \\times a^n = a^{m+n}$ and $(a^m)^n = a^{mn}$.
            * **Logarithms:** Inverse of exponentiation. $\\log_b(x) = y$ is equivalent to $b^y = x$.
            """)
            
        with t_col2:
            st.markdown("#### 📐 Geometry & Trigonometry")
            st.write("""
            * **Pythagoras Theorem:** In a right-angled triangle, $a^2 + b^2 = c^2$.
            * **Trigonometric Ratios:** SOH (Sine), CAH (Cosine), TOA (Tangent).
            * **Circle Geometry:** Circumference = $2\\pi r$, Area = $\\pi r^2$.
            """)

        st.write("---")
        
        # Calculation Section
        st.subheader("⚙️ Technical Calculations")
        c_col1, c_col2 = st.columns(2)
        
        with c_col1:
            st.markdown("#### 🏎️ Engine Compression Ratio")
            vs = st.number_input("Swept Volume ($V_s$):", value=500.0, step=10.0)
            vc = st.number_input("Clearance Volume ($V_c$):", value=50.0, step=5.0)
            if vc > 0:
                cr = (vs + vc) / vc
                st.success(f"Compression Ratio: **{cr:.2f} : 1**")
            else:
                st.error("Clearance Volume must be greater than 0")

        with c_col2:
            st.markdown("#### 📏 Area & Circumference")
            radius = st.number_input("Enter Radius (cm):", value=10.0, step=1.0)
            area = np.pi * (radius ** 2)
            circum = 2 * np.pi * radius
            st.info(f"Area: **{area:.2f} cm²**")
            st.info(f"Circumference: **{circum:.2f} cm**")
            
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 1 (MATHEMATICS) END ---

    # අතවශ්‍යයි: අනෙකුත් Module සඳහා Default පණිවිඩය මෙසේ වෙනස් කරන්න
    elif mod != "Module 1":
        st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3>', unsafe_allow_html=True)
        st.line_chart(np.random.randn(20, 1))
        st.markdown('</div>', unsafe_allow_html=True)
    st.title("📂 ENGINEERING MODULES")
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])
    st.markdown(f'<div class="info-panel"><h3>Loading {mod} Data...</h3>', unsafe_allow_html=True)
    st.line_chart(np.random.randn(20, 1))
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("RETURN TO DASHBOARD"):
        st.session_state.page = 'dashboard'
        st.rerun()