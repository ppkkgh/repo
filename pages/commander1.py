# TODO Goal: jupyter notebook?

import streamlit as st
import sys
from io import StringIO
import subprocess

# Overwrite stdout and stderr
stdout = StringIO()
stderr = StringIO()
sys.stdout = stdout
sys.stderr = stderr

# Function to execute user input
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stdout:
            print(result.stdout, file=sys.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

# Streamlit app
def app():
    st.title("Command Executor")
    command = st.text_input("Enter a command (press Enter to execute)")

    # Execute command when Enter key is pressed
    if st.session_state.get("command") != command:
        st.session_state["command"] = command
        if command:
            execute_command(command)
            st.write("---")  # Add a horizontal line separator

    # Display stdout and stderr
    out = stdout.getvalue()
    if out:
        st.code(out, language="bash")
    err = stderr.getvalue()
    if err:
        st.header("stderr:")
        st.code(err, language="bash")

    # Add a new input box below the result
    new_command = st.text_input("Enter a new command (press Enter to execute)")
    if st.session_state.get("new_command") != new_command:
        st.session_state["new_command"] = new_command
        if new_command:
            execute_command(new_command)
            st.write("---")  # Add a horizontal line separator

if __name__ == "__main__":
    app()