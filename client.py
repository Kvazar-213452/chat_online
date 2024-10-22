from flask import Flask, render_template
from config import config

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.' + config['use_file'], )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
 