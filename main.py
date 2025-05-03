from fastapi import FastAPI
import requests

app = FastAPI()

@app.get()
def root()
    return {status Jade Atlas backend ativo}

@app.post(notify)
def send_notification(message str = Sistema Jade Atlas ativado. Comunicação operacional.)
    telegram_token = 6521799621AAEfqE6Tn1z4hHRfDAzPQaRz4Swih9D0wms
    chat_id = 5913942179
    telegram_url = fhttpsapi.telegram.orgbot{telegram_token}sendMessage

    payload = {chat_id chat_id, text message}
    response = requests.post(telegram_url, json=payload)
    return {
        status mensagem enviada,
        telegram_response response.json()
    }
