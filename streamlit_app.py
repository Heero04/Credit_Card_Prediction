import streamlit
import pandas
import requests


streamlit.title('TEST 2')

st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
