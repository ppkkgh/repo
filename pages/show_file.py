import streamlit as st

# get first parameter
file_path = st.experimental_get_query_params().get('file')[0]

# get name only
if '\\' in file_path:
    file_name = file_path.split('\\')[-1]
else:
    file_name = file_path.split('/')[-1]


# set title
st.set_page_config(page_title=file_name)
# st.title(file_name)
# st.write("file name:", file_name)

# show file contents
with open(file_path, 'r', encoding='utf-8') as f:
    if file_path.endswith('.html'):
        st.write(f.read(), unsafe_allow_html=True)
    else:
        st.write(f.read())