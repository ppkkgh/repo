import streamlit as st
import requests
import json

def chat_completion(user_prompt, sys_prompt, host, port):
    url = f'http://{host}:{port}/v1/chat/completions'
    headers = {'Content-Type': 'application/json'}
    data = {
        "messages": [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": True  # Set stream to True for continuous output
    }

    try:
        response = requests.post(url, headers=headers, json=data, stream=True)
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    try:
                        json_string = line.decode('utf-8')
                        if json_string == "data: [DONE]":
                            break

                        # remove leading "data:"
                        json_string = json_string[6:]
                        json_data = json.loads(json_string)
                        content = json_data.get('choices', [{}])[0].get('delta', {}).get('content', '')

                        if content:
                            # Write the streaming data to Streamlit using st.write_stream
                            st.write_stream(f"{content}")
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {line}")
        else:
            st.write(f"Oops! Check your LM Studio. response: {response}")
    except Exception as e:
        st.write(f"Oops! Did you start LM Studio server?\n\nERROR: {e}")

def main():
    st.title("Chat Completion App")
    user_prompt = st.text_area("Enter your prompt:")
    sys_prompt = st.text_area("Enter the system prompt (optional):", value="You are a helpful AI assistant.")
    host = st.text_input("Enter the host:", value="192.168.0.4")
    port = st.text_input("Enter the port:", value="1234")

    if st.button("Submit"):
        chat_completion(user_prompt, sys_prompt, host, port)

if __name__ == "__main__":
    main()
