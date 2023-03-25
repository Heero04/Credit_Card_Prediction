 
import pickle
import streamlit as st
import streamlit
import pandas
import requests
from urllib.error import URLError

# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
# defining the function which will make the prediction using the data which the user inputs 
def prediction(OWN_A_PROPERTY, INCOME, MARITAL_STATUS, TYPE_OF_HOUSING):   
 
    # Pre-processing user input    
    if OWN_A_PROPERTY== 'N':
        OWN_A_PROPERTY = 0
    else:
        OWN_A_PROPERTY = 1
 
    if INCOME >= 106827:
         INCOME >= 106827
    else:
        INCOME =  0
 
    if MARITAL_STATUS == 'Civil marriage':
        MARITAL_STATUS = 0
    
    elif MARITAL_STATUS == 'Married':
            MARITAL_STATUS = 1
    
    elif MARITAL_STATUS == 'Single / not married':
            MARITAL_STATUS = 2
    
    elif MARITAL_STATUS == 'Separated':
            MARITAL_STATUS = 3
    
    elif MARITAL_STATUS == 'Widow':
            MARITAL_STATUS = 4
    else:
        MARITAL_STATUS = 5  
    
    if TYPE_OF_HOUSING == 'Rented apartment':
        TYPE_OF_HOUSING = 0
    
    elif TYPE_OF_HOUSING == 'House / apartment':
            TYPE_OF_HOUSING = 1

    elif TYPE_OF_HOUSING == 'With parents':
            TYPE_OF_HOUSING = 2
            
    elif TYPE_OF_HOUSING == 'Municipal apartment':
           TYPE_OF_HOUSING = 3
    
    elif TYPE_OF_HOUSING == 'Co-op apartment':
            TYPE_OF_HOUSING = 4
    
    elif TYPE_OF_HOUSING == 'Office apartment':
            TYPE_OF_HOUSING = 5
    else:
        TYPE_OF_HOUSING = 6 
 
  
    # Making predictions 
  prediction = classifier.predict([[OWN_A_PROPERTY, INCOME, MARITAL_STATUS, TYPE_OF_HOUSING]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred

# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    OWN_A_PROPERTY = st.selectbox('OWN_A_PROPERTY',("N","Y"))
    MARITAL_STATUS = st.selectbox('Marital Status',("Civil marriage","Married","Single / not married", "Separated", "Widow")) 
    INCOME = st.number_input("Applicants monthly income") 
    TYPE_OF_HOUSING = st.selectbox('TYPE_OF_HOUSING',("Rented apartment","House / apartment","With parents", "Municipal apartment", "Co-op apartment", "Office apartment"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
   if st.button("Predict"): 
    result = prediction(OWN_A_PROPERTY, INCOME, MARITAL_STATUS, TYPE_OF_HOUSING) 
    st.success(f'Your loan application is {result}')
