# search anything in my PCs

import streamlit as st

import os

def button_clicked(path):
    # run path
    os.system(f'start {path}')    

def search_files(directory, key):
    index = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if key in file:
                index += 1
                # st.write(os.path.join(root, file))
                path = os.path.join(root, file)
                st.button(str(index) + ": " + file, on_click=button_clicked, args=(path,))
    st.write(f"Found #{index} files")

# Prompt user for directory path and key
directory_path = r"C:\Users\dhh\Dropbox"
search_key = st.text_input("Enter the search key: ")
# search_key = st.input("Enter the search key: ")

# Call the search_files function with user input

if search_key:
    search_files(directory_path, search_key)
