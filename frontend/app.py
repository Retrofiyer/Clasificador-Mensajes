import streamlit as st
import requests

st.set_page_config(page_title="Clasificador de Mensajes IA", page_icon="💬")

st.title("💬 Clasificador de Mensajes")
st.markdown("Clasifica un mensaje como 🛑**Urgente**, ✅**Normal** o 🟠**Moderado** usando IA.")

mensaje = st.text_area("Escribe tu mensaje aquí:")

if st.button("🔍 Clasificar mensaje"):
    if mensaje.strip():
        try:
            response = requests.post(
                "http://127.0.0.1:8000/clasificar",
                json={"text": mensaje}
            )
            if response.status_code == 200:
                categoria = response.json()["categoria"]
                st.success(f"🧠 Clasificación: **{categoria}**")
            else:
                st.error("❌ Error del servidor. Intenta más tarde.")
        except Exception as e:
            st.error(f"❌ Error de conexión: {e}")
    else:
        st.warning("⚠️ Por favor, escribe un mensaje para clasificar.")