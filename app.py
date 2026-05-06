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
    # --- MODULE 1: 20 MCQS SECTION ---
        st.write("---")
        st.header("📝 MODULE 01: PRACTICE EXAM (20 QUESTIONS)")
        st.info("EASA Part 66 Style - Select the best answer for each question.")

        # Questions Database
        m1_questions = [
            {"q": "1. What is the value of 1011 in decimal?", "o": ["11", "13", "9", "15"], "a": "11", "ex": "Binary 1011 = (1*8) + (0*4) + (1*2) + (1*1) = 11."},
            {"q": "2. Solve: 2 + 3 x 4", "o": ["20", "14", "18", "12"], "a": "14", "ex": "Using BODMAS: Multiply first (3x4=12), then add (12+2=14)."},
            {"q": "3. The square root of 144 is?", "o": ["12", "14", "16", "10"], "a": "12", "ex": "12 x 12 = 144."},
            {"q": "4. Convert 1/8 to a percentage.", "o": ["10%", "12.5%", "15%", "8%"], "a": "12.5%", "ex": "(1 / 8) * 100 = 12.5%."},
            {"q": "5. What is the sum of angles in a triangle?", "o": ["90°", "180°", "360°", "270°"], "a": "180", "ex": "Internal angles of any triangle always sum to 180 degrees."},
            {"q": "6. Log 100 to the base 10 is?", "o": ["1", "2", "3", "10"], "a": "2", "ex": "10 to the power of 2 is 100."},
            {"q": "7. A ratio of 3:4 is equivalent to?", "o": ["75%", "60%", "80%", "40%"], "a": "75%", "ex": "3/4 = 0.75 or 75%."},
            {"q": "8. What is the area of a circle with radius 'r'?", "o": ["2πr", "πr²", "πd", "2πr²"], "a": "πr²", "ex": "Area = π * radius squared."},
            {"q": "9. Simplify: (a²)³", "o": ["a⁵", "a⁶", "a²", "a⁸"], "a": "a⁶", "ex": "Power of a power rule: multiply exponents (2x3=6)."},
            {"q": "10. In the equation y = mx + c, what does 'm' represent?", "o": ["Intercept", "Gradient", "X-value", "Constant"], "a": "Gradient", "ex": "'m' is the slope or gradient of the line."},
            {"q": "11. 1 Radian is approximately equal to?", "o": ["45°", "57.3°", "60°", "90°"], "a": "57.3°", "ex": "180 / π ≈ 57.295°."},
            {"q": "12. Which of these is a prime number?", "o": ["9", "15", "17", "21"], "a": "17", "ex": "17 is only divisible by 1 and itself."},
            {"q": "13. Sin 30° is equal to?", "o": ["0.5", "0.866", "1", "0.707"], "a": "0.5", "ex": "Standard trigonometric value for Sin 30 is 1/2."},
            {"q": "14. A line touching a circle at only one point is a?", "o": ["Chord", "Tangent", "Secant", "Diameter"], "a": "Tangent", "ex": "A tangent intersects a circle at exactly one point."},
            {"q": "15. Hexadecimal 'A' represents decimal?", "o": ["10", "11", "12", "9"], "a": "10", "ex": "In Hex: 9, A(10), B(11), C(12)..."},
            {"q": "16. 2⁴ is equal to?", "o": ["8", "16", "32", "6"], "a": "16", "ex": "2 * 2 * 2 * 2 = 16."},
            {"q": "17. The value of π (Pi) is approximately?", "o": ["3.12", "3.14", "3.16", "3.18"], "a": "3.14", "ex": "π is approximately 22/7 or 3.14159."},
            {"q": "18. What is 0.005 in scientific notation?", "o": ["5 x 10³", "5 x 10⁻³", "0.5 x 10⁻²", "50 x 10⁻⁴"], "a": "5 x 10⁻³", "ex": "Move decimal 3 places to the right."},
            {"q": "19. The result of any number raised to power 0 is?", "o": ["0", "The number itself", "1", "Infinity"], "a": "1", "ex": "Identity rule: x⁰ = 1."},
            {"q": "20. Solve for x: 2x + 4 = 10", "o": ["2", "3", "4", "5"], "a": "3", "ex": "2x = 6 -> x = 3."}
        ]

        # Score Tracking
        if 'm1_score' not in st.session_state:
            st.session_state.m1_score = 0
            st.session_state.m1_submitted = False

        # Display Questions
        user_answers = []
        for i, item in enumerate(m1_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m1_q{i}", index=None)
            user_answers.append(ans)

        # Submit Button
        if st.button("🚀 SUBMIT MODULE 1 EXAM"):
            st.session_state.m1_submitted = True
            score = 0
            for i, item in enumerate(m1_questions):
                if user_answers[i] == item['a']:
                    score += 1
            st.session_state.m1_score = score
            st.rerun()

        # Result Display
        if st.session_state.m1_submitted:
            st.write("---")
            final_score = st.session_state.m1_score
            percentage = (final_score / 20) * 100
            
            if percentage >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {final_score}/20 ({percentage}%)")
            else:
                st.error(f"❌ FAIL. Score: {final_score}/20 ({percentage}%). Passing is 75%.")

            # Review Answers
            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m1_questions):
                    if user_answers[i] == item['a']:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        st.write(f"Q{i+1}: Incorrect ❌. Correct: **{item['a']}**")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE QUIZ"):
                st.session_state.m1_submitted = False
                st.rerun()
    
           
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
    # --- MODULE 2: PHYSICS SECTION ---
    
        st.write("---")
        st.header("📝 MODULE 02: PHYSICS PRACTICE EXAM")
        st.info("EASA Part 66 Syllabus - Matter, Statics, Kinetics, and Dynamics")

        m2_questions = [
            {"q": "1. What is the standard unit of force?", "o": ["Joule", "Watt", "Newton", "Pascal"], "a": "Newton", "ex": "Force is measured in Newtons (N)."},
            {"q": "2. Boyle's Law relates to which two properties?", "o": ["Pressure/Volume", "Temp/Volume", "Mass/Weight", "Density/Pressure"], "a": "Pressure/Volume", "ex": "Boyle's Law: P1V1 = P2V2 at constant temperature."},
            {"q": "3. The rate of change of displacement is?", "o": ["Acceleration", "Velocity", "Speed", "Inertia"], "a": "Velocity", "ex": "Velocity is displacement divided by time."},
            {"q": "4. What is the density of pure water?", "o": ["100 kg/m³", "500 kg/m³", "1000 kg/m³", "1200 kg/m³"], "a": "1000 kg/m³", "ex": "Pure water has a density of 1000 kg/m³."},
            {"q": "5. Newton's Second Law is expressed as?", "o": ["F = m/a", "F = ma", "F = v/t", "W = mg"], "a": "F = ma", "ex": "Force equals Mass times Acceleration."},
            {"q": "6. Kinetic energy depends on?", "o": ["Height and Mass", "Mass and Velocity", "Pressure and Area", "Time and Force"], "a": "Mass and Velocity", "ex": "KE = 1/2 mv²."},
            {"q": "7. The pressure at the bottom of a liquid column depends on?", "o": ["Width", "Height", "Shape", "Volume"], "a": "Height", "ex": "P = ρgh, where h is the height/depth."},
            {"q": "8. What is the freezing point of water in Kelvin?", "o": ["0 K", "100 K", "273 K", "373 K"], "a": "273 K", "ex": "0°C corresponds to approximately 273 Kelvin."},
            {"q": "9. A vector quantity has both?", "o": ["Mass and Volume", "Size and Direction", "Speed and Time", "Force and Mass"], "a": "Size and Direction", "ex": "Vectors have magnitude and direction."},
            {"q": "10. Work done is calculated by?", "o": ["Force / Distance", "Force x Distance", "Mass x Velocity", "Power x Time"], "a": "Force x Distance", "ex": "Work = Force x Displacement."},
            {"q": "11. Atmospheric pressure at sea level is approx?", "o": ["10 PSI", "14.7 PSI", "20 PSI", "101 PSI"], "a": "14.7 PSI", "ex": "Standard atmospheric pressure is 14.7 PSI."},
            {"q": "12. Acceleration due to gravity (g) is approx?", "o": ["8.9 m/s²", "9.81 m/s²", "10.5 m/s²", "1.6 m/s²"], "a": "9.81 m/s²", "ex": "On Earth, g is standard at 9.81 m/s²."},
            {"q": "13. What is the unit of Power?", "o": ["Joule", "Newton", "Watt", "Volt"], "a": "Watt", "ex": "Power is measured in Watts (W)."},
            {"q": "14. Centripetal force acts towards the?", "o": ["Outside", "Center", "Tangent", "Bottom"], "a": "Center", "ex": "Centripetal force is directed toward the center of rotation."},
            {"q": "15. Matter exists in which three main states?", "o": ["Solid, Liquid, Gas", "Hard, Soft, Wet", "Ice, Water, Steam", "Atom, Molecule, Ion"], "a": "Solid, Liquid, Gas", "ex": "These are the three fundamental states of matter."},
            {"q": "16. Specific Gravity has which unit?", "o": ["kg/m³", "N/m²", "No unit", "Joules"], "a": "No unit", "ex": "Specific gravity is a ratio, so it has no units."},
            {"q": "17. Efficiency of a machine is always?", "o": ["100%", "> 100%", "< 100%", "0%"], "a": "< 100%", "ex": "Output is always less than input due to friction."},
            {"q": "18. Mechanical Advantage (MA) is?", "o": ["Effort / Load", "Load / Effort", "Distance / Time", "Mass / Volume"], "a": "Load / Effort", "ex": "MA = Load / Effort."},
            {"q": "19. The law of conservation of energy states energy cannot be?", "o": ["Stored", "Changed", "Created or Destroyed", "Measured"], "a": "Created or Destroyed", "ex": "Energy only transforms from one form to another."},
            {"q": "20. Stress is defined as?", "o": ["Force x Area", "Force / Area", "Mass / Area", "Length / Area"], "a": "Force / Area", "ex": "Stress = Force per unit area."}
        ]

        if 'm2_submitted' not in st.session_state:
            st.session_state.m2_submitted = False
            st.session_state.m2_score = 0

        user_ans_m2 = []
        for i, item in enumerate(m2_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m2_q{i}", index=None)
            user_ans_m2.append(ans)

        if st.button("🚀 SUBMIT MODULE 2 EXAM"):
            st.session_state.m2_submitted = True
            st.session_state.m2_score = sum(1 for i, item in enumerate(m2_questions) if user_ans_m2[i] == item['a'])
            st.rerun()

        if st.session_state.m2_submitted:
            st.write("---")
            perc = (st.session_state.m2_score / len(m2_questions)) * 100
            if perc >= 75:
                st.success(f"PASS! Score: {st.session_state.m2_score}/20 ({perc}%)")
            else:
                st.error(f"FAIL. Score: {st.session_state.m2_score}/20 ({perc}%)")

            with st.expander("🔍 View Corrections"):
                for i, item in enumerate(m2_questions):
                    is_correct = (user_ans_m2[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 2"):
                st.session_state.m2_submitted = False
                st.rerun()
        
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
    # --- MODULE 3: ELECTRICAL FUNDAMENTALS (FULL 20 QUESTIONS) ---
        st.write("---")
        st.header("⚡ MODULE 03: ELECTRICAL FUNDAMENTALS EXAM")
        st.info("EASA Part 66 Syllabus - Electron Theory, Static Electricity, and DC Circuits")

        m3_questions = [
            {"q": "1. What is the unit of electric current?", "o": ["Volt", "Ohm", "Ampere", "Watt"], "a": "Ampere", "ex": "Electric current is measured in Amperes (A)."},
            {"q": "2. According to Ohm's Law, Voltage (V) equals?", "o": ["I / R", "I * R", "R / I", "I + R"], "a": "I * R", "ex": "V = IR (Voltage = Current x Resistance)."},
            {"q": "3. What is the unit of Electrical Resistance?", "o": ["Ampere", "Coulomb", "Ohm", "Farad"], "a": "Ohm", "ex": "Resistance is measured in Ohms (Ω)."},
            {"q": "4. A material that allows electrons to flow easily is called a?", "o": ["Insulator", "Conductor", "Semiconductor", "Resistor"], "a": "Conductor", "ex": "Conductors like copper allow easy electron flow."},
            {"q": "5. The unit of Electrical Power is?", "o": ["Joule", "Volt", "Watt", "Ampere"], "a": "Watt", "ex": "Power (P) = V * I, measured in Watts (W)."},
            {"q": "6. In a series circuit, what remains constant across all components?", "o": ["Voltage", "Current", "Resistance", "Power"], "a": "Current", "ex": "In a series circuit, the same current flows through all parts."},
            {"q": "7. In a parallel circuit, what remains the same across all branches?", "o": ["Current", "Voltage", "Resistance", "Power"], "a": "Voltage", "ex": "The voltage across each branch in parallel is identical."},
            {"q": "8. What device is used to measure electric current?", "o": ["Voltmeter", "Ammeter", "Ohmmeter", "Wattmeter"], "a": "Ammeter", "ex": "An ammeter measures current in Amperes."},
            {"q": "9. A capacitor stores energy in what form?", "o": ["Magnetic field", "Chemical form", "Electrostatic field", "Heat"], "a": "Electrostatic field", "ex": "Capacitors store energy in an electrostatic field between plates."},
            {"q": "10. What is the unit of Capacitance?", "o": ["Henry", "Farad", "Ohm", "Volt"], "a": "Farad", "ex": "Capacitance is measured in Farads (F)."},
            {"q": "11. An inductor stores energy in what form?", "o": ["Electrostatic field", "Magnetic field", "Heat", "Chemical"], "a": "Magnetic field", "ex": "Inductors store energy in a magnetic field."},
            {"q": "12. What is the unit of Inductance?", "o": ["Farad", "Henry", "Ohm", "Watt"], "a": "Henry", "ex": "Inductance is measured in Henrys (H)."},
            {"q": "13. What color code represents the number '0' in a resistor?", "o": ["Black", "Brown", "Red", "Gold"], "a": "Black", "ex": "In the resistor color code, Black represents 0."},
            {"q": "14. A fuse is always connected in ________ with the circuit?", "o": ["Parallel", "Series", "Either", "None"], "a": "Series", "ex": "Fuses must be in series to break the circuit during a fault."},
            {"q": "15. What is the primary source of DC in an aircraft while flying?", "o": ["Battery", "Generator/Alternator", "Static wick", "Inverter"], "a": "Generator/Alternator", "ex": "Alternators provide the main DC power (via rectifiers)."},
            {"q": "16. Which law states that the sum of currents entering a junction equals the sum leaving it?", "o": ["Ohm's Law", "Kirchhoff's Current Law", "Coulomb's Law", "Faraday's Law"], "a": "Kirchhoff's Current Law", "ex": "Kirchhoff's Current Law (KCL) deals with current conservation."},
            {"q": "17. What is the unit of Electrical Charge?", "o": ["Ampere", "Coulomb", "Volt", "Watt"], "a": "Coulomb", "ex": "Electric charge (Q) is measured in Coulombs (C)."},
            {"q": "18. Conventional current is assumed to flow from?", "o": ["Negative to Positive", "Positive to Negative", "Center to Outside", "Randomly"], "a": "Positive to Negative", "ex": "Conventional current flows from positive (+) to negative (-)."},
            {"q": "19. A 12V battery connected to a 4 Ohm resistor will draw how much current?", "o": ["3A", "48A", "0.33A", "8A"], "a": "3A", "ex": "I = V / R -> 12 / 4 = 3 Amperes."},
            {"q": "20. What is the purpose of a diode?", "o": ["Store charge", "Limit current", "Allow current in one direction", "Increase voltage"], "a": "Allow current in one direction", "ex": "Diodes act as one-way valves for electric current."}
        ]

        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m3_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 3 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m3_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m3_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m3_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 3"):
                st.session_state.m3_submitted = False
                st.rerun()
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
    
        st.write("---")
        st.header("🔌 MODULE 04: ELECTRONIC FUNDAMENTALS")
        m4_questions = [
            {"q": "1. What is the main characteristic of a Semiconductor?", "o": ["High Conductivity", "High Resistance", "Variable Conductivity", "Insulator"], "a": "Variable Conductivity", "ex": "Semiconductors have properties between conductors and insulators."},
            {"q": "2. An N-type semiconductor has an excess of?", "o": ["Holes", "Electrons", "Protons", "Neutrons"], "a": "Electrons", "ex": "N-type (Negative) has extra electrons."},
            {"q": "3. A P-type semiconductor has an excess of?", "o": ["Electrons", "Holes", "Neutrons", "Positrons"], "a": "Holes", "ex": "P-type (Positive) has 'holes' or electron deficiencies."},
            {"q": "4. What is the junction voltage of a Silicon diode?", "o": ["0.3V", "0.7V", "1.1V", "1.5V"], "a": "0.7V", "ex": "Silicon diodes typically require 0.7V to conduct."},
            {"q": "5. What are the three terminals of a Bipolar Junction Transistor (BJT)?", "o": ["Gate, Drain, Source", "Anode, Cathode, Gate", "Emitter, Base, Collector", "Input, Output, Ground"], "a": "Emitter, Base, Collector", "ex": "BJT terminals are Emitter (E), Base (B), and Collector (C)."},
            {"q": "6. In a series circuit, what remains constant across all components?", "o": ["Voltage", "Current", "Resistance", "Power"], "a": "Current", "ex": "In a series circuit, the same current flows through all parts."},
            {"q": "7. In a parallel circuit, what remains the same across all branches?", "o": ["Current", "Voltage", "Resistance", "Power"], "a": "Voltage", "ex": "The voltage across each branch in parallel is identical."},
            {"q": "8. What device is used to measure electric current?", "o": ["Voltmeter", "Ammeter", "Ohmmeter", "Wattmeter"], "a": "Ammeter", "ex": "An ammeter measures current in Amperes."},
            {"q": "9. A capacitor stores energy in what form?", "o": ["Magnetic field", "Chemical form", "Electrostatic field", "Heat"], "a": "Electrostatic field", "ex": "Capacitors store energy in an electrostatic field between plates."},
            {"q": "10. What is the unit of Capacitance?", "o": ["Henry", "Farad", "Ohm", "Volt"], "a": "Farad", "ex": "Capacitance is measured in Farads (F)."},
            {"q": "11. An inductor stores energy in what form?", "o": ["Electrostatic field", "Magnetic field", "Heat", "Chemical"], "a": "Magnetic field", "ex": "Inductors store energy in a magnetic field."},
            {"q": "12. What is the unit of Inductance?", "o": ["Farad", "Henry", "Ohm", "Watt"], "a": "Henry", "ex": "Inductance is measured in Henrys (H)."},
            {"q": "13. What color code represents the number '0' in a resistor?", "o": ["Black", "Brown", "Red", "Gold"], "a": "Black", "ex": "In the resistor color code, Black represents 0."},
            {"q": "14. A fuse is always connected in ________ with the circuit?", "o": ["Parallel", "Series", "Either", "None"], "a": "Series", "ex": "Fuses must be in series to break the circuit during a fault."},
            {"q": "15. What is the primary source of DC in an aircraft while flying?", "o": ["Battery", "Generator/Alternator", "Static wick", "Inverter"], "a": "Generator/Alternator", "ex": "Alternators provide the main DC power (via rectifiers)."},
            {"q": "16. Which law states that the sum of currents entering a junction equals the sum leaving it?", "o": ["Ohm's Law", "Kirchhoff's Current Law", "Coulomb's Law", "Faraday's Law"], "a": "Kirchhoff's Current Law", "ex": "Kirchhoff's Current Law (KCL) deals with current conservation."},
            {"q": "17. What is the unit of Electrical Charge?", "o": ["Ampere", "Coulomb", "Volt", "Watt"], "a": "Coulomb", "ex": "Electric charge (Q) is measured in Coulombs (C)."},
            {"q": "18. Conventional current is assumed to flow from?", "o": ["Negative to Positive", "Positive to Negative", "Center to Outside", "Randomly"], "a": "Positive to Negative", "ex": "Conventional current flows from positive (+) to negative (-)."},
            {"q": "19. A 12V battery connected to a 4 Ohm resistor will draw how much current?", "o": ["3A", "48A", "0.33A", "8A"], "a": "3A", "ex": "I = V / R -> 12 / 4 = 3 Amperes."},
            {"q": "20. What is the purpose of a diode?", "o": ["Store charge", "Limit current", "Allow current in one direction", "Increase voltage"], "a": "Allow current in one direction", "ex": "Diodes act as one-way valves for electric current."}
        ]
        
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m4_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 3 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m4_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m4_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m4_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 3"):
                st.session_state.m3_submitted = False
                st.rerun()
    
        
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
        st.write("---")
        st.header("💻 MODULE 05: DIGITAL TECHNIQUES")
        m5_questions = [
            {"q": "1. Which logic gate is a 'Universal Gate'?", "o": ["AND", "OR", "NAND", "XOR"], "a": "NAND", "ex": "NAND and NOR can build any other gate."},
            {"q": "2. Binary 1101 is equal to decimal?", "o": ["11", "12", "13", "14"], "a": "13", "ex": "8 + 4 + 0 + 1 = 13."},
            {"q": "3. What is the output of an OR gate if inputs are 1 and 0?", "o": ["0", "1", "High-Z", "None"], "a": "1", "ex": "OR gate needs only one input to be 1."},
            {"q": "4. A Flip-Flop is a bit of?", "o": ["Processing", "Memory", "Input", "Output"], "a": "Memory", "ex": "Flip-flops store 1 bit of data."},
            {"q": "5. What does LCD stand for?", "o": ["Light Crystal Display", "Liquid Crystal Display", "Liquid Carbon Diode", "Low Current Display"], "a": "Liquid Crystal Display", "ex": "LCD is common in cockpit displays."},
            {"q": "6. A group of 4 bits is called a?", "o": ["Byte", "Nibble", "Word", "Bit"], "a": "Nibble", "ex": "4 bits = 1 nibble."},
            {"q": "7. ARINC 429 is a standard for?", "o": ["Fuel", "Digital Data Bus", "Engines", "Tires"], "a": "Digital Data Bus", "ex": "Main data bus used in commercial aircraft."},
            {"q": "8. Which gate inverts the input?", "o": ["AND", "OR", "NOT", "NAND"], "a": "NOT", "ex": "NOT gate (Inverter) flips 0 to 1 and 1 to 0."},
            {"q": "9. Hexadecimal F is equal to decimal?", "o": ["10", "14", "15", "16"], "a": "15", "ex": "A=10...F=15."},
            {"q": "10. Fiber optics use _____ to transmit data.", "o": ["Electrons", "Light", "Sound", "Radio"], "a": "Light", "ex": "Fiber optics use total internal reflection of light."},
            {"q": "11. Static electricity can damage?", "o": ["Wires", "CMOS components", "Tires", "Glass"], "a": "CMOS components", "ex": "Digital chips are very sensitive to ESD."},
            {"q": "12. RAM stands for?", "o": ["Read All Memory", "Random Access Memory", "Read Analog Mod", "Rapid Access Main"], "a": "Random Access Memory", "ex": "Volatile temporary storage."},
            {"q": "13. A 'Bit' stands for?", "o": ["Binary Digit", "Binary Tool", "Basic Input", "Bitrate"], "a": "Binary Digit", "ex": "Smallest unit of data."},
            {"q": "14. CRT stands for?", "o": ["Cathode Ray Tube", "Carbon Ray Tech", "Common Radio Tool", "Circuit Relay Test"], "a": "Cathode Ray Tube", "ex": "Older cockpit display technology."},
            {"q": "15. A Multiplexer (MUX) has?", "o": ["1 Input, Many Outputs", "Many Inputs, 1 Output", "1 Input, 1 Output", "No Inputs"], "a": "Many Inputs, 1 Output", "ex": "MUX selects one of many inputs."},
            {"q": "16. EPROM can be erased by?", "o": ["Water", "Electricity", "UV Light", "Heat"], "a": "UV Light", "ex": "Erasable Programmable ROM uses UV light."},
            {"q": "17. What is the LSB in binary?", "o": ["Last Small Bit", "Least Significant Bit", "Low System Bit", "Logic Start Bit"], "a": "Least Significant Bit", "ex": "Rightmost bit in a number."},
            {"q": "18. BCD stands for?", "o": ["Binary Coded Decimal", "Basic Coding Data", "Bit Counting Device", "Binary Control Digit"], "a": "Binary Coded Decimal", "ex": "Representing decimals with binary nibbles."},
            {"q": "19. Which bus is bidirectional?", "o": ["Address Bus", "Data Bus", "Control Bus", "None"], "a": "Data Bus", "ex": "Data travels both ways to/from CPU."},
            {"q": "20. Software instructions stored in ROM are called?", "o": ["Hardware", "Malware", "Firmware", "Shareware"], "a": "Firmware", "ex": "Firmware is permanent software."}
        ]
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m5_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 3 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m5_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m5_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m5_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 3"):
                st.session_state.m3_submitted = False
                st.rerun()# (Add same Submit/Review Logic as Module 4)
    
        
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
    
    
        st.write("---")
        st.header("🔩 MODULE 06: MATERIALS AND HARDWARE")
        m6_questions = [
            {"q": "1. What is the most common aircraft rivet material?", "o": ["Steel", "Copper", "2117 Aluminum", "Zinc"], "a": "2117 Aluminum", "ex": "AD rivets (2117-T4) are standard."},
            {"q": "2. Ferrous metals contain?", "o": ["Copper", "Aluminum", "Iron", "Magnesium"], "a": "Iron", "ex": "Ferrous = Iron-based."},
            {"q": "3. What is the purpose of Alclad?", "o": ["Decoration", "Corrosion protection", "Strength", "Heat resistance"], "a": "Corrosion protection", "ex": "Pure aluminum coating on alloy core."},
            {"q": "4. A 'Castle Nut' is secured with?", "o": ["Lock washer", "Cotter pin", "Glue", "Safety wire"], "a": "Cotter pin", "ex": "Cotter pins go through slots in castle nuts."},
            {"q": "5. Which material is used for engine firewalls?", "o": ["Aluminum", "Titanium/Stainless Steel", "Plastic", "Copper"], "a": "Titanium/Stainless Steel", "ex": "High melting point materials are needed."},
            {"q": "6. A non-destructive test using sound is?", "o": ["X-ray", "Dye Penetrant", "Ultrasonic", "Magnetic Particle"], "a": "Ultrasonic", "ex": "Uses high-frequency sound waves."},
            {"q": "7. What defines a 'Blind' rivet?", "o": ["It has no head", "Used when only one side is accessible", "It is invisible", "It is made of glass"], "a": "Used when only one side is accessible", "ex": "Mandrel pulls to expand the tail."},
            {"q": "8. Composite materials consist of?", "o": ["One metal", "Matrix and Reinforcement", "Liquid only", "Gas and Solid"], "a": "Matrix and Reinforcement", "ex": "E.g., Resin (matrix) and Carbon Fiber (reinforcement)."},
            {"q": "9. 'Galvanizing' involves coating steel with?", "o": ["Tin", "Zinc", "Gold", "Chromium"], "a": "Zinc", "ex": "Zinc prevents rust on steel."},
            {"q": "10. What tool measures the diameter of a wire?", "o": ["Ruler", "Micrometer", "Hammer", "Wrench"], "a": "Micrometer", "ex": "Micrometers provide precise measurements."},
            {"q": "11. A 'Cleco' is used to?", "o": ["Cut metal", "Hold sheets together for riveting", "Paint wings", "Tighten bolts"], "a": "Hold sheets together for riveting", "ex": "Temporary fasteners used during assembly."},
            {"q": "12. Brittleness in metal means it?", "o": ["Bends easily", "Breaks without deforming", "Stretches", "Melts fast"], "a": "Breaks without deforming", "ex": "Opposite of ductility."},
            {"q": "13. What is the most common wood for aircraft?", "o": ["Oak", "Pine", "Sitka Spruce", "Mahogany"], "a": "Sitka Spruce", "ex": "Spruce has high strength/weight ratio."},
            {"q": "14. A bolt with a hole in the shank is for?", "o": ["Weight saving", "Safety wire", "Cooling", "Oil flow"], "a": "Safety wire", "ex": "Allows wire to lock the fastener."},
            {"q": "15. 'Stress' is?", "o": ["Force per unit area", "Change in length", "Speed", "Weight"], "a": "Force per unit area", "ex": "Internal resistance to load."},
            {"q": "16. Which NDT is used for subsurface cracks in steel?", "o": ["Dye Pen", "Magnetic Particle", "Visual", "Tap test"], "a": "Magnetic Particle", "ex": "Detects discontinuities in ferrous metals."},
            {"q": "17. Anodizing is used on?", "o": ["Steel", "Aluminum", "Titanium", "Wood"], "a": "Aluminum", "ex": "Electrochemical surface treatment for Al."},
            {"q": "18. What is 'Fatigue' in metal?", "o": ["Rust", "Failure under repeated loading", "Melting", "Expansion"], "a": "Failure under repeated loading", "ex": "Repeated stress causes crack growth."},
            {"q": "19. A 'Self-locking' nut is not used where?", "o": ["Wings", "Subject to rotation", "Tail", "Fuselage"], "a": "Subject to rotation", "ex": "Lock nuts shouldn't be used on moving parts."},
            {"q": "20. Hardness is the ability of a metal to resist?", "o": ["Bending", "Penetration/Scratching", "Breaking", "Heat"], "a": "Penetration/Scratching", "ex": "Measured by Rockwell or Brinell tests."}
        ]
        
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m6_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 3 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m6_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m6_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m6_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 3"):
                st.session_state.m3_submitted = False
                st.rerun()# (Add same Submit/Review Logic as Module 4)
    
    
        
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
    
        st.write("---")
        st.header("🔧 MODULE 07: MAINTENANCE PRACTICES")
        m7_questions = [
            {"q": "1. What is the purpose of a 'Daily Inspection'?", "o": ["Major overhaul", "Ensure airworthiness for the day", "Check fuel only", "Clean the cabin"], "a": "Ensure airworthiness for the day", "ex": "Daily inspections check for general condition and leaks before flight."},
            {"q": "2. Torque wrenches are used to?", "o": ["Measure length", "Apply specific rotational force", "Check tire pressure", "Cut safety wire"], "a": "Apply specific rotational force", "ex": "Torque ensures fasteners are tightened to the correct specification."},
            {"q": "3. Which tool is used to check for internal cylinder leaks?", "o": ["Micrometer", "Differential Compression Tester", "Multimeter", "Flashlight"], "a": "Differential Compression Tester", "ex": "It measures the ability of cylinder to hold pressure."},
            {"q": "4. What is the standard safety wire size for most aircraft bolts?", "o": ["0.020 inch", "0.032 inch", "0.050 inch", "0.100 inch"], "a": "0.032 inch", "ex": "0.032 inch stainless steel wire is the aviation standard."},
            {"q": "5. A 'Go/No-Go' gauge is used for?", "o": ["Measuring weight", "Checking dimensional limits", "Testing batteries", "Painting"], "a": "Checking dimensional limits", "ex": "It quickly checks if a part is within acceptable tolerance."},
            {"q": "6. When jacking an aircraft, it should be done?", "o": ["Outside in wind", "On level ground inside a hangar", "On a slope", "Using one jack only"], "a": "On level ground inside a hangar", "ex": "Stability is critical during jacking operations."},
            {"q": "7. What is the purpose of a 'T-Clip'?", "o": ["Fueling", "Securing wire bundles", "Painting", "Locking doors"], "a": "Securing wire bundles", "ex": "T-Clips help manage electrical harness routing."},
            {"q": "8. Foreign Object Debris (FOD) is?", "o": ["A type of fuel", "Objects that can damage aircraft", "Navigation data", "Engine oil"], "a": "Objects that can damage aircraft", "ex": "FOD prevention is a critical maintenance practice."},
            {"q": "9. A 'Hard Landing' inspection is required after?", "o": ["Every flight", "Exceeding vertical load limits", "A long flight", "Flying in rain"], "a": "Exceeding vertical load limits", "ex": "Structural checks are needed after severe impacts."},
            {"q": "10. What color is standard 100LL Avgas?", "o": ["Red", "Green", "Blue", "Clear"], "a": "Blue", "ex": "100LL (Low Lead) aviation gasoline is dyed blue."},
            {"q": "11. 'Safetying' a turnbuckle prevents?", "o": ["Corrosion", "Rotation and loosening", "Heat", "Weight gain"], "a": "Rotation and loosening", "ex": "Safety wire or clips prevent turnbuckles from turning."},
            {"q": "12. What does a 'Static Wick' do?", "o": ["Lights up", "Dissipates static electricity", "Measures speed", "Holds the wing"], "a": "Dissipates static electricity", "ex": "Wicks allow static charge to bleed off into the air."},
            {"q": "13. Oxygen systems must be checked for?", "o": ["Fuel leaks", "Moisture and cleanliness", "Oil level", "Tire pressure"], "a": "Moisture and cleanliness", "ex": "Moisture can freeze and block oxygen flow at high altitudes."},
            {"q": "14. A 'Red Tag' on a part usually means?", "o": ["Ready for use", "Unserviceable/Scrap", "New part", "Needs cleaning"], "a": "Unserviceable/Scrap", "ex": "Red tags identify parts that cannot be used."},
            {"q": "15. Tire 'Flat Spots' are usually caused by?", "o": ["Over-inflation", "Heavy braking/skidding", "Soft rubber", "Cold weather"], "a": "Heavy braking/skidding", "ex": "Skidding during landing wears down one area of the tire."},
            {"q": "16. Which NDT method uses a developer powder?", "o": ["Dye Penetrant", "X-ray", "Eddy Current", "Visual"], "a": "Dye Penetrant", "ex": "Developer draws the dye out of cracks to make them visible."},
            {"q": "17. What is 'Bleeding' a hydraulic system?", "o": ["Removing oil", "Removing air", "Adding water", "Cleaning pipes"], "a": "Removing air", "ex": "Air in hydraulic lines makes the system 'spongy' and unresponsive."},
            {"q": "18. A 'Feeler Gauge' measures?", "o": ["Weight", "Gap/Clearance", "Voltage", "Sound"], "a": "Gap/Clearance", "ex": "Used to check spark plug gaps or valve clearances."},
            {"q": "19. Calibration of tools should be done?", "o": ["Once in a lifetime", "At regular certified intervals", "Only when broken", "Every day"], "a": "At regular certified intervals", "ex": "Precision tools must be certified for accuracy periodically."},
            {"q": "20. What is the first step in fire safety?", "o": ["Run away", "Prevention", "Buying a mask", "Opening windows"], "a": "Prevention", "ex": "Keeping hangars clean and oil-free prevents fires."}
        ]
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m7_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 7 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m7_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m7_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m7_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 7"):
                st.session_state.m3_submitted = False
                st.rerun()# (Add same Submit/Review Logic as Module 4)
    
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
    
        st.write("---")
        st.header("✈️ MODULE 08: BASIC AERODYNAMICS")
        m8_questions = [
            {"q": "1. What are the four forces of flight?", "o": ["Lift, Weight, Thrust, Drag", "Up, Down, Left, Right", "Air, Wind, Speed, Mass", "Force, Area, Speed, Drag"], "a": "Lift, Weight, Thrust, Drag", "ex": "These four forces act on an aircraft in flight."},
            {"q": "2. Bernoulli's Principle states that as air velocity increases, pressure?", "o": ["Increases", "Decreases", "Stays same", "Doubles"], "a": "Decreases", "ex": "Faster air creates lower pressure (Lift)."},
            {"q": "3. The angle between the chord line and relative wind is?", "o": ["Angle of Incidence", "Angle of Attack", "Dihedral", "Washout"], "a": "Angle of Attack", "ex": "Known as AOA."},
            {"q": "4. A wing stall occurs when the wing exceeds the?", "o": ["Speed limit", "Critical AOA", "Maximum weight", "Fuel limit"], "a": "Critical AOA", "ex": "Air can no longer flow smoothly over the wing."},
            {"q": "5. What is the purpose of a winglet?", "o": ["To look good", "Reduce induced drag", "Increase weight", "Stop fuel leaks"], "a": "Reduce induced drag", "ex": "Winglets reduce wingtip vortices."},
            {"q": "6. Mach 1 refers to?", "o": ["Speed of sound", "Speed of light", "Top speed", "Takeoff speed"], "a": "Speed of sound", "ex": "Mach is the ratio of aircraft speed to local speed of sound."},
            {"q": "7. The primary control for 'Roll' is?", "o": ["Rudder", "Elevator", "Ailerons", "Flaps"], "a": "Ailerons", "ex": "Ailerons control the longitudinal axis (Roll)."},
            {"q": "8. The 'Rudder' controls movement around which axis?", "o": ["Longitudinal", "Lateral", "Vertical", "Diagonal"], "a": "Vertical", "ex": "Rudder movement is called 'Yaw'."},
            {"q": "9. An 'Elevator' controls?", "o": ["Roll", "Yaw", "Pitch", "Speed"], "a": "Pitch", "ex": "Pitch is movement around the lateral axis."},
            {"q": "10. What is the 'Chord Line'?", "o": ["Wing thickness", "Distance from tip to tip", "Straight line from leading to trailing edge", "Wing area"], "a": "Straight line from leading to trailing edge", "ex": "Reference line for aerodynamic calculations."},
            {"q": "11. 'Aspect Ratio' is the ratio of?", "o": ["Weight to Lift", "Span to Chord", "Width to Height", "Speed to Drag"], "a": "Span to Chord", "ex": "Long, thin wings have high aspect ratios."},
            {"q": "12. In supersonic flight, air is considered?", "o": ["Incompressible", "Compressible", "Liquid", "Static"], "a": "Compressible", "ex": "Air density changes significantly at high speeds."},
            {"q": "13. What is 'Dihedral'?", "o": ["Wing twist", "Upward angle of wings from fuselage", "Wing length", "Tail height"], "a": "Upward angle of wings from fuselage", "ex": "Provides lateral stability."},
            {"q": "14. A 'Spoiler' is used to?", "o": ["Increase lift", "Decrease lift and increase drag", "Cool the engine", "Help the pilot see"], "a": "Decrease lift and increase drag", "ex": "Spoilers 'spoil' the airflow over the wing."},
            {"q": "15. The 'Stagnation Point' is where velocity is?", "o": ["Maximum", "Zero", "Speed of sound", "Infinite"], "a": "Zero", "ex": "Point on leading edge where flow stops."},
            {"q": "16. What creates 'Thrust' in a propeller aircraft?", "o": ["The wings", "The tail", "The propeller", "The wheels"], "a": "The propeller", "ex": "Propellers act like rotating wings to create thrust."},
            {"q": "17. 'Laminar Flow' is?", "o": ["Turbulent air", "Smooth, layered airflow", "Cold air", "Fast wind"], "a": "Smooth, layered airflow", "ex": "Desirable for reducing skin friction drag."},
            {"q": "18. Boundary layer separation causes?", "o": ["More lift", "Pressure drag", "Higher speed", "Lower weight"], "a": "Pressure drag", "ex": "Separation leads to turbulence and drag."},
            {"q": "19. The 'Center of Pressure' moves _____ as AOA increases?", "o": ["Backward", "Forward", "Nowhere", "Down"], "a": "Forward", "ex": "CP moves toward the leading edge as AOA goes up."},
            {"q": "20. Standard Sea Level Pressure is?", "o": ["10 PSI", "14.7 PSI", "29.92 inHg", "Both 14.7 PSI and 29.92 inHg"], "a": "Both 14.7 PSI and 29.92 inHg", "ex": "Standard atmospheric pressure values."}
        ]
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m8_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 8 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m8_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m8_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m8_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 8"):
                st.session_state.m3_submitted = False
                st.rerun()# (Add same Submit/Review Logic as Module 4)
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
    
        st.write("---")
        st.header("🧠 MODULE 09: HUMAN FACTORS")
        m9_questions = [
            {"q": "1. What is the 'SHEL' model?", "o": ["Software, Hardware, Environment, Liveware", "Speed, Heat, Energy, Lift", "System, Human, Entry, Logic", "None"], "a": "Software, Hardware, Environment, Liveware", "ex": "Standard HF model in aviation."},
            {"q": "2. What is 'Circadian Rhythm'?", "o": ["Heart rate", "Body's 24-hour cycle", "Breathing speed", "Flight path"], "a": "Body's 24-hour cycle", "ex": "Relates to sleep and alertness."},
            {"q": "3. The 'Dirty Dozen' refers to?", "o": ["12 bad tools", "12 human error causes", "12 broken parts", "12 old aircraft"], "a": "12 human error causes", "ex": "Factors like fatigue, lack of knowledge, etc."},
            {"q": "4. Lack of communication is a part of?", "o": ["The SHEL model", "The Dirty Dozen", "Ohm's Law", "Bernoulli's Principle"], "a": "The Dirty Dozen", "ex": "Poor communication is a major error source."},
            {"q": "5. What is 'Peripheral Vision'?", "o": ["Center vision", "Side vision", "Night vision", "Blind spot"], "a": "Side vision", "ex": "Ability to see things outside direct line of sight."},
            {"q": "6. 'Hypoxia' is a lack of?", "o": ["Food", "Water", "Oxygen", "Sleep"], "a": "Oxygen", "ex": "Common issue at high altitudes."},
            {"q": "7. Visual illusions can be caused by?", "o": ["Rain", "Darkness", "Sloping runways", "All of the above"], "a": "All of the above", "ex": "Many factors can trick the eyes."},
            {"q": "8. What is 'Complacency'?", "o": ["Being too careful", "Self-satisfaction / overconfidence", "Being angry", "Working too fast"], "a": "Self-satisfaction / overconfidence", "ex": "A major part of the Dirty Dozen."},
            {"q": "9. Effective communication involves?", "o": ["A sender only", "A receiver only", "A sender, message, and receiver", "Shouting"], "a": "A sender, message, and receiver", "ex": "Communication must be closed-loop."},
            {"q": "10. 'Fatigue' can be caused by?", "o": ["Lack of sleep", "Stress", "Long work hours", "All of the above"], "a": "All of the above", "ex": "Fatigue reduces performance and safety."},
            {"q": "11. Short-term memory can hold approx. how many items?", "o": ["1-2", "7 +/- 2", "20-30", "100"], "a": "7 +/- 2", "ex": "The average person's memory limit."},
            {"q": "12. What is 'Situational Awareness'?", "o": ["Knowing where the tools are", "Knowing what is happening around you", "Knowing the aircraft tail number", "Being able to read"], "a": "Knowing what is happening around you", "ex": "Crucial for safety and decision making."},
            {"q": "13. 'Motivation' is best described as?", "o": ["Being fast", "The drive to achieve a goal", "Following orders", "Ignoring rules"], "a": "The drive to achieve a goal", "ex": "Inner drive to perform tasks."},
            {"q": "14. A 'Peer Pressure' error occurs when?", "o": ["A tool breaks", "You follow the group even if they are wrong", "You work alone", "You read the manual"], "a": "You follow the group even if they are wrong", "ex": "Social pressure to ignore safety rules."},
            {"q": "15. 'Noise' in a hangar can lead to?", "o": ["Better hearing", "Fatigue and communication errors", "Faster work", "Happiness"], "a": "Fatigue and communication errors", "ex": "High noise levels are a stressor."},
            {"q": "16. 'Insomnia' is?", "o": ["Fear of heights", "Inability to sleep", "Loss of memory", "Muscle pain"], "a": "Inability to sleep", "ex": "Affects alertness during maintenance."},
            {"q": "17. Which organ is responsible for balance?", "o": ["Eyes", "Inner Ear", "Skin", "Hands"], "a": "Inner Ear", "ex": "Vestibular system in the ear manages balance."},
            {"q": "18. Stress that is good for performance is called?", "o": ["Distress", "Eustress", "No-stress", "Chronic stress"], "a": "Eustress", "ex": "Low levels of stress can improve focus."},
            {"q": "19. An 'Assertive' person?", "o": ["Is rude", "States facts and concerns clearly", "Does not speak", "Always agrees"], "a": "States facts and concerns clearly", "ex": "Assertiveness is positive in safety."},
            {"q": "20. Culture in a company affects?", "o": ["Only pilots", "Safety and performance", "The color of the plane", "The price of fuel"], "a": "Safety and performance", "ex": "Safety culture starts from the organization."}
        ]
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m9_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 9 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m9_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m9_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m9_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 9"):
                st.session_state.m3_submitted = False
                st.rerun()# (Add same Submit/Review Logic as Module 4)
    # --- MODULE 9 (HUMAN FACTORS) START ---
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
    
        st.write("---")
        st.header("⚖️ MODULE 10: AVIATION LEGISLATION")
        m10_questions = [
            {"q": "1. What does ICAO stand for?", "o": ["International Civil Aviation Organization", "International Control Aviation Office", "Internal Civil Aircraft Org", "None"], "a": "International Civil Aviation Organization", "ex": "ICAO is a specialized agency of the UN."},
            {"q": "2. EASA Part 66 deals with?", "o": ["Aircraft Operations", "Certifying Staff Maintenance", "Aircraft Noise", "Pilot Licensing"], "a": "Certifying Staff Maintenance", "ex": "Part 66 defines the requirements for maintenance licenses."},
            {"q": "3. A Certificate of Release to Service (CRS) is issued after?", "o": ["Flight", "Maintenance", "Takeoff", "Design"], "a": "Maintenance", "ex": "CRS confirms maintenance was done according to standards."},
            {"q": "4. How long must maintenance records be kept?", "o": ["1 year", "2 years", "3 years", "Until aircraft is retired"], "a": "3 years", "ex": "EASA typically requires records to be kept for 3 years after work completion."},
            {"q": "5. What is an AD (Airworthiness Directive)?", "o": ["A suggestion", "Mandatory instruction for safety", "A flight plan", "Part of a manual"], "a": "Mandatory instruction for safety", "ex": "ADs are issued by authorities to correct safety deficiencies."},
            {"q": "6. An 'A' license holder can certify?", "o": ["Major engine overhauls", "Minor scheduled line maintenance", "Avionics upgrades", "Nothing"], "a": "Minor scheduled line maintenance", "ex": "Category A is for line maintenance tasks."},
            {"q": "7. What is the role of the ICAO Annex 1?", "o": ["Environment", "Personnel Licensing", "Security", "Safe Transport of Goods"], "a": "Personnel Licensing", "ex": "Annex 1 sets global standards for licensing."},
            {"q": "8. A Form 1 (EASA) is a?", "o": ["Pilot logbook", "Authorized Release Certificate for components", "Design drawing", "Fuel receipt"], "a": "Authorized Release Certificate for components", "ex": "Form 1 certifies a component is airworthy."},
            {"q": "9. 'Continuing Airworthiness' is the responsibility of?", "o": ["The pilot", "The owner/operator", "The mechanic", "The airport"], "a": "The owner/operator", "ex": "The operator must ensure the aircraft stays airworthy."},
            {"q": "10. EASA Part 145 deals with?", "o": ["Pilot training", "Maintenance Organization Approval", "Manufacturing", "Medical standards"], "a": "Maintenance Organization Approval", "ex": "Defines rules for maintenance companies."},
            {"q": "11. An 'SB' (Service Bulletin) is issued by?", "o": ["The Government", "The Manufacturer", "The Pilot", "The Airport"], "a": "The Manufacturer", "ex": "Manufacturers issue SBs for improvements or fixes."},
            {"q": "12. What is 'MEL'?", "o": ["Minimum Equipment List", "Maximum Energy Level", "Main Engine Logic", "Maintenance Error List"], "a": "Minimum Equipment List", "ex": "Lists items that can be inoperative for a flight."},
            {"q": "13. Annex 6 of ICAO deals with?", "o": ["Security", "Operation of Aircraft", "Accident Investigation", "Search and Rescue"], "a": "Operation of Aircraft", "ex": "Standards for safe aircraft operations."},
            {"q": "14. A Category B1 license covers?", "o": ["Avionics only", "Mechanical (Airframe/Engine)", "Passenger service", "Cleaning"], "a": "Mechanical (Airframe/Engine)", "ex": "B1 is for mechanical systems and simple avionics."},
            {"q": "15. What is a Type Certificate?", "o": ["A pilot's ID", "Design approval for an aircraft type", "Fuel certificate", "Weight report"], "a": "Design approval for an aircraft type", "ex": "Issued when an aircraft design meets safety standards."},
            {"q": "16. Part M deals with?", "o": ["Manufacturing", "Continuing Airworthiness", "Medical", "Manuals"], "a": "Continuing Airworthiness", "ex": "Standards for keeping aircraft airworthy."},
            {"q": "17. An incident must be reported within?", "o": ["24 hours", "48 hours", "72 hours", "1 week"], "a": "72 hours", "ex": "Standard requirement for occurrence reporting."},
            {"q": "18. Who issues a Certificate of Airworthiness (C of A)?", "o": ["The Manufacturer", "The National Aviation Authority", "The Airline", "The Pilot"], "a": "The National Aviation Authority", "ex": "NAA issues the C of A after inspection."},
            {"q": "19. SARPs stand for?", "o": ["Security and Risk Plans", "Standards and Recommended Practices", "Search and Rescue Pilots", "System and Radio Parts"], "a": "Standards and Recommended Practices", "ex": "ICAO's regulatory framework."},
            {"q": "20. What is the purpose of EASA Part 147?", "o": ["Fueling rules", "Maintenance Training Organizations", "Design rules", "Landing fees"], "a": "Maintenance Training Organizations", "ex": "Defines rules for training mechanics."}
        ]
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m10_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 10 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m10_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m10_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m10_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 10"):
                st.session_state.m3_submitted = False
                st.rerun()# (Add sa# (Add same Submit/Review Logic as Module 4)
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
    
        st.write("---")
        st.header("✈️ MODULE 11: AEROPLANE SYSTEMS")
        m11_questions = [
            {"q": "1. What is the primary function of a slat?", "o": ["Decrease drag", "Increase lift at high AOA", "Speed up air", "Cool wings"], "a": "Increase lift at high AOA", "ex": "Slats delay the stall at low speeds."},
            {"q": "2. Hydraulic fluid in commercial aircraft is usually?", "o": ["Red mineral oil", "Skydrol (Purple)", "Water", "Engine oil"], "a": "Skydrol (Purple)", "ex": "Skydrol is fire-resistant but corrosive."},
            {"q": "3. A 'Monocoque' structure carries loads in the?", "o": ["Internal frame", "External skin", "Fuel tanks", "Engines"], "a": "External skin", "ex": "In monocoque, the skin itself carries the stress."},
            {"q": "4. What is the purpose of an Accumulator in hydraulics?", "o": ["Filter fluid", "Store pressurized fluid", "Cool fluid", "Measure pressure"], "a": "Store pressurized fluid", "ex": "Stores energy and dampens pressure surges."},
            {"q": "5. Aircraft oxygen systems for passengers typically use?", "o": ["Liquid oxygen", "Chemical oxygen generators", "Scuba tanks", "Air pumps"], "a": "Chemical oxygen generators", "ex": "Commonly found in overhead passenger units."},
            {"q": "6. What is 'Pressurization' maintained by?", "o": ["Bleed air", "Exhaust gas", "External fans", "Oxygen tanks"], "a": "Bleed air", "ex": "Air is bled from the engine compressor to pressurize the cabin."},
            {"q": "7. A 'Fail-safe' structure is designed to?", "o": ["Never fail", "Carry loads after a partial failure", "Be very light", "Explode safely"], "a": "Carry loads after a partial failure", "ex": "Uses redundant load paths for safety."},
            {"q": "8. What is the function of a 'Trim Tab'?", "o": ["Increase speed", "Reduce pilot control pressure", "Open doors", "Lock the engine"], "a": "Reduce pilot control pressure", "ex": "Helps maintain a flight attitude without pilot effort."},
            {"q": "9. Anti-skid systems work by?", "o": ["Locking wheels", "Modulating brake pressure", "Stopping the engine", "Adding weight"], "a": "Modulating brake pressure", "ex": "Prevents wheels from locking and skidding."},
            {"q": "10. What is a 'Spars' in a wing?", "o": ["Wing surface", "Main longitudinal member", "The tip", "Fuel pump"], "a": "Main longitudinal member", "ex": "Spars carry the main structural loads of the wing."},
            {"q": "11. 'Bleed Air' for cabin heating comes from?", "o": ["Combustion chamber", "Engine Compressor", "Turbine", "Exhaust"], "a": "Engine Compressor", "ex": "Compressed air is hot and clean before combustion."},
            {"q": "12. What is the purpose of a Check Valve?", "o": ["Allow flow in one direction", "Stop all flow", "Increase pressure", "Measure temperature"], "a": "Allow flow in one direction", "ex": "Prevents backflow in systems."},
            {"q": "13. In a tricycle landing gear, the steering is usually on?", "o": ["Main wheels", "Nose wheel", "Tail wheel", "Wings"], "a": "Nose wheel", "ex": "The nose gear is used for ground steering."},
            {"q": "14. A 'Vapour Cycle' system is used for?", "o": ["Fueling", "Air conditioning", "De-icing", "Lighting"], "a": "Air conditioning", "ex": "Uses a refrigerant to cool the air."},
            {"q": "15. Pitot-static systems measure?", "o": ["Fuel level", "Airspeed and Altitude", "Engine RPM", "Tire pressure"], "a": "Airspeed and Altitude", "ex": "Uses air pressure to calculate flight data."},
            {"q": "16. What is the function of a 'Fuselage'?", "o": ["Hold cargo and passengers", "Create lift", "Burn fuel", "Steer the plane"], "a": "Hold cargo and passengers", "ex": "The main body of the aircraft."},
            {"q": "17. A 'Servo Tab' moves in the?", "o": ["Same direction as control surface", "Opposite direction to control surface", "Inward", "Outward"], "a": "Opposite direction to control surface", "ex": "Assists in moving large surfaces."},
            {"q": "18. Ice on the wings causes?", "o": ["More lift", "Increased drag and decreased lift", "Higher speed", "Better fuel economy"], "a": "Increased drag and decreased lift", "ex": "Ice disrupts the smooth airflow over the wing."},
            {"q": "19. The 'Shimmy Damper' prevents?", "o": ["Fuel leaks", "Nose wheel vibration", "Engine noise", "Tail movement"], "a": "Nose wheel vibration", "ex": "Stops oscillations during taxiing and takeoff."},
            {"q": "20. What is 'Fly-by-Wire'?", "o": ["Using cables to fly", "Electronic signals control surfaces", "Using a kite", "Old technology"], "a": "Electronic signals control surfaces", "ex": "The pilot's inputs are sent via wires as electrical signals."}
        ]
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m11_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 11 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m11_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m11_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m11_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 11"):
                st.session_state.m3_submitted = False
                st.rerun()# (Add sa# (Add 
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
    
        st.write("---")
        st.header("🚁 MODULE 12: HELICOPTER SYSTEMS")
        m12_questions = [
            {"q": "1. What control changes the pitch of all rotor blades equally?", "o": ["Cyclic", "Collective", "Rudder pedals", "Throttle"], "a": "Collective", "ex": "Collective control increases or decreases total lift."},
            {"q": "2. The 'Cyclic' control is used for?", "o": ["Up/Down movement", "Directional (Forward/Back/Side) movement", "Starting the engine", "Tail rotor speed"], "a": "Directional (Forward/Back/Side) movement", "ex": "Changes the tilt of the rotor disk."},
            {"q": "3. What is the purpose of the Tail Rotor?", "o": ["To create lift", "To counteract torque", "To cool the cabin", "To increase speed"], "a": "To counteract torque", "ex": "Prevents the helicopter body from spinning in the opposite direction of the main rotor."},
            {"q": "4. 'Autorotation' is a state where?", "o": ["The engine is at full power", "The rotor is driven by air instead of engine", "The helicopter is upside down", "The tail rotor fails"], "a": "The rotor is driven by air instead of engine", "ex": "Allows for a safe landing during engine failure."},
            {"q": "5. What is 'Translational Lift'?", "o": ["Lift from a crane", "Extra lift gained when moving forward", "Lift from the tail", "Static lift"], "a": "Extra lift gained when moving forward", "ex": "Increased rotor efficiency as airspeed increases."},
            {"q": "6. A 'Fully Articulated' rotor head can?", "o": ["Only rotate", "Flap, Drag, and Feather", "Not move at all", "Only feather"], "a": "Flap, Drag, and Feather", "ex": "Allows blades to move in three axes for stability."},
            {"q": "7. 'Ground Effect' occurs within which height?", "o": ["1000 feet", "One rotor diameter height", "10,000 feet", "5 miles"], "a": "One rotor diameter height", "ex": "Air trapped between the rotor and ground increases lift efficiency."},
            {"q": "8. What is 'Dissymmetry of Lift'?", "o": ["Weight imbalance", "Advancing blade having more lift than retreating blade", "Broken wings", "Low fuel"], "a": "Advancing blade having more lift than retreating blade", "ex": "Caused by the forward speed of the helicopter added to rotor speed."},
            {"q": "9. The 'Swash Plate' converts?", "o": ["Fuel to energy", "Pilot inputs to rotor blade pitch", "Electricity to heat", "Sound to vibration"], "a": "Pilot inputs to rotor blade pitch", "ex": "Consists of stationary and rotating parts to transmit control."},
            {"q": "10. 'Retreating Blade Stall' limits a helicopter's?", "o": ["Altitude", "Maximum forward speed", "Fuel capacity", "Passenger count"], "a": "Maximum forward speed", "ex": "The retreating blade loses lift at high forward speeds."},
            {"q": "11. What is 'Coriolis Effect' in a rotor?", "o": ["Blade temperature", "Acceleration/Deceleration as blade flaps", "Radio noise", "Wind speed"], "a": "Acceleration/Deceleration as blade flaps", "ex": "Relates to conservation of angular momentum."},
            {"q": "12. A 'Semirigid' rotor system uses?", "o": ["One blade", "A teetering hinge", "Hydraulic motors", "Fixed blades"], "a": "A teetering hinge", "ex": "Common in two-bladed helicopters like Bell 206."},
            {"q": "13. The main rotor transmission is used to?", "o": ["Generate electricity", "Reduce engine RPM to rotor RPM", "Pump fuel", "Heat the oil"], "a": "Reduce engine RPM to rotor RPM", "ex": "Engines spin much faster than rotors."},
            {"q": "14. 'Feathering' a blade means?", "o": ["Cleaning it", "Changing its pitch angle", "Removing it", "Painting it"], "a": "Changing its pitch angle", "ex": "Feathering controls the lift of the blade."},
            {"q": "15. Tail rotor pedals control?", "o": ["Vertical movement", "Yaw (Heading)", "Pitch", "Engine RPM"], "a": "Yaw (Heading)", "ex": "Pedals change tail rotor pitch to control direction."},
            {"q": "16. What is a 'Fenestron'?", "o": ["A type of wing", "A shrouded tail rotor", "A fuel tank", "A glass window"], "a": "A shrouded tail rotor", "ex": "Enclosed tail rotor for safety and noise reduction."},
            {"q": "17. 'Lead-lag' movement is also known as?", "o": ["Flapping", "Hunting/Dragging", "Feathering", "Hovering"], "a": "Hunting/Dragging", "ex": "Movement of the blade in the plane of rotation."},
            {"q": "18. A 'NOTAR' system uses?", "o": ["Two main rotors", "Air jets instead of tail rotor", "Batteries", "No fuel"], "a": "Air jets instead of tail rotor", "ex": "NO TAil Rotor technology uses air for torque control."},
            {"q": "19. Helicopter transmissions usually require?", "o": ["Water cooling", "Dedicated oil cooling system", "No lubrication", "Manual greasing"], "a": "Dedicated oil cooling system", "ex": "Transmissions generate significant heat during operation."},
            {"q": "20. 'Settling with Power' is also called?", "o": ["Hovering", "Vortex Ring State", "Fast landing", "Normal descent"], "a": "Vortex Ring State", "ex": "A dangerous condition where the helicopter sinks into its own downwash."}
        ]
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m12_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 12 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m12_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m12_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m12_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 12"):
                st.session_state.m3_submitted = False
                st.rerun()
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
    
        st.write("---")
        st.header("📡 MODULE 13: AIRCRAFT SYSTEMS (AVIONICS)")
        m13_questions = [
            {"q": "1. What does EFIS stand for?", "o": ["Electronic Flight Instrument System", "Engine Fuel Indicator System", "Emergency Flight Internal System", "None"], "a": "Electronic Flight Instrument System", "ex": "EFIS uses digital displays instead of mechanical gauges."},
            {"q": "2. The 'Pitot Tube' measures which type of pressure?", "o": ["Static Pressure", "Total (Pitot) Pressure", "Cabin Pressure", "Fuel Pressure"], "a": "Total (Pitot) Pressure", "ex": "Pitot tubes capture the ram air pressure."},
            {"q": "3. What is the purpose of an ILS (Instrument Landing System)?", "o": ["To measure fuel", "To provide guidance during landing", "To talk to passengers", "To start the engine"], "a": "To provide guidance during landing", "ex": "ILS provides lateral and vertical guidance to the runway."},
            {"q": "4. A 'VHF' radio typically operates in which frequency range?", "o": ["3 - 30 kHz", "118 - 137 MHz", "1 - 2 GHz", "None"], "a": "118 - 137 MHz", "ex": "VHF is used for short-range air-to-ground communication."},
            {"q": "5. What is the function of an FMS (Flight Management System)?", "o": ["Automate flight planning and navigation", "Cool the engine", "Control cabin lights", "Deploy landing gear"], "a": "Automate flight planning and navigation", "ex": "FMS acts as the 'brain' of modern aircraft navigation."},
            {"q": "6. 'TCAS' is used to prevent?", "o": ["Engine failure", "Mid-air collisions", "Fuel leaks", "Rain"], "a": "Mid-air collisions", "ex": "Traffic Collision Avoidance System alerts pilots to nearby aircraft."},
            {"q": "7. What does the 'Black Box' (FDR) record?", "o": ["Only pilot voices", "Flight data parameters", "The weather", "Passenger names"], "a": "Flight data parameters", "ex": "Flight Data Recorder stores technical info for accident investigation."},
            {"q": "8. An 'Altimeter' works based on?", "o": ["Radio waves", "Barometric pressure", "Engine speed", "GPS only"], "a": "Barometric pressure", "ex": "It measures static pressure to determine altitude."},
            {"q": "9. 'Weather Radar' typically uses which band?", "o": ["X-band", "L-band", "HF-band", "VLF-band"], "a": "X-band", "ex": "X-band is ideal for detecting precipitation (rain/storm)."},
            {"q": "10. What is 'Fly-by-Wire'?", "o": ["Flying with ropes", "Electrical signals to control actuators", "Old style control", "Flying near power lines"], "a": "Electrical signals to control actuators", "ex": "Replaces mechanical cables with electrical wiring."},
            {"q": "11. The 'Autopilot' uses which device to sense movement?", "o": ["Thermometers", "Gyroscopes", "Barometers", "Cameras"], "a": "Gyroscopes", "ex": "Gyros sense changes in pitch, roll, and yaw."},
            {"q": "12. What is the purpose of a Static Wick?", "o": ["To light a fire", "To dissipate static electricity into the air", "To measure wind", "To hold the wing"], "a": "To dissipate static electricity into the air", "ex": "Prevents radio interference by releasing static charge."},
            {"q": "13. 'DME' (Distance Measuring Equipment) measures?", "o": ["Ground distance", "Slant range distance", "Height", "Weight"], "a": "Slant range distance", "ex": "The direct line-of-sight distance between aircraft and station."},
            {"q": "14. An 'ADF' (Automatic Direction Finder) points to?", "o": ["The North Pole", "An NDB station", "The Sun", "The Moon"], "a": "An NDB station", "ex": "Non-Directional Beacons are used with ADF for navigation."},
            {"q": "15. What is 'BITE' in avionics?", "o": ["A type of tooth", "Built-In Test Equipment", "Basic Internal Tool", "None"], "a": "Built-In Test Equipment", "ex": "BITE allows systems to test themselves for faults."},
            {"q": "16. 'VOR' is used for?", "o": ["Communication", "Short-range navigation", "Landing in fog", "Measuring oil"], "a": "Short-range navigation", "ex": "VHF Omnidirectional Range provides bearing info."},
            {"q": "17. A 'Transponder' sends info to?", "o": ["The Pilot", "Air Traffic Control (ATC) Radar", "The Engine", "Other passengers"], "a": "Air Traffic Control (ATC) Radar", "ex": "Provides identification and altitude to controllers."},
            {"q": "18. 'LRU' stands for?", "o": ["Long Range Unit", "Line Replaceable Unit", "Light Radio Unit", "None"], "a": "Line Replaceable Unit", "ex": "Modular components that can be quickly replaced on the flight line."},
            {"q": "19. Fiber optic cables use _____ to transmit data?", "o": ["Electricity", "Light", "Sound", "Water"], "a": "Light", "ex": "Light signals allow for high-speed, interference-free data."},
            {"q": "20. The primary purpose of a 'Radome' is?", "o": ["Aerodynamic protection for radar", "Holding fuel", "Passenger window", "Baggage door"], "a": "Aerodynamic protection for radar", "ex": "The nose cone made of material that allows radar waves to pass."}
        ]
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m13_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 13 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m13_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m13_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m13_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 13"):
                st.session_state.m3_submitted = False
                st.rerun()
    
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

        st.write("---")
        st.header("🚀 MODULE 14: PROPULSION (GAS TURBINE ENGINES)")
        m14_questions = [
            {"q": "1. What is the correct order of the Brayton Cycle?", "o": ["Intake, Compression, Combustion, Exhaust", "Intake, Exhaust, Compression, Combustion", "Compression, Intake, Exhaust, Combustion", "None"], "a": "Intake, Compression, Combustion, Exhaust", "ex": "Also known as Suck, Squeeze, Bang, Blow."},
            {"q": "2. A 'Turbojet' engine produces thrust by?", "o": ["A large fan", "High-velocity exhaust gases", "Propellers", "Pushing the ground"], "a": "High-velocity exhaust gases", "ex": "All thrust comes from the exhaust jet."},
            {"q": "3. The 'Compressor' in a jet engine increases air?", "o": ["Volume", "Velocity", "Pressure", "Humidity"], "a": "Pressure", "ex": "Compressors squeeze the air before combustion."},
            {"q": "4. What is the purpose of the 'Turbine'?", "o": ["Create thrust", "Drive the compressor", "Cool the air", "Filter fuel"], "a": "Drive the compressor", "ex": "The turbine extracts energy from hot gases to turn the compressor shaft."},
            {"q": "5. In a 'High Bypass' Turbofan, most thrust comes from?", "o": ["The core exhaust", "The bypass fan", "The combustion chamber", "The tailpipe"], "a": "The bypass fan", "ex": "Bypass air provides 75-80% of the thrust in modern engines."},
            {"q": "6. 'Newton's Third Law' states that every action has?", "o": ["No reaction", "An equal and opposite reaction", "A small reaction", "Heat"], "a": "An equal and opposite reaction", "ex": "The basis of jet propulsion."},
            {"q": "7. What is the function of the 'Stators' in a compressor?", "o": ["To spin fast", "To redirect air and increase pressure", "To burn fuel", "To stop the engine"], "a": "To redirect air and increase pressure", "ex": "Stators convert kinetic energy into pressure energy."},
            {"q": "8. 'Secondary Air' in a combustion chamber is used for?", "o": ["Burning fuel", "Cooling the liner", "Increasing speed", "Starting the fire"], "a": "Cooling the liner", "ex": "Protects the metal parts from melting."},
            {"q": "9. A 'Centrifugal Compressor' uses _____ to increase pressure?", "o": ["Pistons", "Centrifugal force", "Magnets", "Water"], "a": "Centrifugal force", "ex": "Air is slung outward to increase pressure."},
            {"q": "10. What is 'Surge' in an engine?", "o": ["High power", "Complete breakdown of airflow through the compressor", "Extra fuel", "A smooth landing"], "a": "Complete breakdown of airflow through the compressor", "ex": "A dangerous reversal of airflow."},
            {"q": "11. 'EGT' stands for?", "o": ["Engine Gas Temperature", "Exhaust Gas Temperature", "External Gear Torque", "None"], "a": "Exhaust Gas Temperature", "ex": "Critical parameter for engine health monitoring."},
            {"q": "12. What fuel is most common for jet engines?", "o": ["Avgas 100LL", "Jet A-1 (Kerosene based)", "Diesel", "Nitrogen"], "a": "Jet A-1 (Kerosene based)", "ex": "Kerosene has high energy density and safety features."},
            {"q": "13. An 'Afterburner' increases thrust by?", "o": ["More compression", "Injecting fuel into the exhaust", "Reducing weight", "Slowing down"], "a": "Injecting fuel into the exhaust", "ex": "Adds extra energy to the exhaust gas for supersonic flight."},
            {"q": "14. The 'Diffuser' section does what?", "o": ["Speeds up air", "Decreases velocity and increases pressure", "Burns fuel", "Rotates the shaft"], "a": "Decreases velocity and increases pressure", "ex": "Prepares air for the combustion chamber."},
            {"q": "15. What is 'Bypass Ratio'?", "o": ["Fuel to air ratio", "Ratio of bypass air to core air", "Speed to weight ratio", "None"], "a": "Ratio of bypass air to core air", "ex": "High bypass means more air goes around the core."},
            {"q": "16. 'Thrust Reversers' are used for?", "o": ["Going backward in air", "Assisting braking during landing", "Starting the engine", "Increasing altitude"], "a": "Assisting braking during landing", "ex": "Redirects thrust forward to slow the aircraft down."},
            {"q": "17. A 'Turboprop' engine drives a?", "o": ["Fan", "Propeller", "Wheels", "Pump"], "a": "Propeller", "ex": "Turbine energy is used to turn a propeller via a gearbox."},
            {"q": "18. What is the purpose of 'Igniters'?", "o": ["To stay on forever", "To start the combustion process", "To clean the engine", "To measure heat"], "a": "To start the combustion process", "ex": "Similar to spark plugs, used during start-up or heavy rain."},
            {"q": "19. 'N1' usually refers to?", "o": ["Core speed", "Low-pressure compressor/Fan speed", "Oil pressure", "Fuel flow"], "a": "Low-pressure compressor/Fan speed", "ex": "A primary thrust indicator on many engines."},
            {"q": "20. Engine 'Oil' is used for?", "o": ["Combustion", "Lubrication and Cooling", "Weight", "Cleaning windows"], "a": "Lubrication and Cooling", "ex": "Protects high-speed bearings from heat and friction."}
        ]
        
        if 'm3_submitted' not in st.session_state:
            st.session_state.m3_submitted = False
            st.session_state.m3_score = 0

        user_ans_m3 = []
        for i, item in enumerate(m14_questions):
            st.markdown(f"**Q{i+1}: {item['q']}**")
            ans = st.radio(f"Select answer for Q{i+1}:", item['o'], key=f"m3_q{i}", index=None)
            user_ans_m3.append(ans)

        if st.button("🚀 SUBMIT MODULE 14 EXAM"):
            st.session_state.m3_submitted = True
            st.session_state.m3_score = sum(1 for i, item in enumerate(m14_questions) if user_ans_m3[i] == item['a'])
            st.rerun()

        if st.session_state.m3_submitted:
            st.write("---")
            perc = (st.session_state.m3_score / len(m14_questions)) * 100
            if perc >= 75:
                st.balloons()
                st.success(f"🎊 PASS! Score: {st.session_state.m3_score}/20 ({perc}%)")
            else:
                st.error(f"❌ FAIL. Score: {st.session_state.m3_score}/20 ({perc}%). Pass is 75%.")

            with st.expander("🔍 Review Corrections"):
                for i, item in enumerate(m14_questions):
                    is_correct = (user_ans_m3[i] == item['a'])
                    if is_correct:
                        st.write(f"Q{i+1}: Correct ✅")
                    else:
                        correct_val = item['a']
                        st.write(f"Q{i+1}: Incorrect ❌ (Correct: {correct_val})")
                        st.caption(f"Reason: {item['ex']}")

            if st.button("🔄 RETAKE MODULE 14"):
                st.session_state.m3_submitted = False
                st.rerun()

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
        <div style="font-size: 28px; color: #00FF00; font-weight: bold;"> THANK YOU FOR USING AVIONIX MASTER CORE</div>
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