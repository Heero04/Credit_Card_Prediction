import streamlit
import pandas
import requests

# this is the main function in which we define our webpage 


streamlit.title('TEST 2')

option = streamlit.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

streamlit.write('You selected:', option)
