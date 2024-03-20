import streamlit as st

# Check if 'chat_messages' is already in the session state
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []


def execute_command(command): # execute command and return out, err
    import subprocess
    import sys
    
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return "", str(e)

# Create a text input for the user to type their message
user_input = st.text_input("Type your message here:")

# Create a button for the user to send their message
if st.button("Send"):
    # Append the user's message to the chat_messages list in the session state
    # st.session_state.chat_messages.append('You: ' + user_input)
    # run command and get output or error
    out, err = execute_command(user_input)
    st.session_state.chat_messages.append({ 'cmd': user_input, 'out': out, 'err': err })

# Display the chat messages
for message in reversed(st.session_state.chat_messages):
    # write message(json) as yaml
    txt = '$' + message['cmd'] + '\n' + message['out']
    if message['err']: 
        txt = txt + '\n* err:\n' + message['err']
    st.code(txt)
    # txt = '*out:\n' + message['out'] + '\n\n*err:\n' + message['err']
    # st.text_area(label=message['cmd'], value=txt)
