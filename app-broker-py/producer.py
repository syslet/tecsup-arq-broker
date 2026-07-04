import sys
from flask import Flask, render_template, request
import socketio

app = Flask(__name__)

# Cliente Socket.IO para conectarse al broker
sio = socketio.Client()
BROKER_URL = "http://localhost:5000"
sio.connect(BROKER_URL)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tweet = request.form['tweet']
        # Enviar al broker
        sio.emit('publish', {'topic': 'tweets', 'message': tweet})
        return render_template('producer.html', enviado=True, tweet=tweet)
    return render_template('producer.html', enviado=False)

if __name__ == '__main__':
    # Leer argumento de puerto desde línea de comandos
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("⚠️ El argumento debe ser un número. Usando puerto por defecto 5001.")
            port = 5001
    else:
        port = 5001

    print(f"🚀 Productor iniciado en http://localhost:{port}")
    app.run(port=port)
