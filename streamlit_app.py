import streamlit
import pandas
import requests

# Testing Streamlit


streamlit.title('Credit Card Prediction')

option = streamlit.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

streamlit.selectbox('OWN_A_PROPERTY',("N","Y"))

streamlit.write('You selected:', option)
