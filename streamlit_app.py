import streamlit
import pandas
import requests
from urllib.error import URLError

##streamlit.title('TEST 2')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
