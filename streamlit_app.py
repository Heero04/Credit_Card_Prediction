import streamlit
import pandas
import requests


streamlit.title('TEST 2')

st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")



option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
##OWN_A_PROPERTY = st.selectbox('OWN_A_PROPERTY',("N","Y"))
