
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open('real.sav', 'rb') as model_file:
    model = pickle.load(model_file)

# Konfigurasi halaman
st.set_page_config(page_title="Prediksi Harga Properti", layout="centered")

# Judul
st.title("Aplikasi Prediksi Harga Properti")
st.write("Masukkan data properti di bawah ini:")

# Input dari pengguna
X1 = st.number_input("Transaksi per meter persegi (X1)", min_value=0.0)
X2 = st.number_input("Usia rumah (X2)", min_value=0.0)
X3 = st.number_input("Jarak ke stasiun MRT terdekat (X3)", min_value=0.0)
X4 = st.number_input("Jumlah toko terdekat dalam 500 meter (X4)", min_value=0)
X5 = st.number_input("Latitude (X5)", format="%.6f")
X6 = st.number_input("Longitude (X6)", format="%.6f")

# Tombol Prediksi
if st.button("Prediksi Harga"):
    input_data = np.array([[X1, X2, X3, X4, X5, X6]])
    prediction = model.predict(input_data)
    st.success(f"Perkiraan Harga Rumah: {prediction[0]:,.2f} (dalam satuan yang sesuai)")

# Footer
st.markdown("---")
st.caption("Model by Rifky Azhar Prayoga – Streamlit Deployment")
