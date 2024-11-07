# pages/prediksi.py
import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model_path = 'model/gradient_boost_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Judul Halaman dan Deskripsi
st.title("Prediksi Tingkat Kesuburan Tanah")

# Input untuk nutrisi tanah
st.write("Masukkan nilai nutrisi tanah untuk melakukan prediksi:")

# Formulir input untuk setiap fitur tanah
col1,  col2 = st.columns([1, 1], vertical_alignment="center")
with col1:
    N = st.number_input("Rasio Nitrogen (NH4+) dalam tanah", min_value=0.0, step=0.1)
    P = st.number_input("Rasio Fosfor (P) dalam tanah", min_value=0.0, step=0.1)
    K = st.number_input("Rasio Kalium (K) dalam tanah", min_value=0.0, step=0.1)
    ph = st.number_input("Keasaman Tanah (pH)", min_value=0.0, step=0.1)
    ec = st.number_input("Kapasitas Konduktivitas Listrik", min_value=0.0, step=0.1)
    oc = st.number_input("Kandungan Karbon Organik", min_value=0.0, step=0.1)
with col2:
    S = st.number_input("Kandungan Sulfur (S)", min_value=0.0, step=0.1)
    zn = st.number_input("Kandungan Seng (Zn)", min_value=0.0, step=0.1)
    fe = st.number_input("Kandungan Besi (Fe)", min_value=0.0, step=0.1)
    cu = st.number_input("Kandungan Tembaga (Cu)", min_value=0.0, step=0.1)
    Mn = st.number_input("Kandungan Mangan (Mn)", min_value=0.0, step=0.1)
    B = st.number_input("Kandungan Boron (B)", min_value=0.0, step=0.1)

# Tombol untuk melakukan prediksi
if st.button("Prediksi"):
    # Definsikan nama kolom yang sesuai dengan pelatihan model
    feature_names = ['N', 'P', 'K', 'pH', 'EC', 'OC', 'S', 'Zn', 'Fe', 'Cu', 'Mn', 'B']
    # Mempersiapkan data input untuk model
    input_data = pd.DataFrame([[N, P, K, ph, ec, oc, S, zn, fe, cu, Mn, B]], columns=feature_names)
    
    # Melakukan prediksi
    prediction = model.predict(input_data)[0]

    # Menampilkan hasil prediksi
    if prediction == 0:
        st.success("Prediksi: Tanah Kurang Subur")
    elif prediction == 1:
        st.success("Prediksi: Tanah Subur")
    else:
        st.success("Prediksi: Tanah Sangat Subur")
