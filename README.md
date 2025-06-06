<div>
    <h1>🧠 Clasificación Automatizada de Mensajes</h1>
</div>

## Acerca del Proyecto

Este proyecto implementa un sistema inteligente que clasifica automáticamente mensajes de texto en tres categorías: **Urgente 🔥**, **Moderado ⏳** o **Normal ✅**, utilizando el modelo de lenguaje de Google Gemini a través de LangChain. La API se expone con FastAPI y la visualización se realiza mediante Streamlit, brindando una experiencia simple e interactiva.

## 🗂️ Tabla de Contenidos

<ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del Proyecto</a>
      <ul>
        <li><a href="#resumen">Resumen</a></li>
        <li><a href="#características">Características</a></li>
        <li><a href="#tecnologías-utilizadas">Tecnologías Utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#primeros-pasos">Primeros Pasos</a>
      <ul>
        <li><a href="#requisitos-previos">Requisitos Previos</a></li>
        <li><a href="#instalación">Instalación</a></li>
        <li><a href="#configuración">Configuración</a></li>
        <li><a href="#ejecutar-el-servicio">Ejecutar el Servicio</a></li>
        <li><a href="#evidencia">Evidencia</a></li>
      </ul>
    </li>
    <li>
      <a href="#contribuciones">Contribuciones</a>
    </li>
 </ol>

---

## Resumen

El sistema consta de dos partes:

- 🔧 **Backend**: API REST construida con FastAPI, que se conecta con LangChain y utiliza el modelo Gemini para realizar la clasificación inteligente de mensajes.
- 🖥️ **Frontend**: Interfaz gráfica desarrollada con Streamlit para ingresar mensajes y visualizar el resultado de la clasificación.

Las categorías asignadas son:
- **🔥 Urgente**: Atención inmediata.
- **⏳ Moderado**: Importante, pero no urgente.
- **✅ Normal**: Sin urgencia ni prioridad especial.


## Características

<div>
  <ul>
      <li>✅ <b>Clasificación automática de texto:</b> IA basada en Gemini y LangChain.</li>
      <li>🧠 <b>Zero-shot reasoning:</b> No requiere entrenamiento previo.</li>
      <li>📡 <b>API REST con FastAPI:</b> Exposición clara y escalable.</li>
      <li>🖼️ <b>Interfaz con Streamlit:</b> Simple, rápida y fácil de usar.</li>
  </ul>
</div>


## Tecnologías Utilizadas

[![Python][python.com]][python-url]


## Primeros Pasos

### Requisitos Previos

- **Python 3.9 o superior** → [Descargar Python](https://www.python.org/downloads/)
- Tener una clave de API para Google Gemini → [Google AI Studio](https://ai.google.dev/)



### Instalación

1. Clona el repositorio:

   ```sh
    git clone https://github.com/Retrofiyer/Clasificador-Mensajes.git
    cd Clasificador-Mensajes
   ```
2. Crea un entorno virtual y activa:

   ```sh
    python -m venv .venv
    .venv\Scripts\activate   # En Linux/macOS: source .venv/bin/activate
   ```

3. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
   ```

## Configuración

1. Crea un archivo .env en la carpeta raíz con este contenido:

     ```sh
    GOOGLE_API_KEY=TU_API_KEY
   ```

## Ejecutar el Servicio

1. Ejecuta el backend desde su carpeta:

    ```sh
    uvicorn main:app --reload
   ```

2. Ejecuta el frontend desde su carpeta:

    ```sh
    streamlit run app.py
   ```

## Evidencia

1. Usando Swagger:
![127 0 0 1_8000_docs](https://github.com/user-attachments/assets/991ce6f8-a20f-449e-9d3f-547948d05b84)

2. Usando Postman:

![image](https://github.com/user-attachments/assets/a99fc085-2b36-4b19-8be2-3ac3e94e8bf0)

3. Usando el Front-End:

![image](https://github.com/user-attachments/assets/65a804e8-8fad-4e96-94f1-8d590ddf11ed)


## Contribuciones

¡Tu ayuda es bienvenida!
Si deseas mejorar este proyecto (corregir errores, agregar características o mejorar la documentación), no dudes en escribirme a: 📬 sebitas5225@gmail.com


[python.com]: https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
