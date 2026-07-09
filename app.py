import streamlit as st
st.set_page_config(page_title="Mi Rincon de Practicas", page_icon="💗", layout="centered")
st.title("🌺 Bienvenido a mi espacio de pruebas")
st.write("Aqui voy a practicar programacion y crear cosas que me gustan")

# --- AQUI CREAMOS LAS PESTAÑAS---
pestaña1, pestaña2 = st.tabs(["✨ Mis Gustos". "🧠 Personalidades"])
                              with pestaña 1:
st.subheader("¿Que serie o grupo descubriremos hoy?")
option = st.selectbox(
  "Elige una opcion para ver un mensaje especial:",
  ["Selecciona uno...", "K-dramas Romanticos", "Tiktok", "Flores favoritas"]
)
if option == "K-dramas Romanticos":
  st.success("¡Una excelente eleccion! Nada como una buena historia de amor.")
      st. balloons() #¡Esto lanza globos por toda la pantalla!🎈
elif option == "Tiktok":
  st.info("Si te distrae perfecto, pero no mucho tiempo plis Diana, sabe que tiene que estudiar")
elif option == "Flores favoritas":
  st.warning("Las flores como las peonías son las mejores ¡No te rindas!") # st. warning sale en color amarillo/naranja lindo

      with pestaña2:
st.subheader("El rincon de las personalidades")
st.write("Te apasiona el MBTI o el Eneagrama? ¡Pronto hare un test interactivo aqui!")
