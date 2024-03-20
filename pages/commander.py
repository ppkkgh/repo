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

    # Display stdout and stderr
    out = stdout.getvalue()
    if out:
        # st.header("Output")
        st.code(out, language="bash")
    
    err = stderr.getvalue()
    if err:
        st.header("stderr:")
        st.code(err, language="bash")

if __name__ == "__main__":
    app()