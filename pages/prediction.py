# pages/prediksi.py
import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = 'model/gradient_boost_model.pkl'  # Adjusted path for the model
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Page title and description
st.title("Prediksi Tingkat Kesuburan Tanah")

# Input fields for soil nutrients
st.write("Masukkan nilai nutrisi tanah untuk melakukan prediksi:")
N = st.number_input("Kandungan Nitrogen (N)", min_value=0.0, step=0.1)
P = st.number_input("Kandungan Phosphorus (P)", min_value=0.0, step=0.1)
K = st.number_input("Kandungan Kalium (K)", min_value=0.0, step=0.1)
pH = st.number_input("pH Tanah", min_value=0.0, step=0.1)
Moisture = st.number_input("Kelembapan Tanah", min_value=0.0, step=0.1)
Cu = st.number_input("Kandungan Tembaga (Cu)", min_value=0.0, step=0.1)
Zn = st.number_input("Kandungan Seng (Zn)", min_value=0.0, step=0.1)

# Prediction button
if st.button("Prediksi"):
    # Prepare input data for the model
    input_data = np.array([[N, P, K, pH, Moisture, Cu, Zn]])
    # Make prediction
    prediction = model.predict(input_data)[0]

    # Map prediction to soil fertility label
    if prediction == 0:
        st.success("Prediksi: Tanah Tidak Subur")
    elif prediction == 1:
        st.success("Prediksi: Tanah Kurang Subur")
    else:
        st.success("Prediksi: Tanah Subur")
