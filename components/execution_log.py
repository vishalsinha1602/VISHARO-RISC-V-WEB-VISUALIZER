import streamlit as st

def execution_log():
    st.markdown(
        """
       
            <div class="log-title">EXECUTION LOG</div>
            <div id="log-box" class="log-box"></div>
        """,
        unsafe_allow_html=True
    )
    return st.empty()
