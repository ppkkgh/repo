# search anything in my PCs

import streamlit as st
import os
import urllib.parse

def file_path_to_url(path):
    return "/show_file?file=" + urllib.parse.quote(path)

def button_clicked(path):
    # run path
    os.system(f'notepad "{path}"')    

def search_files(directory, key):
    index = 0
    for root, dirs, files in os.walk(directory):
        root_short = root[len(directory_path):]
        for file_name in files:
            if key in file_name:
                index += 1
                # st.write(os.path.join(root, file))
                file_path = os.path.join(root, file_name)
                # take 20 characters from file_path
                # short_len = 70
                # file_name_short = file_name[:short_len] + ('..' if len(file_name) > short_len else '')
                st.button(str(index) + ": " + file_name, on_click=button_clicked, args=(file_path,))
                st.write(file_path)
                
                # Convert file path to URL
                file_url = file_path_to_url(file_path)

                # Linking to the converted URL
                st.markdown(f'[{file_path}]({file_url})')
                
                # TODO when click the file info, show content of the file
    st.write(f"Found #{index} files")

# Prompt user for directory path and key
directory_path = r"C:\Users\dhh\Dropbox"
search_key = st.text_input("Enter the search key: ")
# search_key = st.input("Enter the search key: ")

# Call the search_files function with user input

if search_key:
    search_files(directory_path, search_key)
