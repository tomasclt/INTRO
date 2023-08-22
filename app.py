import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

st.subheader("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Interfaces Mult2.png')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.write("Primera Columna")
    agree = st.checkbox('I agree')
    if agree:
       st.write('Great!')
   # st.radio(
   #     "Set text input label visibility 👉",
   #     key="visibility",
   #     options=["visible", "hidden", "collapsed"],
   # )
   # st.text_input(
   #     "Placeholder for the other text input widget",
   #     "This is a placeholder",
    #    key="placeholder",
    #)

with col2:
    st.write("Esta es la segunda columna")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiva':
       st.write('La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
       st.write('La audición es fundamental para tu interfaz')
