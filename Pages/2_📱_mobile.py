import streamlit as st
from streamlit_lottie import st_lottie
import json
import pickle
import numpy as np
import time

st.set_page_config(
    page_title="Mobile-Price-Prediction",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded",
)

mob = pickle.load(open('Pages\mob.pkl', 'rb'))
df_mob = pickle.load(open('Pages\df_mob.pkl', 'rb'))

st.title("Mobile Predictor")
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.sidebar.info("This is Mobile Price Pridiction Section")

# Brande
Brand = st.selectbox('Brand of Mobile', df_mob['Big_brands'].unique())

# RAM
Ram = st.selectbox('RAM in GB', df_mob['RAM'].unique())

# Processor
Processor = st.selectbox('Processor', df_mob['Processor'].unique())

# Battery
Battery = st.selectbox('Battery in MAh', df_mob['Battery'].unique())

# Rear Camera
Rear_Camera = st.selectbox('Rear camera in MP', df_mob['Rear Camera'].unique())

# Front Camera
Front_Camera = st.number_input('Front Camera in MP')

# Display
Display = st.number_input('Display in Inches')

# Operating System
Operating_System = st.selectbox(
    'Operating_System', df_mob['Operating System'].unique())

# Fabrication
Fabrication = st.selectbox('Fabrication of Mobile', df_mob['Fabrication'].unique())

# Graphics
Graphics = st.selectbox('Graphics of Mobile', df_mob['Graphics'].unique())

# Display Type
Display_Type = st.selectbox('Display of Mobile', df_mob['Display Type'].unique())

# Pixel Density
Pixel_Density = st.number_input('Pixel_Density of Mobile(PPI)')

# Refresh Rate
Refresh_Rate = st.selectbox(
    'Refresh Rate of Mobile', df_mob['Refresh Rate'].unique())

# Quick Charging
Quick_Charging = st.selectbox('Does it have quick charging?', ['Yes', 'No'])

# USB Type-C
Usb_Type_C = st.selectbox('Is it USB Tupe-C', ['Yes', 'No'])

# Internal Memory
Internal_Memory = st.selectbox(
    'Internal Memory of Mobile', df_mob['Internal Memory'].unique())

# Expandable Memory
Expandable_Memory = st.selectbox(
    'Does it Have Option for Expandable Memory', ['Yes', 'No'])

# Audio Jack
Audio_Jack = st.selectbox('Does it have Audio Jack', ['Yes', 'No'])


# LOTTY file
def load_lottyFile(filename: str):
    with open (filename, 'r') as f:
        return json.load(f)

lotty_animation = load_lottyFile('Pages/lotty.json')

# PREDICT button
if st.button("Predict Price"):
    Quick_Charging = 1 if Quick_Charging == 'Yes' else 0
    Usb_Type_C     = 1 if Usb_Type_C == 'Yes' else 0
    Expandable_Memory = 1 if Expandable_Memory == 'Yes' else 0
    Audio_Jack     = 1 if Audio_Jack == 'Yes' else 0

    query = np.array([Ram,Processor,Battery,Rear_Camera,Front_Camera,Display,Operating_System,
                      Fabrication,Graphics,Display_Type,Pixel_Density,Refresh_Rate,
                      Quick_Charging,Usb_Type_C,Internal_Memory,Expandable_Memory,Audio_Jack,
                      Brand])
    
    query = query.reshape(1, 18)
 
    # Predict the price
    Predicted_price = int(np.exp(mob.predict(query)[0]))
    st_lottie(lotty_animation, key='shiv', loop=True, height=400, width=300)
    time.sleep(2)
    st.title(f'The predicted price of this configuration is: {Predicted_price}💸 ')
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Use an expander to show/hide the configuration details
    with st.expander("Show Configuration"):
        st.write(query)

    st.balloons()

