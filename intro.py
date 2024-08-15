import streamlit as st
from PIL import Image

st.title("PEDRO SE QUEDO DORMIDO")
st.header("pedro tenia que venir a clase pero probablemente se quedo dormido producto del cansancio que supone el inicio de semestre")

image = Image.open("images.jpg")
st.image(image, caption="lil yachty")

texto = st.text_input("hecho", "Podemos decir que hay muchas similitudes entre pedro y lil yatchy")
st.write("podriamos enumerarlas pero nunca terminariamos",texto)
