import json
from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

# Ініціалізація списку повідомлень
messages = []

# Завантаження старих повідомлень з файлу
def load_messages():
    global messages
    try:
        with open('messages.json', 'r') as f:
            messages = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        messages = []

# Збереження повідомлень у файл
def save_messages():
    with open('messages.json', 'w') as f:
        json.dump(messages, f)

@app.route('/')
def index():
    return "Чат працює!"

@socketio.on('message')
def handleMessage(msg):
    print(f"Повідомлення: {msg}")
    messages.append(msg)  # Додаємо повідомлення до списку
    save_messages()       # Зберігаємо в файл
    send(msg, broadcast=True)  # Надсилає повідомлення всім підключеним клієнтам

@socketio.on('get_messages')
def handle_get_messages():
    # Відправляємо старі повідомлення новому клієнту
    send(messages, broadcast=False)  # Надсилає старі повідомлення лише новому клієнту

if __name__ == '__main__':
    load_messages()  # Завантажуємо старі повідомлення при запуску сервера
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
