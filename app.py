import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

st.subheader("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Interfaces Mult2.png')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
