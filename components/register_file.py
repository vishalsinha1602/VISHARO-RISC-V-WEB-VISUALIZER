import streamlit as st

# MAPPING for the 32 RISC-V registers (x0 to x31)
# Maps numerical index (0-31) to the standard ABI name
RISCV_ABI_MAP = {
    0: 'zero (x0)', 1: 'ra (x1)', 2: 'sp (x2)', 3: 'gp (x3)',
    4: 'tp (x4)', 5: 't0 (x5)', 6: 't1 (x6)', 7: 't2 (x7)',
    8: 's0/fp (x8)', 9: 's1 (x9)', 10: 'a0 (x10)', 11: 'a1 (x11)',
    12: 'a2 (x12)', 13: 'a3 (x13)', 14: 'a4 (x14)', 15: 'a5 (x15)',
    16: 'a6 (x16)', 17: 'a7 (x17)', 18: 's2 (x18)', 19: 's3 (x19)',
    20: 's4 (x20)', 21: 's5 (x21)', 22: 's6 (x22)', 23: 's7 (x23)',
    24: 's8 (x24)', 25: 's9 (x25)', 26: 's10 (x26)', 27: 's11 (x27)',
    28: 't3 (x28)', 29: 't4 (x29)', 30: 't5 (x30)', 31: 't6 (x31)',
}


def render_register_file(used_registers=None):
    st.markdown("<h4 class='reg-title'>Register File</h4>", unsafe_allow_html=True)

    # 1. Get registers from session_state (dynamic)
    # The session state dictionary is assumed to use the numerical names (e.g., 'R0', 'R1', or 'x0', 'x1')
    registers_data = st.session_state.get('registers', {})

    # 2. If no register data yet, create placeholders using standard RISC-V naming convention
    if not registers_data:
        # Create placeholder UI with "N/A" values for consistent layout
        # We use a key that can be easily mapped, like 'x0', 'x1', etc., for consistency
        registers_data = {f"x{i}": "0" for i in range(32)}

    # 3. Create the final list of (ABI_NAME, VALUE) pairs to display
    display_regs_list = []

    for i in range(32):
        abi_name = RISCV_ABI_MAP[i]
        
        # Try to find the value using common key formats (R#, x#, or numerical index)
        # Assuming the key in session_state is either 'x0', 'x1', etc. (common in RISC-V simulators)
        key_x = f"x{i}"
        
        if key_x in registers_data:
            value = registers_data[key_x]
        else:
            # Fallback for systems using R# keys or if it's the placeholder '0'
            value = registers_data.get(f"R{i}", "0")
        
        # 4. Apply optional filtering (if used_registers are specified)
        # Note: 'used_registers' list should contain the *numerical* names (e.g., 'x1', 'x2')
        # for filtering to work with the session_state keys.
        if used_registers is None or key_x in used_registers:
            display_regs_list.append((abi_name, value))

    reg_items = display_regs_list

    # 5. Render in a grid layout (4 columns per row)
    num_cols = 4
    num_rows = (len(reg_items) + num_cols - 1) // num_cols

    for row in range(num_rows):
        # Use a list of st.column objects to ensure proper column creation
        cols = st.columns(num_cols) 
        for col_index in range(num_cols):
            idx = row * num_cols + col_index
            if idx < len(reg_items):
                reg_name, val = reg_items[idx]
                with cols[col_index]:
                    # The register name now uses the ABI standard
                    st.markdown(
                        f"""
                        <div class="reg-box">
                            <span class="reg-name">{reg_name}</span>
                            <span class="reg-value">{val}</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

# Example usage (assuming the session state has been initialized elsewhere)
# st.session_state['registers'] = {'x0': '0x00000000', 'x1': '0x80000000', 'x2': '0x7ffff000', ...}
# render_register_file(used_registers=['x1', 'x2', 'x10']) # Optional: filter to show only ra, sp, a0
# render_register_file() # Show all 32 registers