import streamlit as st

def simulation_result(result=None):
    """
    Display simulation result summary (status, message, cycles, CPI, etc.).
    """
    st.markdown("<h3 class='section-title'>Simulation Result</h3>", unsafe_allow_html=True)

    # Default placeholder values
    if not result:
        result = {
            "status": "N/A",
            "message": "N/A",
            "total_cycle": "N/A",
            "cpi": "N/A",
            "total_instructions": "N/A"
        }

    # Layout for top row
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <p class="result-title">STATUS</p>
            <p class="result-value">{result['status']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="result-card">
            <p class="result-title">MESSAGE</p>
            <p class="result-value">{result['message']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Layout for bottom row
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"""
    <div class="result-card">
        <p class="result-title">TOTAL CYCLE</p>
        <p class="result-value">{result['total_cycle']}</p>
    </div>
    """, unsafe_allow_html=True)

    c2.markdown(f"""
    <div class="result-card">
        <p class="result-title" style="font-size:15px">CYCLE PER INSTRUCTION</p>
        <p class="result-value">{result['cpi']}</p>
    </div>
    """, unsafe_allow_html=True)

    c3.markdown(f"""
    <div class="result-card">
        <p class="result-title" style="font-size:12px" >TOTAL EXECUTED INSTRUCTION</p>
        <p class="result-value">{result['total_instructions']}</p>
    </div>
    """, unsafe_allow_html=True)
