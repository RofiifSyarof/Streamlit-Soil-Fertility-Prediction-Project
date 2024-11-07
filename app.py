# home.py
import streamlit as st

# Title and description
st.title("Prediksi Tingkat Kesuburan Tanah")
st.write(
    """
    Selamat datang di aplikasi prediksi tingkat kesuburan tanah! 
    Aplikasi ini dapat membantu menentukan tingkat kesuburan tanah berdasarkan kandungan nutrisi tanah.
    
    **Cara Menggunakan**:
    - Buka halaman prediksi di menu sebelah kiri.
    - Masukkan nilai nutrisi tanah yang ingin Anda periksa.
    - Klik "Prediksi" untuk mengetahui tingkat kesuburan tanah.
    """
)

# Display information about soil fertility levels
st.header("Tentang Tingkat Kesuburan Tanah")
st.write("""
1. **Tidak Subur**: Tanah yang tidak memiliki cukup nutrisi yang dibutuhkan untuk pertumbuhan tanaman.
2. **Kurang Subur**: Tanah yang memiliki nutrisi cukup tetapi belum optimal untuk pertumbuhan tanaman.
3. **Subur**: Tanah dengan kandungan nutrisi optimal untuk mendukung pertumbuhan tanaman yang baik.
""")

# Footer or additional info
st.write("---")
st.write("Dikembangkan untuk membantu dalam penilaian kesuburan tanah secara cepat dan akurat.")
