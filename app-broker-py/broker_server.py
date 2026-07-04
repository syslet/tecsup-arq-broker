from flask import Flask
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Diccionario para manejar suscripciones: tópico -> lista de clientes
subscriptions = {}

@socketio.on('connect')
def handle_connect():
    print("✅ Cliente conectado")

@socketio.on('disconnect')
def handle_disconnect():
    print("❌ Cliente desconectado")

@socketio.on('subscribe')
def handle_subscribe(data):
    topic = data.get('topic')
    sid = data.get('sid') if 'sid' in data else None
    join_room(topic)
    if topic not in subscriptions:
        subscriptions[topic] = []
    # Usamos el sid que SocketIO maneja internamente
    subscriptions[topic].append(sid)
    print(f"📌 Cliente suscrito al tópico: {topic}")

@socketio.on('publish')
def handle_publish(data):
    topic = data.get('topic')
    message = data.get('message')
    print(f"📨 Mensaje recibido en tópico {topic}: {message}")
    emit('message', {'topic': topic, 'message': message}, room=topic)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
