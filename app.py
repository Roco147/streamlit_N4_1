import streamlit as st

st.title("Mi Primera Aplicación con Streamlit")

st.header("Formulario de Registro de Alumno")

nombre = st.text_input("Ingresa tu nombre completo:")

edad = st.number_input("Ingresa tu edad:")

lenguaje = st.selectbox(
    "¿Cuál es tu lenguaje de programación favorito?",
    ["Python", "JavaScript", "C++", "Java", "Otro"]
)

if st.button("Enviar"):
    if nombre:
        st.write(f"¡Bienvenido/a, {nombre}!")
        st.write(f"**Edad:** {edad} años")
        st.write(f"**Lenguaje favorito:** {lenguaje}")
    else:
        st.error("Por favor, ingresa tu nombre antes de continuar.")