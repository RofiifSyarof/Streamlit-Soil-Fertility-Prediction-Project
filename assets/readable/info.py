import streamlit as st

def kurang_subur():
    st.write('---')
    st.markdown(
        '''
        <h2 style="text-align: center;">Tanah Kurang Subur</h2>
        ''', unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.write('')
    with col2:
        st.write('Dari hasil prediksi menunjukkan bawah data tanah yang Anda berikan merupakan tanah yag kurang subur.')
        st.write('Tanah yang kurang subur tidak cocok untuk kegiatan pertanian.')
    with col3:
        st.write('')
    
    st.write('\n')
    st.write('\n')
    
    st.markdown(
        '''
        <h3 style="text-align: center;">Rekomendasi yang dapat diberikan</h5>
        ''', unsafe_allow_html=True
    )
    
    col1, col2= st.columns([1, 1], vertical_alignment='center')
    with col1:
        st.image('./assets/Images/Farmer.jpg')
    with col2:
        st.markdown('#### Petani:')
        st.write('Bagi petani yang tetap ingin melakukan pertanian di tanah kurang subur, disarankan untuk melakukan beberapa hal berikut:')
        st.write('1. Melakukan penambahan pupuk organik,')
        st.write('2. Menambahkan pupuk anorganik,')
        st.write('3. Melakukan rotasi tanaman,')
        st.write('4. Menjaga kebersihan lahan, dan')
        st.write('5. Menjaga kelembaban tanah.')
        
    col1, col2= st.columns([1, 1], vertical_alignment='center')
    with col1:
        st.markdown('#### Pengusaha:')
        st.write('Bagi pengusaha yang ingin mengembangkan bisnisnya, maka lahan dengan tanah yang kurang subur ini dapat dijadikan sebagai lahan untuk kegiatan non-pertanian seperti:')
        st.write('1. Pembangunan perumahan,')
        st.write('2. Pembangunan industri,')
        st.write('3. Pembangunan sarana umum,')
        st.write('4. Pembangunan tempat wisata, dan')
        st.write('5. Pembangunan tempat komersil.')    
    with col2:
        st.image('./assets/Images/BussinesMan.jpg')    
    
def subur():
    st.write('---')
    st.markdown(
        '''
        <h2 style="text-align: center;">Tanah Subur</h2>
        ''', unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write('')
    with col2:
        st.write('Dari hasil prediksi menunjukkan bawah data tanah yang Anda berikan merupakan tanah yang subur.')
        st.write('Tanah yang subur cocok bagi petani untuk melakukan kegiatan pertanian. Tanah yang subur cocok bagi petani untuk melakukan kegiatan pertanian. Perlu diperhatikan saja jenis tanaman yang akan ditanam agar sesuai dengan kondisi tanah. Umumnya tanaman yang cocok ditanam di tanah subur adalah tanaman pangan, seperti:')
    with col3:
        st.write('')
        
    st.write('\n')
    
    col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment='center')
    with col1:
        st.image('./assets/Images/RicePlant.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Padi</p>
            ''', unsafe_allow_html=True
        )
    with col2:
        st.image('./assets/Images/CornPlant.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Jagung</p>
            ''', unsafe_allow_html=True
        )
    with col3:
        st.image('./assets/Images/SoyBean.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Kedelai</p>
            ''', unsafe_allow_html=True
        )
        
    col1, col2, col3 , col4= st.columns([1, 1, 1, 1], vertical_alignment='center')
    with col1:
        st.write('')
    with col2:
        st.image('./assets/Images/Nuts.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Kacang-kacangan</p>
            ''', unsafe_allow_html=True
        )
    with col3:
        st.image('./assets/Images/Vegetables.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Sayuran</p>
            ''', unsafe_allow_html=True
        )
    with col4:
        st.write('')
        
    st.markdown(
        '''
        <h3 style="text-align: center;">Kondisi kesuburan tanah pada tingkat ini memang belum terlalu cocok untuk tanaman yang membutuhkan waktu tumbuh yang lama, atau sekitar 5 tahun.</h5>
        ''', unsafe_allow_html=True
    )
    
def sangat_subur():
    st.write('---')
    st.markdown(
        '''
        <h2 style="text-align: center;">Tanah Sangat Subur</h2>
        ''', unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write('')
    with col2:
        st.write('Dari hasil prediksi menunjukkan bawah data tanah yang Anda berikan merupakan tanah yang sangat subur.')
        st.write('Tanah yang sangat subur sangat cocok bagi petani untuk melakukan kegiatan pertanian. Tanah yang sangat subur ini sangat cocok untuk tanaman hortikultura atau tanaman buah-buahan. Contoh tanaman yang cocok ditanam di tanah yang sangat subur adalah:')
    with col3:
        st.write('')
        
    st.write('\n')
    
    col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment='center')
    with col1:
        st.image('./assets/Images/Mango.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Mangga</p>
            ''', unsafe_allow_html=True
        )
    with col2:
        st.image('./assets/Images/Apple.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Apel</p>
            ''', unsafe_allow_html=True
        )
    with col3:
        st.image('./assets/Images/Coconut.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Kelapa</p>
            ''', unsafe_allow_html=True
        )
        
    col1, col2, col3 , col4= st.columns([1, 1, 1, 1], vertical_alignment='center')
    with col1:
        st.write('')
    with col2:
        st.image('./assets/Images/Guava.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Jambu</p>
            ''', unsafe_allow_html=True
        )
    with col3:
        st.image('./assets/Images/Orange.jpg')
        st.markdown(
            '''
            <p style="text-align: center;">Jeruk</p>
            ''', unsafe_allow_html=True
        )
    with col4:
        st.write('')
        
    st.markdown(
        '''
        <h3 style="text-align: center;">Dengan kondisi tanah yang sangat subur, petani dapat memperoleh hasil panen yang optimal.</h5>
        ''', unsafe_allow_html=True
    )

sangat_subur()