import streamlit as st

def control_buttons():
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("RESET", key="reset", use_container_width=True):
            return "reset"
    with col2:
        if st.button("RUN", key="run", use_container_width=True):
            return "run"
    with col3:
        if st.button("STEP", key="step", use_container_width=True):
            return "step"
    return None
