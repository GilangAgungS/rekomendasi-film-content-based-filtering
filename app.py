import streamlit as st
import pickle as pkl
import pandas as pd
import requests

def ambil_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1ae0cb88a38abf696469f4d6625ebd71&language=en-US'.format(movie_id))

    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def fungsi_rekomendasi(movie):
    movie_index = movies_list[movies_list['title']==movie].index[0]
    distances = similarity_rekomen[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    list_rekomendasi = []
    poster_rekomendasi = []
    for i in movie_list:
        movie_id = movies_list.iloc[i[0]].movie_id
        list_rekomendasi.append(movies_list.iloc[i[0]].title)
        
        #ambil poster dari API
        poster_rekomendasi.append(ambil_poster(movie_id))

    return list_rekomendasi, poster_rekomendasi



#membukat list film yang disimpan dalam bentuk pickle
movies_list = pkl.load(open('movies.pkl', 'rb'))

#membuka model similarity matrix
similarity_rekomen = pkl.load(open('similarity_rekomen.pkl', 'rb'))

st.title('Sistem Rekomendasi Film')

#search box
pilih_film = st.selectbox(
    'Pilih Film',
        movies_list['title'].values) 

#tombol rekomendasi
if st.button('Rekomendasi'):
    judul, poster = fungsi_rekomendasi(pilih_film)

    col0, col1, col2, col3, col4 = st.columns(5)

    with col0:
        
        st.image(poster[0])
        st.header(judul[0])

    with col1:
        
        st.image(poster[1])
        st.header(judul[1])

    with col2:
        
        st.image(poster[2])
        st.header(judul[2])

    with col3:
        
        st.image(poster[3])
        st.header(judul[3])

    with col4:
        
        st.image(poster[4])
        st.header(judul[4])
