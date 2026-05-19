import streamlit as st

st.title("🎈 percobaanlpk")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
import streamlit as st

# Judul aplikasi
st.title("Kalkulator Sederhana")

# Input angka
angka1 = st.number_input("Masukkan angka pertama")
angka2 = st.number_input("Masukkan angka kedua")

# Pilihan operasi
operasi = st.selectbox(
    "Pilih operasi",
    ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian")
)

# Tombol hitung
if st.button("Hitung"):

    if operasi == "Penjumlahan":
        hasil = angka1 + angka2

    elif operasi == "Pengurangan":
        hasil = angka1
