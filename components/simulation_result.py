import streamlit as st

def simulation_result(result=None):
    """
    Display the simulation result summary using existing CSS styles.
    """

    # Section Title
    st.markdown("<h3 class='section-title'>📊 Simulation Result</h3>", unsafe_allow_html=True)

    # Default placeholder result (if simulation not run yet)
    if result is None:
        result = {
            "status": "NOT RUN",
            "message": "Execute code to see results.",
            "total_cycle": 0,
            "cpi": 0.0,
            "total_instructions": 0
        }

    # Layout - Top row (Status, Message)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <p class="result-title">STATUS</p>
            <p class="result-value">{result.get('status', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="result-card">
            <p class="result-title">MESSAGE</p>
            <p class="result-value">{result.get('message', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

    # Layout - Bottom row (Cycles, CPI, Instructions)
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"""
    <div class="result-card">
        <p class="result-title">TOTAL CYCLES</p>
        <p class="result-value">{result.get('total_cycle', 0):,}</p>
    </div>
    """, unsafe_allow_html=True)

    c2.markdown(f"""
    <div class="result-card">
        <p class="result-title">CPI</p>
        <p class="result-value">{result.get('cpi', 0.0):.2f}</p>
    </div>
    """, unsafe_allow_html=True)

    c3.markdown(f"""
    <div class="result-card">
        <p class="result-title" style="font-size:13px">EXECUTED INSTRUCTIONS</p>
        <p class="result-value">{result.get('total_instructions', 0):,}</p>
    </div>
    """, unsafe_allow_html=True)
