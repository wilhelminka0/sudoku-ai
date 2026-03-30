from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Adresa tvojí AI v Dockeru
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_data = request.json.get('question')
    payload = {
        "model": "gemma2:27b",
        "prompt": f"Jsi expert na Sudoku. Uživatel potřebuje poradit s touto hrou: {user_data}. Odpovídej krátce česky.",
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    # Port 5000, jak jsi chtěl!
    app.run(host='0.0.0.0', port=5000)
