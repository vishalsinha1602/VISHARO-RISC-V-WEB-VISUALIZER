import streamlit as st
def run_code(code):
    # Placeholder for your RISC-V simulation logic
    return "Program executed successfully!"

def reset_state():
    return "Simulator reset."

def step_code(code):
    return "Executed one instruction."


# for register file dynaic value change 
def run_code(code):
    # Example simulation result
    st.session_state['registers']['R1'] = 5
    st.session_state['registers']['R2'] = 8
    st.session_state['registers']['R10'] = 13
    return "Program executed successfully!"
