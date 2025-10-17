import streamlit as st
from components.code_editor import code_editor
from components.execution_log import execution_log
from components.control_buttons import control_buttons
from utils.simulator import run_code, reset_state, step_code
from components.register_file import render_register_file
# Load CSS
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h3 class='title'>VISHARO → RISC-V WEB-VISUALIZER</h3>", unsafe_allow_html=True)

# Layout

col1, col2 = st.columns(2)

with col1:
    user_code = code_editor()

with col2:
    log_area = execution_log()

# Buttons
action = control_buttons()

# Logic for buttons
if action == "run":
    output = run_code(user_code)
    st.session_state['log'] = output
elif action == "reset":
    reset_state()
elif action == "step":
    output = step_code(user_code)
    st.session_state['log'] = output

# Update execution log
if 'log' in st.session_state:
    log_area.markdown(st.session_state['log'])

#register file 



# Optional: list of used registers (update this dynamically in your simulator)
render_register_file()

#simulation result

from components.simulation_result import simulation_result

# ...

# Simulation result (after register file)
if 'log' in st.session_state:
    # Assuming your simulator returns metrics along with log
    result = st.session_state.get("simulation_result", None)
    simulation_result(result)
else:
    simulation_result()
