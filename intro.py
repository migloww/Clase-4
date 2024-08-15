import streamlit as st
from PIL import Image

st.title("PEDRO SE QUEDO DORMIDO")
st.header("pedro tenia que venir a clase pero probablemente se quedo dormido producto del cansancio que supone el inicio de semestre")

image = Image.open("images.jpg")
st.image(image, caption="lil yachty")

texto = st.text_input("hecho", "Podemos decir que hay muchas similitudes entre pedro y lil yatchy")
st.write("podriamos enumerarlas pero nunca terminariamos",texto)

st.subheader("ahora usaremos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("esta es la primera columna")
  st.write("Pedro se parece a este sujeto?")
  resp = st.checkbox("estoy de acuerdo")
  if resp:
    st.write("correcto!")

with col2:
  st.subheader("esta es la segunda columna")
  modo = st.radio("cuales son las similitudes?",("la ropa", "esta dormido","ninguna"))
  if modo == "la ropa":
    st.write("probablemente no")
  if modo == "esta dormido":
    st.write("¡correcto!")
  if modo == "ninguna":
    st.write("pero si son iguales")

