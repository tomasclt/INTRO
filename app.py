# -*- coding: utf-8 -*-
import streamlit as st
from PIL import Image

# ------------------------------
# Config
# ------------------------------
st.set_page_config(page_title="Mi Primera App", page_icon="✨", layout="centered")

# ------------------------------
# Tema oscuro + estilos (solo CSS)
# ------------------------------
st.markdown("""
<style>
:root{
  --radius: 16px;
  --bg: #0b1220;
  --panel: rgba(17,25,40,.75);
  --panel-border: rgba(255,255,255,.08);
  --text: #e5e7eb;
  --muted: #9ca3af;
  --primaryA: #22d3ee; /* cyan */
  --primaryB: #6366f1; /* indigo */
  --success: #10b981;
  --danger: #ef4444;
}

/* Fondo gradiente oscuro */
html, body, [class*="css"] {
  background:
    radial-gradient(1200px 700px at 10% 0%, rgba(34,211,238,.07), transparent 60%),
    radial-gradient(900px 600px at 90% 10%, rgba(99,102,241,.08), transparent 60%),
    linear-gradient(180deg, #0b1220 0%, #0b1220 100%) !important;
  color: var(--text) !important;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
main .block-container{ max-width: 980px; padding-top: 2rem; padding-bottom: 3rem; }

/* Tarjetas (glass) */
.card{
  background: var(--panel);
  border: 1px solid var(--panel-border);
  border-radius: var(--radius);
  box-shadow: 0 20px 60px rgba(2,6,23,.25);
  padding: 18px 20px;
}

/* Títulos */
h1, h2, h3 { letter-spacing: -.02em; color: #f3f4f6; }
small, .small, .caption { color: var(--muted) !important; }

/* Imagen */
div[data-testid="stImage"] img{
  border-radius: 14px !important;
  box-shadow: 0 24px 70px rgba(0,0,0,.45);
}

/* Inputs */
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div{
  background: rgba(255,255,255,.04) !important;
  border: 1px solid rgba(255,255,255,.08) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
}
.stTextArea textarea::placeholder,
.stTextInput input::placeholder{ color: #94a3b8 !important; }

/* Radio / Checkbox labels */
label, .stRadio, .stCheckbox{ color: var(--text) !important; }

/* Botones pill con gradiente y variantes */
.stButton > button{
  border-radius: 999px;
  padding: .7rem 1.1rem;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.06);
  color: var(--text);
  transition: all .2s ease;
  box-shadow: 0 10px 26px rgba(0,0,0,.25);
}
.stButton > button:hover{ transform: translateY(-1px); }

/* Primario (gradiente) */
.btn-primary > button{
  background: linear-gradient(90deg, var(--primaryA), var(--primaryB)) !important;
  color: white !important;
  border: 0 !important;
  box-shadow: 0 14px 40px rgba(99,102,241,.35);
}

/* Éxito / Peligro (por si los quieres) */
.btn-success > button{ background: linear-gradient(90deg,#34d399,#10b981) !important; color:#052e2b !important; border:0 !important; }
.btn-danger  > button{ background: linear-gradient(90deg,#fb7185,#ef4444) !important; color:white !important; border:0 !important; }

/* Separador suave */
.soft-divider{ height:1px; margin: 1rem 0 1.25rem 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.08), transparent); border:0; }

/* Sidebar oscuro */
section[data-testid="stSidebar"] > div:first-child{
  background: linear-gradient(180deg, rgba(34,211,238,.12), rgba(99,102,241,.12));
  border-right: 1px solid rgba(255,255,255,.08);
}
section[data-testid="stSidebar"] *{ color: var(--text) !important; }

/* Ajustes menores */
.stAlert{ background: rgba(255,255,255,.06) !important; border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)

# ------------------------------
# App (misma lógica, nuevo look)
# ------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("Mi Primera App ✨")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Fácilmente puedo realizar backend y frontend.")

# Imagen (con manejo si no existe)
try:
    image = Image.open('Interfaces Mult2.png')
    st.image(image, caption='Interfaces multimodales', use_container_width=False)
except Exception:
    st.caption("💡 Coloca un archivo **Interfaces Mult2.png** en el directorio para mostrar la imagen.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

# Entrada de texto
st.markdown('<div class="card">', unsafe_allow_html=True)
texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', f"**{texto}**")
st.markdown('</div>', unsafe_allow_html=True)

# Dos columnas
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2, vertical_alignment="top")

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario.")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
        st.success('✅ ¡Correcto!')

with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("¿Qué modalidad es la principal en tu interfaz?",
                    ('Visual', 'Auditiva', 'Táctil'))
    if modo == 'Visual':
        st.info('👁️ La vista es fundamental para tu interfaz.')
    elif modo == 'Auditiva':
        st.info('🎧 La audición es fundamental para tu interfaz.')
    elif modo == 'Táctil':
        st.info('🤚 El tacto es fundamental para tu interfaz.')
st.markdown('</div>', unsafe_allow_html=True)

# Botón con estilo primario
st.markdown('<div class="card">', unsafe_allow_html=True)
st
