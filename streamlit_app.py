import xgboost as xgb
import streamlit as st
import pandas


# Testing Streamlit


streamlit.title('Credit Card Prediction')


option = streamlit.selectbox('DO YOU OWN A PROPERTY',("N","Y"))

streamlit.write('You selected:', option)
