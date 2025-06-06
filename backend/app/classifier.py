import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# Configura Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Plantilla de prompt
prompt = PromptTemplate(
    input_variables=["mensaje"],
    template="Clasifica el siguiente mensaje como 'Urgente', 'Normal' o 'Moderado'. \n\nMensaje: {mensaje}, Responde de esta manera: '🛑 Urgente', '✅ Normal' o '🟠 Moderado' y el tipo de atención que necesita(ejemplo: 'inmediata') dependiendo de la categoria"
)

# Cadena LangChain
chain = LLMChain(llm=llm, prompt=prompt)

def classify_message(texto: str) -> str:
    result = chain.invoke({"mensaje": texto})
    return result["text"].strip()