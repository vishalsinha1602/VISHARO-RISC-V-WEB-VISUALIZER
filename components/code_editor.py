import streamlit as st

def code_editor():
    default_code = """.main:
    # write your code here

.end:
    ebreak
"""
    code = st.text_area(
    "Code Editor Input",
    default_code,
    height=300,
    key="code_editor",
    label_visibility="collapsed"
)
    return code
