from flask import Flask, request, jsonify
import json
import os
from flask_cors import CORS
from config import config

app = Flask(__name__)
CORS(app)

if not os.path.exists(config['file_data']):
    with open(config['file_data'], "w") as file:
        json.dump([], file)

@app.route('/masg', methods=['POST'])
def save_message():
    user = request.form.get('user')
    masg = request.form.get('masg')

    if not user or not masg:
        return jsonify({"error": "Missing user or masg parameter"}), 400

    with open(config['file_data'], 'r') as file:
        messages = json.load(file)

    messages.append([user, masg])

    with open(config['file_data'], 'w') as file:
        json.dump(messages, file, indent=4)

    return jsonify({"success": True, "message": "Message saved successfully"}), 201

@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        with open(config['file_data'], 'r') as file:
            messages = json.load(file)
        return jsonify(messages), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
