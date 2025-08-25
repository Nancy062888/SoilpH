import streamlit as st
import numpy as np
import pickle
import joblib
from  tensorflow.keras.models import load_model

import   streamlit  as st; from PIL import Image; import numpy  as np
import pandas  as pd; import pickle

import os

filename1 = 'https://raw.githubusercontent.com/imsb1371/streamBiochar/refs/heads/main/Capture1.PNG'
# filename2 = 'https://raw.githubusercontent.com/imsb1371/streamBiochar/refs/heads/main/Capture2.PNG'

st.title('Prediction of Heavy Metal Removal Efficiency Using Biochar')
with st.container():
    st.image(filename1)
    # st.image(filename2)



# Arrange input boxes into three columns for input features
col1, col2 = st.columns(2)
with col1:
    mat = st.number_input('Mean annual temperature (°C)', 0.0)
with col2:
    map = st.number_input('Mean annual precipitation (mm)', 0.0)

col4, col5, col6 = st.columns(3)
with col4:
    Wetness = st.number_input('Wetness index', 0.0)
with col5:
    isoc = st.number_input('Initial soil organic carbon (g/kg)', 0.0)
with col6:
    itn = st.number_input('Initial total nitrogen (g/kg)', 0.0)

col7, col8, col9 = st.columns(3)
with col7:
    iph = st.number_input('Initial pH', 0.0)
with col8:
    bpt = st.number_input('Biochar pyrolysis temperature (°C)', 0.0)
with col9:
    bc = st.number_input('Biochar carbon (g/kg)', 0.0)

col10, col11, col12 = st.columns(3)
with col10:
    bn = st.number_input('Biochar nitrogen (g/kg)', 0.0)
with col11:
    bcnr = st.number_input('Biochar carbon/nitrogen ratio', 0.0)
with col12:
    BiopH = st.number_input('Biochar pH', 0.0)


col13, col14 = st.columns(2)
with col13:
    bioadd = st.number_input('Biochar addition (t/ha)', 0.0)
with col14:
    trd = st.number_input('Trial duration (day)', 0.0)

col17 = st.columns(1)
with col17[0]:
    treat = st.radio(
        'Treatment',
        [0, 1],
        help='0 = biochar-only applications; 1 = biochar combined with fertilizer'
    )

col18 = st.columns(1)
with col18[0]:
    cropt = st.radio(
        'Crop type',
        [0, 1],
        help='0 = no crop plant; 1 = crops plant'
    )

col19, col20, col21  = st.columns(3)
with col19:
    soild = st.number_input('Soil depth (cm)', 0.0)




# Gather all inputs into a list for normalization
input_values = [mat, map, Wetness, isoc, itn, iph, bpt, bc, bn, bcnr, BiopH, bioadd, trd, treat, cropt, soild] 



# Combine normalized inputs with one-hot encoding
inputvec = np.array(input_values)

# Check zeros only in the numeric features
zero_count = sum(1 for value in inputvec if value == 0)


if st.button('Run'):
    if zero_count > 5:
        st.error("Error: More than 5 inputs values are zero. Please provide valid inputs for features.")
    else:
        try:
            # Load the model
            model2 = joblib.load('model_bundle.joblib')

            # Predict using the model
            inputvec = inputvec.reshape(1, -1)  # Ensure correct shape
            YY = model2.predict(inputvec)

            # Display predictions
            col19, col20, col21 = st.columns(3)
            with col19:
                st.write("Soil pH following biochar treatment: ", np.round(abs(YY), 2))

        except Exception as e:
            st.error(f"Model prediction failed: {e}")



filename7 = 'https://raw.githubusercontent.com/imsb1371/streamBiochar/refs/heads/main/Capture3.PNG'
filename8 = 'https://raw.githubusercontent.com/imsb1371/streamBiochar/refs/heads/main/Capture4.PNG'

col22, col23 = st.columns(2)
with col22:
    with st.container():
        st.markdown("<h5>Developer:</h5>", unsafe_allow_html=True)
        st.image(filename8)

with col23:
    with st.container():
        st.markdown("<h5>Supervisor:</h5>", unsafe_allow_html=True)
        st.image(filename7) 


footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 12px;
    }
    </style>
    <div class="footer">
    This web app was developed in School of Resources and Safety Engineering, Central South University, Changsha 410083, China
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
