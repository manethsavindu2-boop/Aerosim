if app_mode == "Dashboard":
        # Using the SR-71 Blackbird background
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://r.jina.ai/i/6ef2482283084334a179374026600989");
                background-attachment: fixed;
                background-size: cover;
            }}
            .main {{
                background: rgba(0, 0, 0, 0.7); 
                color: white;
                padding: 30px;
                border-radius: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        st.title("🦅 AVIONIX | SR-71 STRATEGIC COMMAND")
        st.subheader("Advanced Aerospace Engineering & EASA Suite")
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("System Speed", "Mach 3.2+")
        with col2:
            st.metric("EASA Status", "14 Modules Active")
        with col3:
            st.metric("Altitude", "85,000 ft")

        st.info("Welcome, Engineer. The Avionix Systems suite is fully operational. Select a module from the sidebar to begin.")