import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

st.subheader("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('Interfaces Mult2.png')

st.image(image, caption='Sunrise by the mountains')
