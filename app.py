import streamlit as st
st.set_page_config(page_title="Mi Rincon de Practicas", page_icon="💗", layout="centered")
st.title("🌺 Bienvenido a mi espacio de pruebas")
st.write("Aqui voy a practicar programacion y crear cosas que me gustan")

# --- AQUI CREAMOS LAS PESTAÑAS---
pestaña1, pestaña2 = st.tabs(["✨ Mis Gustos", "🧠 Personalidades"])
with pestaña1:
    st.subheader("¿Qué serie o grupo descubriremos hoy?")
    opcion = st.selectbox(
        "Elige una opcion para ver un mensaje especial:",
        ["Selecciona uno...", "K-dramas Romanticos", "Tiktok", "Flores favoritas"]
    )
if opcion == "K-dramas Romanticos":
  st.success("¡Una excelente eleccion! Nada como una buena historia de amor.")
  st.balloons() # ¡Esto lanza globos por toda la pantalla! 🎈
elif opcion == "Tiktok":
        st.info("Si te distrae perfecto, pero no mucho tiempo plis Diana, sabe que tiene que estudiar")
elif opcion == "Flores favoritas":
        st.warning("🪷 Las flores como las peonías, tulipanes y lotos son las mejores. ¡No te rindas! 💪") # st.warning sale en color amarillo/naranja lindo

with pestaña2:
    st.subheader("El rincon de las personalidades")
    st.write("Te apasiona el MBTI o el Eneagrama? ¡Pronto haremos un test interactivo aquí!")

# --- NUEVA PESTAÑA: CATÁLOGO DE K-DRAMAS ---
with pestaña3:
st.subheader("💖 Catálogo de K-Dramas Románticos")
st.write("Selecciona un K-drama para ver una breve sinopsis y un mensaje especial.")

drama_seleccionado = st.selectbox(
    "¿Que historia te gustaria descubrir?",
    ["Selecciona uno...", "Propuesta Laboral", "True beauty", "Mi adorable demonio", "King the land"]
)
if drama_seleccionado = "Propuesta laboral":
        st.success("🏢 **Propuesta Laboral:** Una investigadora de alimentos se hace pasar por su amiga en una cita a ciegas, ¡y resulta ser su jefe! Una comedia romántica súper divertida.")
        st.balloons()
elif drama_seleccionado == "True beauty":
         st.info("😘 **True beauty:** Una adolescente en un nuevo instituto despues de haber recibido bulling por parte de sus demas compañeros".)
elif drama_seleccionado == "Mi adorable demonio":
         st.warning(" **Mi adorable demonio**: Historia donde los protagonistas son obligados a compartir un destino, afortunadamente no se como se enamoraron son tan lindos".)
elif drama_seleccionado == "King the land":
         st.success("🏢 **King the land**: Una chica entra a trabajar como secretaria en un famoso hotel, y de forma vergonsoza y rencorosa conoce a lo que seria su futuro amor":)
