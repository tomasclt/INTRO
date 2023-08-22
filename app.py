import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

image = Image.open('Interfaces Mult2.png')

st.image(image, caption='Sunrise by the mountains')
