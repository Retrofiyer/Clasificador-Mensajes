from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.classifier import classify_message

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/clasificar")
def clasificar_mensaje(message: Message):
    try:
        categoria = classify_message(message.text)
        return {"categoria": categoria}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))