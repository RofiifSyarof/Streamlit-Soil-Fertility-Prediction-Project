# home.py
import streamlit as st

# Set page config to widen the display area
st.set_page_config(page_title="SoilSense", layout="wide")

# Title and description
st.markdown("<h1 style='text-align: center;font-weight: bold'>SoilSense</h1>", unsafe_allow_html=True)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

col1, col2 = st.columns([2, 2], vertical_alignment='center')
with col1:
    st.image("https://www.pngitem.com/pimgs/m/146-1468479_soil-png-transparent-png.png", width=150)
with col2:
    st.markdown("<h2 style='text-align: center;'>Apa itu SoilSense?</h2>", unsafe_allow_html=True)
    st.write(
        """
        SoilSense adalah sebuah aplikasi berbasis AI yang dirancang untuk membantu pengguna memprediksi tingkat kesuburan tanah berdasarkan data nutrisi yang dimasukkan. 
        Dengan menggunakan teknologi Machine Learning, aplikasi ini memberikan hasil prediksi dalam waktu singkat dan akurat yang terbagi menajdi tiga kategori: 
        - **Tanah Kurang Subur**, 
        - **Tanah Subur**, dan 
        - **Tanah Sangat Subur**.
        """
    )
    
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

col1, col2 = st.columns([2, 2], vertical_alignment='center')
with col1:
    st.markdown("<h2 style='text-align: center;'>Mengapa menggunakan SoilSense?</h2>", unsafe_allow_html=True)
    st.write(
        """
        SoilSense menawarkan beberapa fitur menjadi keunggulan, yaitu:
        - **Prediksi Cepat**: SoilSense memberikan hasil prediksi dalam waktu singkat.
        - **Akurat**: SoilSense menggunakan teknologi Machine Learning untuk memberikan hasil prediksi yang akurat.
        - **User-friendly**: SoilSense dirancang dengan antarmuka yang mudah digunakan.
        - **Rekomendasi**: Salah satu fitur tambahan yang mungkin berguna bagi beberapa pengguna dengan memberikan rekomendasi tindakan yang dapat diambil berdasarkan hasil prediksi.
        - **Tidak Memerlukan Registrasi**: SoilSense dapat digunakan tanpa perlu mendaftar terlebih dahulu.
        - **Gratis**: SoilSense dapat digunakan secara gratis.
        """
    )
with col2:
        st.image("https://www.pngitem.com/pimgs/m/146-1468479_soil-png-transparent-png.png", width=150)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

col1, col2 = st.columns([2, 2], vertical_alignment='center')
with col1:
    st.image("https://www.pngitem.com/pimgs/m/146-1468479_soil-png-transparent-png.png", width=150)
with col2:
    st.markdown("<h2 style='text-align: center;'>Bagaimana cara menggunakan SoilSense?</h2>", unsafe_allow_html=True)
    st.write(
        """
        SoilSense dapat digunakan hanya dengan melakukan tiga langkah mudah:
        1. **Masukkan Data Nutrisi**
        2. **Klik Tombol Prediksi**
        3. **Lihat Hasil Prediksi**
        """
    )

st.write('\n')
st.write('\n')
st.write('\n')

# Header
st.markdown("<h2 style='text-align: center;'>Sudah siap menggunakan SoilSense?</h2>", unsafe_allow_html=True)
# Subheader
st.markdown("<h4 style='text-align: center;'>Buka sidebar di kiri layar dan pilih Prediksi.</h4>", unsafe_allow_html=True)
