import streamlit as st
from components.code_editor import code_editor
from components.execution_log import execution_log
from components.control_buttons import control_buttons
from utils.simulator import run_code, reset_state, step_code
from components.register_file import render_register_file
from components.simulation_result import simulation_result

# -------------------- LOAD GLOBAL CSS --------------------
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    
# -------------------- Header --------------------
st.markdown("""


<div class="footer">
    <p class="footer-title">💻 COA PROJECT — RISC-V WEB VISUALIZER</p>
    <p class="footer-sub">Under the Guidance of <strong>Asutosh Srivastava Sir</strong></p>
    <p class="footer-team">Developed by Team <strong>VISHARO</strong>:</p>
    <p class="footer-names">
        Vishal Kumar Sinha &nbsp; | &nbsp; Roseline &nbsp; | &nbsp; Harshita Sharma &nbsp; | &nbsp; Shweta
    </p>
</div>
            
<hr style="border: 1px solid #444; margin-top: 40px; margin-bottom: 10px;">
""", unsafe_allow_html=True)


# -------------------- APP TITLE --------------------
st.markdown("<h3 class='title'>VISHARO → RISC-V WEB-VISUALIZER</h3>", unsafe_allow_html=True)

# -------------------- MAIN LAYOUT --------------------
col1, col2 = st.columns(2)

with col1:
    user_code = code_editor()

with col2:
    log_area = execution_log()

# -------------------- CONTROL BUTTONS --------------------
action = control_buttons()

# -------------------- SIMULATION LOGIC --------------------
if action == "run":
    result_data, output_log = run_code(user_code)
    st.session_state["simulation_result"] = result_data
    st.session_state["log"] = output_log

elif action == "reset":
    reset_state()
    st.session_state.clear()

elif action == "step":
    result_data, output_log = step_code(user_code)
    st.session_state["simulation_result"] = result_data
    st.session_state["log"] = output_log

# -------------------- EXECUTION LOG --------------------
if "log" in st.session_state:
    log_area.markdown(st.session_state["log"], unsafe_allow_html=True)
else:
    log_area.markdown("<p style='color:gray;'>No output yet.</p>", unsafe_allow_html=True)

# -------------------- REGISTER FILE --------------------
render_register_file()

# -------------------- SIMULATION RESULT --------------------
simulation_result(st.session_state.get("simulation_result", None))

# -------------------- PIPELINE DIAGRAM (Coming Soon) --------------------
# You can add your visualization component here later:
# render_pipeline_diagram()


