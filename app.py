import streamlit as st
import pickle as pkl
import pandas as pd

movies_dict = pkl.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Sistem Rekomendasi Film')

option = st.selectbox(
    'Pilih Film',
        movies['title'].values)