import streamlit as st
import numpy as np
import pandas as pd
import time
import os
from PIL import Image

# st.title('Streamlit Test App')
st.set_page_config(page_title="My Streamlit Test")

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Print the directory
print("Script directory:", script_dir)

# show files in dir..
filelist = []
for root, dirs, files in os.walk(script_dir):
    for file in files:
        filename = os.path.join(root, file)
        filelist.append(filename)
st.write(filelist)

if st.checkbox('show chart'):
    chart_data = pd.DataFrame(
         np.random.randn(10, 2),
         columns=['a', 'b'])

    st.line_chart(chart_data)


if st.checkbox('show map'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)


if st.checkbox('show slider'):
    # slider
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)

if st.checkbox('show input box'):
    st.text_input("Your name", key="name")


if st.checkbox('show select box', value=True):

    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })

    option = st.selectbox(
        'Which number do you like best?',
         df['first column'])

    'You selected: ', option

if st.checkbox('show sidebar'):
    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )

    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )

if st.checkbox('show columns'):
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")

'Starting a long computation...'

if st.checkbox('show progress bar'):
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(5):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'Iteration {i+1}')
      bar.progress(i + 1)
      time.sleep(0.1)

    '...and now we\'re done!'
    
my_expander = st.expander(label='test', expanded=True)
my_expander.write('Hello there!')
clicked = my_expander.button('Click me!')

my_expander1 = st.expander(label='test1')
my_expander1.write('Hello there 1!')
clicked1 = my_expander1.button('Click me 1!')

# Open the image file
image = Image.open('image/sample.png')

# Display the image with a caption
st.image(image, caption='My sample image')

st.write('Hello, *World!* :sunglasses: is always the beginning!')
st.write('iteration is now 5')

# link sample
url = "https://github.com/ppkkgh/repo/edit/main/streamlit_app.py"
st.markdown(f"[source code is: streamlit_app.py]({url})", unsafe_allow_html=True)

# why not get notifications?
