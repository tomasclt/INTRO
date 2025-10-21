# -*- coding: utf-8 -*-
import streamlit as st
from PIL import Image

# ---------- Configuración de página (no cambia la lógica) ----------
st.set_page_config(page_title="Mi Primera App", page_icon="✨", layout="centered")

# ---------- Estilos: Dark theme alto contraste (solo estética) ----------
st.markdown("""
<style>
:root{
  --radius: 16px;
  /* Paleta alto contraste */
  --bgA: #0b1120;   /* fondo base */
  --bgB: #0f172a;   /* fondo gradiente */
  --panel: #111827; /* panel oscuro sólido */
  --panel-border: #1f2937; 
  --text: #f8fafc;  /* texto principal */
  --muted: #cbd5e1; /* texto secundario */
  --input: #0f172a; /* fondo inputs */
  --input-border: #334155;
  --focus: #22d3ee; /* foco accesible */
  --primaryA: #2563eb; /* azul 600 */
  --primaryB: #1d4ed8; /* azul 700 */
}

html, body, [class*="css"] {
  background: linear-gradient(180deg, var(--bgA) 0%, var(--bgB) 100%) !important;
  color: var(--text) !important;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
main .block-container{ max-width: 980px; padding-top: 2rem; padding-bottom: 3rem; }

/* Títulos y textos */
h1, h2, h3 { letter-spacing: -.01em; color: #f9fafb; }
p, label, span, li { color: var(--text); }
.caption, .small, small { color: var(--muted) !important; }

/* Imagen */
div[data-testid="stImage"] img{
  border-radius: 14px !important;
  box-shadow: 0 24px 60px rgba(0,0,0,.55);
}

/* Inputs con alto contraste */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div,
.stRadio > div, .stCheckbox > div {
  background: transparent !important;
  color: var(--text) !important;
}
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div {
  background: var(--input) !important;
  border: 1px solid var(--input-border) !important;
  border-radius: 12px !important;
}
.stTextArea textarea::placeholder,
.stTextInput input::placeholder{
  color: #94a3b8 !important; /* visible pero no compite */
}

/* Estados de foco visibles */
:focus, :focus-visible,
.stTextInput input:focus,
.stTextArea textarea:focus {
  outline: 2px solid var(--focus) !important;
  outline-offset: 2px !important;
  box-shadow: none !important;
}

/* Botones: primario sólido y legible */
.stButton > button{
  border-radius: 999px;
  padding: .72rem 1.15rem;
  border: 1px solid var(--panel-border);
  background: #1f2937; /* neutro sólido */
  color: var(--text);
  transition: transform .15s ease, box-shadow .15s ease, background .15s ease;
  box-shadow: 0 8px 20px rgba(0,0,0,.35);
}
.stButton > button:hover{
  transform: translateY(-1px);
  background: #273244;
}

/* Botón más importante: color primario */
div:has(> button[kind="secondary"]) > button,  /* fallback */
.stButton > button:first-child {
  background: linear-gradient(90deg, var(--primaryA), var(--primaryB)) !important;
  color: #ffffff !important;
  border: 0 !important;
  box-shadow: 0 14px 36px rgba(37,99,235,.45);
}

/* Sidebar oscuro */
section[data-testid="stSidebar"] > div:first-child{
  background: #0c1324;
  border-right: 1px solid var(--panel-border);
}
section[data-testid="stSidebar"] *{ color: var(--text) !important; }

/* Alertas legibles */
.stAlert{
  background: #0f172a !important;
  border: 1px solid #334155 !important;
  color: var(--text) !important;
  border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- TU APP (idéntica en arquitectura y lógica) ----------
st.title(" Mi Primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Interfaces Mult2.png')

st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')
  
with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiva':
       st.write('La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
       st.write('El tacto es fundamental para tu interfaz')
        
st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:" , set_mod)

with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
    # aca haz la aplicacioon en un tema oscuro y pon colores en los botones que resalten de buena manera
