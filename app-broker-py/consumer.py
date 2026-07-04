import socketio
import uuid
from datetime import datetime

# URL del broker
BROKER_URL = "http://localhost:5000"

# Crear cliente Socket.IO
sio = socketio.Client()

# Generar identificador único (primeros 8 caracteres del UUID)
consumer_id = str(uuid.uuid4())[:8]

@sio.event
def connect():
    print(f"✅ Cliente conectado | ID: {consumer_id}")
    # Suscribirse al tópico "tweets"
    sio.emit('subscribe', {'topic': 'tweets', 'id': consumer_id})

@sio.event
def disconnect():
    print(f"❌ Cliente desconectado | ID: {consumer_id}")

@sio.on('message')
def on_message(data):
    # Obtener timestamp actual
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] 📩 [{consumer_id}] Tweet recibido: {data['message']}")

if __name__ == "__main__":
    try:
        sio.connect(BROKER_URL)
        print("Esperando mensajes... (Ctrl+C para salir)")
        sio.wait()
    except Exception as e:
        print(f"Error de conexión: {e}")
