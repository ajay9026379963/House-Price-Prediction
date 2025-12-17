import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained data
model = joblib.load('House_price_Prediction.pkl')

st.title('House Price Prediction App')

# Input features

bedrooms= st.number_input('Number of bedroom', min_value=0, max_value=10)
bathrooms = st.number_input('Number of bathroom', min_value=1, max_value=10)
sqft_living = st.number_input('Score footage of leaving area', min_value=100, max_value=10000)
sqft_lot = st.number_input('Score footage of lot are', min_value=100, max_value=100000)
floors = st.number_input('Number of floors', min_value=1,max_value=5)
country = st.number_input('Country', min_value=1, max_value=2) #USA


# Prepare the input data for prediction 

input_data = pd.DataFrame({
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'sqft_living': [sqft_living],
    'sqft_lot': [sqft_lot],
    'floors': [floors],
    'country': [country]
    
    
})

# Make prediction 
if st.button('Predict Price'):
    prediction = model.predict(input_data)
    st.success(f'The predicted house price is: $[{prediction[0]:,.2f}]')
    
    