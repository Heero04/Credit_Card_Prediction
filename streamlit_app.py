import streamlit
import pandas
import requests


streamlit.title('TEST 2')

streamlit.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

streamlit.write('You selected:', option)
