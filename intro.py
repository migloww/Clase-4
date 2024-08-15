import streamlit as st


st.title("PEDRO SE QUEDO DORMIDO")
st.header("pedro tenia que venir a clase pero probablemente se quedo dormido producto del cansancio que supone el inicio de semestre")
from PIL import image
image = Image.open("images.jpg")
st.image(image, caption="lil yachty")

