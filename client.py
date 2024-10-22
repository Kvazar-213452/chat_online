import socketio
from flask import Flask, render_template

app = Flask(__name__)
sio = socketio.Client()

# Обробка отримання повідомлення
@sio.event
def message(data):
    print(f"Новий меседж: {data}")
    # Додаємо повідомлення в інтерфейс
    messagesDiv = document.getElementById('messages')
    messagesDiv.innerHTML += '<div>' + data + '</div>'
    messagesDiv.scrollTop = messagesDiv.scrollHeight  # Прокрутка донизу

# Обробка підключення
@sio.event
def connect():
    print("Підключено до сервера")
    sio.emit('get_messages')  # Запитуємо старі повідомлення при підключенні

# Обробка отримання старих повідомлень
@sio.event
def old_messages(data):
    for msg in data:
        message(msg)  # Виводимо старі повідомлення

# Обробка відключення
@sio.event
def disconnect():
    print("З'єднання закрите")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # Підключаємося до сервера
    sio.connect('http://localhost:5000')
    app.run(host='0.0.0.0', port=5001)
