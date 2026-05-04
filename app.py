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
# --- STEP 3: MODULES PAGE ---
elif st.session_state.page == 'modules':
    apply_avionix_design("https://images-assets.nasa.gov/image/iss064e007861/iss064e007861~orig.jpg", overlay_opacity=0.7)
    st.title("📂 ENGINEERING MODULES")
    
    # පළමුව mod variable එක මෙහිදී define කරන්න
    mod = st.selectbox("SELECT MODULE", [f"Module {i}" for i in range(1, 15)])

    # දැන් mod variable එක පරීක්ෂා කරන්න
    if mod == "Module 1":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📘 MODULE 01: MATHEMATICS")
        
        # Theory Section
        st.subheader("📚 Key Mathematical Theory")
        t_col1, t_col2 = st.columns(2)
        
        with t_col1:
            st.markdown("#### 🔢 Arithmetic & Algebra")
            st.write("""
            * **BODMAS:** Brackets, Orders, Division/Multiplication, Addition/Subtraction.
            * **Indices:** $a^m \\times a^n = a^{m+n}$
            * **Logarithms:** $\\log_b(x) = y \Rightarrow b^y = x$.
            """)
            
        with t_col2:
            st.markdown("#### 📐 Geometry & Trigonometry")
            st.write("""
            * **Pythagoras Theorem:** $a^2 + b^2 = c^2$.
            * **Circle Geometry:** Area = $\\pi r^2$, Circumference = $2\\pi r$.
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
                st.error("Clearance Volume must be > 0")

        with c_col2:
            st.markdown("#### 📏 Area & Circumference")
            radius = st.number_input("Enter Radius (cm):", value=10.0, step=1.0)
            area = np.pi * (radius ** 2)
            st.info(f"Area: **{area:.2f} cm²**")
            
        st.markdown('</div>', unsafe_allow_html=True)

    # --- MODULE 2 (PHYSICS) START ---
    elif mod == "Module 2":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📕 MODULE 02: PHYSICS")
        
        # Physics Theory Section
        st.subheader("📚 Key Physics Theory")
        p_col1, p_col2 = st.columns(2)
        
        with p_col1:
            st.markdown("#### 🏃 Statics & Kinetics")
            st.write("""
            * **Newton's 1st Law:** An object remains at rest or in uniform motion unless acted upon by a force.
            * **Newton's 2nd Law:** Force equals mass times acceleration ($F = m \\times a$).
            * **Newton's 3rd Law:** For every action, there is an equal and opposite reaction.
            * **Work:** Work is done when a force moves an object ($W = F \\times d$).
            """)
            
        with p_col2:
            st.markdown("#### 💨 Fluid Dynamics & Heat")
            st.write("""
            * **Bernoulli's Principle:** An increase in the speed of a fluid occurs simultaneously with a decrease in static pressure (Key to Aircraft Lift).
            * **Boyle's Law:** $P_1V_1 = P_2V_2$ (At constant temperature).
            * **Charles's Law:** $V_1/T_1 = V_2/T_2$ (At constant pressure).
            * **Density:** Mass per unit volume ($\\rho = m / V$).
            """)

        st.write("---")
        
        # Physics Calculation Section
        st.subheader("⚙️ Essential Physics Calculations")
        pc_col1, pc_col2 = st.columns(2)
        
        with pc_col1:
            st.markdown("#### ⚖️ Force & Acceleration")
            p_mass = st.number_input("Object Mass (kg):", value=10.0, step=1.0)
            p_acc = st.number_input("Acceleration (m/s²):", value=9.81, step=0.1)
            force_res = p_mass * p_acc
            st.success(f"Force (F): **{force_res:.2f} Newtons (N)**")
            
            st.markdown("#### 📏 Work Done")
            p_dist = st.number_input("Distance Moved (meters):", value=5.0, step=0.5)
            work_res = force_res * p_dist
            st.info(f"Work (W): **{work_res:.2f} Joules (J)**")

        with pc_col2:
            st.markdown("#### 🌊 Pressure & Density")
            p_force = st.number_input("Applied Force (N):", value=100.0, step=10.0, key="p_force")
            p_area = st.number_input("Surface Area (m²):", value=2.0, step=0.1)
            if p_area > 0:
                pressure = p_force / p_area
                st.warning(f"Pressure (P): **{pressure:.2f} Pascals (Pa)**")
            
            st.markdown("#### ⛽ Density Calculation")
            d_mass = st.number_input("Fluid Mass (kg):", value=50.0, step=1.0)
            d_vol = st.number_input("Fluid Volume (m³):", value=5.0, step=0.5)
            if d_vol > 0:
                density = d_mass / d_vol
                st.info(f"Density (ρ): **{density:.2f} kg/m³**")
            
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 3 (ELECTRICAL FUNDAMENTALS) START ---
    elif mod == "Module 3":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("⚡ MODULE 03: ELECTRICAL FUNDAMENTALS")
        
        # Electrical Theory Section
        st.subheader("📚 Key Electrical Theory")
        e_col1, e_col2 = st.columns(2)
        
        with e_col1:
            st.markdown("#### ⚡ Electron Theory & Static Electricity")
            st.write("""
            * **Structure of Matter:** Atoms consist of protons (+), neutrons, and electrons (-).
            * **Static Electricity:** Accumulation of charge on a surface; critical for aircraft bonding and earthing.
            * **Coulomb’s Law:** Force between two charges is proportional to their product and inversely to the square of the distance.
            """)
            
            st.markdown("#### 🔋 DC Sources & Ohm's Law")
            st.write("""
            * **Ohm's Law:** $V = I \\times R$ (Voltage = Current $\\times$ Resistance).
            * **Power:** $P = V \\times I$ or $P = I^2 \\times R$.
            * **Kirchhoff's Voltage Law (KVL):** The sum of voltages around any closed loop is zero.
            * **Kirchhoff's Current Law (KCL):** Total current entering a junction equals total current leaving.
            """)
            
        with e_col2:
            st.markdown("#### 🔌 Resistance & Capacitance")
            st.write("""
            * **Resistance Factors:** Length, cross-sectional area, material (resistivity), and temperature.
            * **Resistors in Series:** $R_{total} = R_1 + R_2 + ...$
            * **Resistors in Parallel:** $1/R_{total} = 1/R_1 + 1/R_2 + ...$
            * **Capacitance:** Storage of electric charge ($Q = C \\times V$).
            * **Magnetism:** Electromagnets and the motor/generator principles used in aircraft starters and alternators.
            """)

        st.write("---")
        
        # Electrical Calculation Section
        st.subheader("⚙️ Essential Electrical Calculations")
        ec_col1, ec_col2 = st.columns(2)
        
        with ec_col1:
            st.markdown("#### 🛠️ Ohm's Law & Power Tool")
            e_volt = st.number_input("Voltage (V):", value=28.0, step=1.0) # Aircraft DC standard
            e_res = st.number_input("Resistance (Ω):", value=4.0, step=0.1)
            
            if e_res > 0:
                e_curr = e_volt / e_res
                e_pwr = e_volt * e_curr
                st.success(f"Current (I): **{e_curr:.2f} Amperes (A)**")
                st.info(f"Power (P): **{e_pwr:.2f} Watts (W)**")
            else:
                st.error("Resistance must be greater than 0")

        with ec_col2:
            st.markdown("#### 🔌 Series vs Parallel Resistance")
            r1 = st.number_input("Resistor 1 (Ω):", value=10.0, step=1.0)
            r2 = st.number_input("Resistor 2 (Ω):", value=10.0, step=1.0)
            
            r_series = r1 + r2
            st.warning(f"Total Series Resistance: **{r_series:.2f} Ω**")
            
            if (r1 + r2) > 0:
                r_parallel = (r1 * r2) / (r1 + r2)
                st.success(f"Total Parallel Resistance: **{r_parallel:.2f} Ω**")
            
            st.markdown("#### 🔋 Capacitance Calculation")
            cap_c = st.number_input("Capacitance (Farads):", value=0.001, format="%.4f")
            cap_v = st.number_input("Voltage across Capacitor (V):", value=12.0)
            charge_q = cap_c * cap_v
            st.info(f"Stored Charge (Q): **{charge_q:.4f} Coulombs**")
            
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 4 (ELECTRONIC FUNDAMENTALS) START ---
    elif mod == "Module 4":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("🔌 MODULE 04: ELECTRONIC FUNDAMENTALS")
        
        et_col1, et_col2 = st.columns(2)
        with et_col1:
            st.markdown("#### 🧪 Semiconductors & Diodes")
            st.write("""
            * **P-N Junction:** The interface between P-type and N-type materials.
            * **Diodes:** Allows current flow in one direction; used for rectification (AC to DC).
            * **Zener Diode:** Used for voltage regulation in aircraft power units.
            """)
        with et_col2:
            st.markdown("#### 📟 Transistors")
            st.write("""
            * **NPN & PNP:** The two main types of Bipolar Junction Transistors (BJT).
            * **Functions:** Used as a switch or as an amplifier.
            * **Gain (β):** The relationship between base and collector current ($I_c / I_b$).
            """)

        st.write("---")
        st.subheader("⚙️ Electronic Calculations")
        elc1, elc2 = st.columns(2)
        with elc1:
            st.markdown("#### 📈 Transistor Current Gain")
            ib = st.number_input("Base Current ($I_b$ in μA):", value=100.0, step=10.0)
            ic = st.number_input("Collector Current ($I_c$ in mA):", value=10.0, step=1.0)
            beta = ic / (ib / 1000) if ib > 0 else 0
            st.success(f"Current Gain (β): **{beta:.2f}**")
        with elc2:
            st.markdown("#### 🔢 Logic Gate Simulator")
            gate = st.selectbox("Gate Type:", ["AND", "OR", "NAND", "NOR"], key="m4_gate")
            a = st.checkbox("Input A", key="m4_a")
            b = st.checkbox("Input B", key="m4_b")
            if gate == "AND": out = a and b
            elif gate == "OR": out = a or b
            elif gate == "NAND": out = not (a and b)
            else: out = not (a or b)
            st.info(f"Output: **{'1 (High)' if out else '0 (Low)'}**")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 5 (DIGITAL TECHNIQUES) START ---
    elif mod == "Module 5":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("🖥️ MODULE 05: DIGITAL TECHNIQUES")
        
        dt_col1, dt_col2 = st.columns(2)
        with dt_col1:
            st.markdown("#### 🔢 Number Systems")
            st.write("""
            * **Binary (Base 2):** Used by computers (0s and 1s).
            * **Hexadecimal (Base 16):** Used for memory addressing.
            * **Octal (Base 8):** Occasionally used in older systems.
            """)
        with dt_col2:
            st.markdown("#### ✈️ Aircraft Systems")
            st.write("""
            * **EFIS:** Electronic Flight Instrument System (Glass Cockpits).
            * **BITE:** Built-In Test Equipment for fault detection.
            * **EMI/HIRF:** Protection against Electromagnetic Interference.
            """)

        st.write("---")
        st.subheader("⚙️ Digital Data Tools")
        dc1, dc2 = st.columns(2)
        with dc1:
            st.markdown("#### 🔢 Decimal to Binary Converter")
            dec_num = st.number_input("Enter Decimal Number:", value=10, step=1)
            st.success(f"Binary Representation: **{bin(dec_num)[2:]}**")
        with dc2:
            st.markdown("#### 📊 Fiber Optics")
            st.write("Fiber optics use light pulses for data transmission, offering high speed and total immunity to EMI.")
            st.info("Calculation: Data Rate = Frequency $\\times$ Bit Depth")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 6 (MATERIALS & HARDWARE) START ---
    elif mod == "Module 6":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("🛠️ MODULE 06: MATERIALS & HARDWARE")
        
        mt_col1, mt_col2 = st.columns(2)
        with mt_col1:
            st.markdown("#### 🏗️ Aircraft Materials")
            st.write("""
            * **Ferrous:** Steels and iron alloys.
            * **Non-Ferrous:** Aluminum, Magnesium, Titanium (High strength-to-weight).
            * **Composites:** Carbon fiber, Glass fiber, Kevlar.
            """)
        with mt_col2:
            st.markdown("#### 🔩 Hardware & Fasteners")
            st.write("""
            * **Bolts:** AN, MS, and NAS standards.
            * **Rivets:** Solid rivets and blind rivets (Pop rivets).
            * **Corrosion:** Stress corrosion, Galvanic corrosion, and Fretting.
            """)

        st.write("---")
        st.subheader("⚙️ Hardware Engineering Tools")
        mc1, mc2 = st.columns(2)
        with mc1:
            st.markdown("#### 🏋️ Stress Analysis")
            force_m = st.number_input("Applied Load (N):", value=5000.0, key="m6_f")
            area_m = st.number_input("Cross Section Area (m²):", value=0.02, key="m6_a")
            stress = force_m / area_m if area_m > 0 else 0
            st.warning(f"Calculated Stress: **{stress/1e6:.2f} MPa**")
        with mc2:
            st.markdown("#### 🌡️ Thermal Expansion")
            orig_len = st.number_input("Original Length (m):", value=1.0)
            temp_diff = st.number_input("Temp Change (°C):", value=50.0)
            # Aluminum coefficient approx 23e-6
            exp = orig_len * 23e-6 * temp_diff
            st.info(f"Expansion (Aluminum): **{exp*1000:.3f} mm**")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 7 (MAINTENANCE PRACTICES) START ---
    elif mod == "Module 7":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("🔧 MODULE 07: MAINTENANCE PRACTICES")
        
        m7_col1, m7_col2 = st.columns(2)
        with m7_col1:
            st.markdown("#### 🛠️ Tooling & Safety")
            st.write("""
            * **Safety:** Use of PPE, fire extinguishers, and workshop safety protocols.
            * **Precision Tools:** Micrometers, vernier calipers, and torque wrenches.
            * **Calibration:** Ensuring all measuring tools are within certified limits.
            """)
        with m7_col2:
            st.markdown("#### 🔍 Inspection Techniques")
            st.write("""
            * **Visual Inspection:** Identifying cracks, corrosion, and wear.
            * **NDT:** Non-Destructive Testing (Dye penetrant, Eddy current, Ultrasonic).
            * **Lubrication:** Importance of correct oils and greases for moving parts.
            """)

        st.write("---")
        st.subheader("⚙️ Maintenance Math Tools")
        m7c1, m7c2 = st.columns(2)
        with m7c1:
            st.markdown("#### 🔧 Torque Conversion")
            t_val = st.number_input("Torque Value:", value=100.0)
            t_unit = st.selectbox("From Unit:", ["lb-ft to Nm", "Nm to lb-ft"])
            res = t_val * 1.3558 if "lb-ft" in t_unit else t_val / 1.3558
            st.success(f"Converted Torque: **{res:.2f}**")
        with m7c2:
            st.markdown("#### 📏 Micrometer Reading Simulator")
            st.write("Precision measurement is vital for ensuring component tolerances in engine and airframe maintenance.")
            st.info("Reading = Sleeve + Thimble + (Vernier Scale if available)")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 8 (BASIC AERODYNAMICS) START ---
    elif mod == "Module 8":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("🦅 MODULE 08: BASIC AERODYNAMICS")
        
        m8_col1, m8_col2 = st.columns(2)
        with m8_col1:
            st.markdown("#### 🌬️ Physics of the Atmosphere")
            st.write("""
            * **ISA:** International Standard Atmosphere ($15°C$, $1013.25 hPa$).
            * **Airflow:** Laminar vs Turbulent flow.
            * **Bernoulli’s Principle:** Total Pressure = Static Pressure + Dynamic Pressure.
            """)
        with m8_col2:
            st.markdown("#### ✈️ Aerodynamic Forces")
            st.write("""
            * **Lift:** Generated by pressure difference (Angle of Attack).
            * **Drag:** Parasite drag and Induced drag.
            * **Stability:** Longitudinal, Lateral, and Directional stability.
            """)

        st.write("---")
        st.subheader("⚙️ Aerodynamic Calculations")
        m8c1, m8c2 = st.columns(2)
        with m8c1:
            st.markdown("#### 🛩️ Lift Equation")
            cl = st.number_input("Coefficient of Lift ($C_L$):", value=0.5)
            rho = st.number_input("Air Density (kg/m³):", value=1.225)
            vel = st.number_input("Velocity (m/s):", value=50.0)
            area_s = st.number_input("Wing Area (m²):", value=20.0)
            lift = 0.5 * rho * (vel**2) * area_s * cl
            st.success(f"Calculated Lift: **{lift/1000:.2f} kN**")
        with m8c2:
            st.markdown("#### 📏 Aspect Ratio")
            span = st.number_input("Wing Span (m):", value=15.0)
            chord = st.number_input("Average Chord (m):", value=2.0)
            ar = span / chord
            st.info(f"Aspect Ratio: **{ar:.2f}**")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 9 (HUMAN FACTORS) START ---
    elif mod == "Module 9":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("👤 MODULE 09: HUMAN FACTORS")
        
        m9_col1, m9_col2 = st.columns(2)
        with m9_col1:
            st.markdown("#### 🧠 Human Performance")
            st.write("""
            * **Vision & Hearing:** Limitations in perception and auditory processing.
            * **Information Processing:** Memory, attention, and decision-making.
            * **Fatigue:** The impact of lack of sleep on maintenance safety.
            """)
        with m9_col2:
            st.markdown("#### 🤝 Social Psychology")
            st.write("""
            * **SHEL Model:** Software, Hardware, Environment, Liveware interaction.
            * **Communication:** Barriers to effective information exchange.
            * **The Dirty Dozen:** 12 most common causes of human error in aviation.
            """)

        st.write("---")
        st.subheader("⚙️ Human Factors Analysis")
        st.write("Human factors do not typically use equations, but focus on the **Error Management** cycle.")
        st.info("Current Mission: Minimize errors through 'Double Check' and 'Effective Communication'.")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 10 (AVIATION LEGISLATION) START ---
    elif mod == "Module 10":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("⚖️ MODULE 10: AVIATION LEGISLATION")
        
        m10_col1, m10_col2 = st.columns(2)
        with m10_col1:
            st.markdown("#### 🌍 Global Authorities")
            st.write("""
            * **ICAO:** Sets international standards for civil aviation.
            * **EASA:** European Union Aviation Safety Agency (Part 66/145/M).
            * **FAA:** Federal Aviation Administration (USA).
            """)
        with m10_col2:
            st.markdown("#### 📜 Regulations")
            st.write("""
            * **Part 66:** Licensing of Maintenance Personnel.
            * **Part 145:** Approved Maintenance Organizations (AMO).
            * **Part M:** Continuing Airworthiness Requirements.
            """)

        st.write("---")
        st.subheader("⚙️ Legislative Compliance")
        st.write("Compliance is measured by adherence to the **CRS** (Certificate of Release to Service) standards.")
        st.warning("Violation of these standards can lead to license suspension and safety risks.")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 11 (TURBINE AEROPLANE STRUCTURES & SYSTEMS) START ---
    elif mod == "Module 11":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("✈️ MODULE 11: TURBINE AEROPLANE STRUCTURES & SYSTEMS")
        
        m11_col1, m11_col2 = st.columns(2)
        with m11_col1:
            st.markdown("#### 🏗️ Airframe Structures")
            st.write("""
            * **Fuselage:** Monocoque and semi-monocoque structures.
            * **Wings:** Cantilever and braced wing designs.
            * **Hydraulics:** Reservoir, pumps, and actuators for flight controls.
            """)
        with m11_col2:
            st.markdown("#### 🛠️ Systems & Components")
            st.write("""
            * **Air Conditioning:** Pack systems and pressurization control.
            * **Fuel Systems:** Storage, feed, and jettison systems.
            * **Landing Gear:** Retraction and braking systems (Anti-skid).
            """)

        st.write("---")
        st.subheader("⚙️ Systems Calculations")
        m11c1, m11c2 = st.columns(2)
        with m11c1:
            st.markdown("#### 🌊 Hydraulic Force")
            h_press = st.number_input("Hydraulic Pressure (PSI):", value=3000.0)
            h_area = st.number_input("Piston Area (sq in):", value=2.5)
            h_force = h_press * h_area
            st.success(f"Output Force: **{h_force:.2f} lbs**")
        with m11c2:
            st.markdown("#### ⛽ Fuel Consumption Rate")
            f_flow = st.number_input("Fuel Flow Rate (kg/hr):", value=2500.0)
            f_time = st.number_input("Flight Time (hours):", value=3.5)
            st.info(f"Total Fuel Required: **{f_flow * f_time:.2f} kg**")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 12 (HELICOPTER AERODYNAMICS, STRUCTURES & SYSTEMS) START ---
    elif mod == "Module 12":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("🚁 MODULE 12: HELICOPTER AERODYNAMICS, STRUCTURES & SYSTEMS")
        
        m12_col1, m12_col2 = st.columns(2)
        with m12_col1:
            st.markdown("#### 🌀 Rotary Wing Aerodynamics")
            st.write("""
            * **Lift:** Generated by the main rotor blades (Collective pitch).
            * **Control:** Cyclic pitch and Anti-torque (Tail rotor) systems.
            * **Flight States:** Hovering, Autorotation, and Ground effect.
            """)
        with m12_col2:
            st.markdown("#### ⚙️ Helicopter Systems")
            st.write("""
            * **Transmission:** Main gearbox, tail rotor drive, and clutches.
            * **Vibration:** Tracking and balancing of rotor blades.
            * **Blades:** Composite and metallic rotor blade construction.
            """)

        st.write("---")
        st.subheader("⚙️ Helicopter Math Tools")
        m12c1, m12c2 = st.columns(2)
        with m12c1:
            st.markdown("#### 🔄 Tip Speed Calculation")
            r_rad = st.number_input("Rotor Radius (m):", value=6.0)
            r_rpm = st.number_input("Rotor RPM:", value=400.0)
            # Tip speed = 2 * pi * r * (RPM/60)
            tip_v = 2 * 3.14159 * r_rad * (r_rpm / 60)
            st.success(f"Rotor Tip Speed: **{tip_v:.2f} m/s**")
        with m12c2:
            st.markdown("#### ⚖️ Torque Balance")
            st.write("Anti-torque must equal the reaction torque of the main rotor to maintain heading.")
            st.info("Tip: Tail rotor thrust is adjusted via the rudder pedals.")
        st.markdown('</div>', unsafe_allow_html=True)
    # --- MODULE 13 (AIRCRAFT AERODYNAMICS, STRUCTURES & SYSTEMS) START ---
    elif mod == "Module 13":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("📡 MODULE 13: AIRCRAFT AERODYNAMICS, STRUCTURES & SYSTEMS")
        
        m13_col1, m13_col2 = st.columns(2)
        with m13_col1:
            st.markdown("#### 🛰️ Avionic Systems")
            st.write("""
            * **Auto-flight:** Autopilot, Flight Director, and FMS.
            * **Communication:** VHF, HF, and SATCOM systems.
            * **Navigation:** VOR, ILS, DME, and GPS.
            """)
        with m13_col2:
            st.markdown("#### 🚨 Warning & Recording")
            st.write("""
            * **Radar:** Weather radar and Ground Proximity Warning (GPWS).
            * **Recorders:** CVR (Cockpit Voice) and FDR (Flight Data).
            * **Instruments:** Electronic Flight Instrument System (EFIS).
            """)

        st.write("---")
        st.subheader("⚙️ Avionics Calculations")
        m13c1, m13c2 = st.columns(2)
        with m13c1:
            st.markdown("#### 📻 Radio Propagation")
            freq = st.number_input("Frequency (MHz):", value=121.5)
            wavelength = 300 / freq
            st.success(f"Wavelength: **{wavelength:.2f} meters**")
        with m13c2:
            st.markdown("#### ⚡ Power Consumption")
            volt_a = st.number_input("Avionics Voltage (V):", value=28.0)
            curr_a = st.number_input("Total Current Load (A):", value=15.0)
            st.info(f"System Load: **{volt_a * curr_a:.2f} Watts**")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # --- MODULE 14 (PROPULSION) START ---
    elif mod == "Module 14":
        st.markdown('<div class="info-panel">', unsafe_allow_html=True)
        st.header("🔥 MODULE 14: PROPULSION (HELICOPTER GAS TURBINE)")
        
        m14_col1, m14_col2 = st.columns(2)
        with m14_col1:
            st.markdown("#### ⚙️ Turbine Engine Theory")
            st.write("""
            * **Brayton Cycle:** Intake, Compression, Combustion, Exhaust.
            * **Free Turbine:** Used to drive the rotor system independently.
            """)
        with m14_col2:
            st.markdown("#### 🚀 Performance Factors")
            st.write("""
            * **SFC:** Specific Fuel Consumption.
            * **Surge & Stall:** Airflow instability within the compressor.
            """)

        st.write("---")
        st.subheader("📊 Engine Performance Graph")
        v = np.linspace(1, 10, 100)
        p = 10 / v 
        chart_data_m14 = pd.DataFrame({'Volume (V)': v, 'Pressure (P)': p})
        st.area_chart(chart_data_m14.set_index('Volume (V)'))

        # Calculations
        st.write("---")
        st.subheader("⚙️ Propulsion Calculations")
        m14c1, m14c2 = st.columns(2)
        with m14c1:
            fuel_flow = st.number_input("Fuel Flow (kg/hr):", value=150.0)
            power_out = st.number_input("Shaft Horsepower (SHP):", value=500.0)
            sfc = fuel_flow / power_out if power_out > 0 else 0
            st.success(f"SFC: **{sfc:.3f} kg/hr/SHP**")
        with m14c2:
            c_temp = st.number_input("Exhaust Gas Temp (°C):", value=600.0)
            st.info(f"Fahrenheit: **{(c_temp * 9/5) + 32:.1f} °F**")
        st.markdown('</div>', unsafe_allow_html=True)

        # --- ADDING ENDING FACTS HERE ---
        st.write("---")
        st.header("🏁 SYSTEM DIAGNOSTICS SUMMARY")
        
        # Engine Wallpaper & Bar Chart
        st.image("https://images.unsplash.com/photo-1544724569-5f546fa662b5", caption="Engine Health Analysis", use_container_width=True)
        
        diag_data = pd.DataFrame({
            'Symptoms': ['Vibration', 'Overheat', 'Fuel Leak', 'Pressure Drop'],
            'Severity': [20, 85, 10, 45]
        })
        st.bar_chart(diag_data.set_index('Symptoms'))

        # Symptoms and Actions Table
        st.markdown("""
        | Symptom | Severity | Recommended Action |
        | :--- | :--- | :--- |
        | **High EGT** | 85% | Reduce Throttle & Check Cooling |
        | **Low Oil Pressure** | 45% | Check Pump & Filter |
        | **Vibration** | 20% | Inspect Compressor Blades |
        """)

        # Multi-Language Thank You Message
        st.markdown('<div class="info-panel" style="text-align: center; border: 2px solid #00FF00;">', unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size: 28px; color: #00FF00; font-weight: bold;">🙏 THANK YOU FOR USING AVIONIX MASTER CORE</div>
        <div style="font-size: 16px; margin-top: 15px;">
            <b>[ENGLISH]</b> Thank you for your excellence. | <b>[DEUTSCH]</b> Vielen Dank. <br>
            <b>[FRANÇAIS]</b> Merci beaucoup. | <b>[РУССКИЙ]</b> Благодарим вас. <br>
            <b>[日本語]</b> ありがとうございました。 | <b>[中文]</b> 感谢您。
        </div>
        """, unsafe_allow_html=True)
        
        # Creator Credit
        st.markdown("<hr><h3 style='text-align: center; color: #FFD700;'>CREATOR: SAVINDU MANETH</h3>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Return Button
        if st.button("⬅️ BACK TO DASHBOARD"):
            st.session_state.page = 'dashboard'
            st.rerun()