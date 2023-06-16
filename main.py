import pickle 
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('breast_cancer.sav', 'rb'))

# judul web
st.title('Prediksi Pengidap Penyakit Kanker Payudara')
st.text('Aryo Hardirega - 201351025 - Malam A')

mean_radius = st.number_input('Radiu')

mean_texture = st.number_input('Texture')

mean_perimeter = st.number_input('Perimeter')

mean_area = st.number_input('Area')

mean_smoothness = st.number_input('Smoothness')

# code for prediction
Penumpang = ''

if st.button ('Diagnosis') :
    Penumpang = model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness]])
    
    if (Penumpang[0]==0):
        Penumpang = 'Pasien bukan pengidap penyakit kanker payudara'
    else:
        Penumpang = 'Pasien adalah pengidap penyakit kanker payudara'
        
st.success(Penumpang)