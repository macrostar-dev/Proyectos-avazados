import requests
from datetime import datetime

# 🔹 Pega aquí tu token (personal o de bot)
WEBEX_TOKEN = ""

# 🔹 Pega aquí el roomId del chat donde quieres enviar el mensaje
WEBEX_ROOM_ID = ""

def enviar_mensaje():
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_TOKEN}",
        "Content-Type": "application/json"
    }

    mensaje = (
        "El correo del reportede Uadmin se a enviado exitosamente.👓\n"
        f"⏱️ Hora de envio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    data = {
        "roomId": WEBEX_ROOM_ID,
        "text": mensaje
    }

    resp = requests.post(url, headers=headers, json=data)

    if resp.status_code == 200:
        print("✅ Mensaje enviado correctamente.")
    else:
        print("❌ Error al enviar mensaje:")
        print(resp.status_code, resp.text)

