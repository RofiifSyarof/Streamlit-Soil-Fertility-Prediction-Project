# pages/prediksi.py
import streamlit as st
import pickle
import pandas as pd

from assets.readable import info

# Load the trained model
model_path = 'model/gradient_boosting_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Judul Halaman dan Deskripsi
st.markdown(
    """
    <h1 style='text-align: center;'><b>🌱Prediksi SoilSense<b></h1>
    """,
    unsafe_allow_html=True
)
st.write('---')

st.markdown(
    """
    <h3 style='text-align: center;'>⚠️Instruksi penggunaan⚠️</h3>
    <ol style='text-align: left; margin-left: 30%;'>
        <li>Masukkan data nutrisi tanah pada formulir yang tersedia.</li>
        <li>Klik tombol <b>"Prediksi"</b> untuk memulai prediksi.</li>
        <li>Hasil prediksi akan muncul di bawah berserta dengan rekomendasinya.</li>
    </ol>
    """,
    unsafe_allow_html=True
)

# Input untuk nutrisi tanah
st.subheader("📃Masukkan data nutrisi tanah pada form berikut:")

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

st.write("\n")
st.write("\n")

container = st.container()
container.markdown(
    """
    <style>
    .stButton {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

if container.button("Prediksi"):
    # Definisikan nama kolom yang sesuai dengan pelatihan model
    feature_names = ['N', 'P', 'K', 'pH', 'EC', 'OC', 'S', 'Zn', 'Fe', 'Cu', 'Mn', 'B']
    # Mempersiapkan data input untuk model
    input_data = pd.DataFrame([[N, P, K, ph, ec, oc, S, zn, fe, cu, Mn, B]], columns=feature_names)
    
    # Melakukan prediksi
    prediction = model.predict(input_data)[0]

    # Menampilkan hasil prediksi
    if prediction == 0:
        st.markdown(
            """
            <div style='display: flex; flex-direction: column; align-items: center;'>
                <h5>Hasil prediksi menunjukkan bahwa data tanah Anda</h5>
                <h2 style='
                    text-align: center; 
                    background-color: #ffebee;
                    color: #d32f2f;
                    border: 2px solid #d32f2f;
                    padding: 10px;
                    border-radius: 8px;
                    display: inline-block;
                    margin: 0 auto;
                '>Kurang Subur</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        info.kurang_subur()
    elif prediction == 1:
        st.markdown(
            """
            <div style='display: flex; flex-direction: column; align-items: center;'>
                <h5>Hasil prediksi menunjukkan bahwa data tanah Anda</h5>
                <h2 style='
                    text-align: center; 
                    background-color: #fff9c4;
                    color: #fbc02d;
                    border: 2px solid #fbc02d;
                    padding: 10px;
                    border-radius: 8px;
                    display: inline-block;
                    margin: 0 auto;
                '>Subur</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        info.subur()
    else:
        st.markdown(
            """
            <div style='display: flex; flex-direction: column; align-items: center;'>
                <h5>Hasil prediksi menunjukkan bahwa data tanah Anda</h5>
                <h2 style='
                    text-align: center;
                    background-color: #e8f5e9;
                    color: #2e7d32;
                    border: 2px solid #2e7d32;
                    padding: 10px;
                    border-radius: 8px;
                    display: inline-block;
                    margin: 0 auto;
                '>Sangat Subur</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        info.sangat_subur()
            
# Informasi Tambahan
st.sidebar.title("Tentang Halaman Ini")
st.sidebar.info("""
    - Halaman yang Anda lihat adalah halaman prediksi dari Soilsense.
    
    - Halaman ini memungkinkan pengguna untuk memasukkan nilai nutrisi tanah dan mendapatkan prediksi tingkat kesuburan tanah.
    
    - Rekomendasi tindakan yang dapat diambil berdasarkan hasil prediksi juga disediakan.
    
    - Untuk kembali ke Beranda, klik tombol navigasi yang tersedia di bagian atas sidebar.
""")