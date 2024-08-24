import streamlit as st
import pickle
import numpy as np

# Load model (dictionary of songs and recommendations)
with open('final.pkl', 'rb') as f:
    weather_p = pickle.load(f)

# Streamlit app header
st.title("Weather Prediction")

# Create a form for weather input fields
with st.form("weather_form"):
    temperature = st.number_input("Enter the Temperature")
    humidity = st.number_input("Enter the Humidity (%)")   
    dew_point = st.number_input("Enter the Dew Point (°C)")
    bar = st.number_input("Enter the Barometer")
    wind = st.number_input("Enter the Wind Speed (km/h)")
    rain = st.number_input("Enter the Max Rain per Minute (mm)")
    heat= st.number_input("Enter the Maximum Heat Index (°C)")
    
    # Submit button
    submit_button = st.form_submit_button(label="PREDICT THE WEATHER")

# Action on form submission
if submit_button:
    # Example: Process input data (e.g., prediction)
    hh=weather_p.predict(np.array([[temperature,humidity,dew_point,bar,wind,rain,heat]]))
    if (hh==0):
        st.subheader("Weather Prediction : RAINFALL" )
    elif(hh==1):
        st.subheader("Weather Prediction : COOL" )
    elif(hh==2):
        st.subheader("Weather Prediction : EXTREAM HOT" )
    elif(hh==3):
        st.subheader("Weather Prediction : NORMAL " )
    else:
        st.subheader("Weather Prediction : SUNNY" )                
