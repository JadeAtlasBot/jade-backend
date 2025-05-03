from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Jade Atlas backend ativo"}

@app.post("/notify")
def send_notification(message: str = "Sistema Jade Atlas ativado. Comunicação operacional."):
    telegram_token = "6746078990:AAE0Fc4-pcmDboC0e_xF4Zq1IvZ-DxlDhaU"
    chat_id = "5070282354"
    telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(telegram_url, json=payload)
    return {"status": "mensagem enviada", "telegram_response": response.json()}