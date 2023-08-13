import streamlit as st
import pickle
import numpy as np

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
Display = st.selectbox('Display', df_mob['Display'].unique())

# Operating System
Operating_System = st.selectbox(
    'Operating_System', df_mob['Operating System'].unique())

# Fabrication
Fabrication = st.number_input('Fabrication of Mobile (ex 8,6,12) int')

# Graphics
Graphics = st.selectbox('Graphics of Mobile', df_mob['Graphics'].unique())

# Display Type
Display_Type = st.selectbox(
    'Display of Mobile', df_mob['Display Type'].unique())

# Pixel Density
Pixel_Density = st.number_input('Pixel_Density of Mobile')

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
    
    st.write(query)

    # Predict the price
    Predicted_price = mob.predict(query)[0]
    st.title(Predicted_price)
    # st.balloons()