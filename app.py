import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_data = request.json.get('question')
    
    # Tyto údaje si server iThope doplní sám z políček na webu
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    
    # Formát zprávy pro moderní servery (OpenAI standard)
    payload = {
        "model": "gemma3:27b",
        "messages": [
            {"role": "system", "content": "Jsi expert na Sudoku. Odpovídej krátce česky."},
            {"role": "user", "content": user_data}
        ],
        "stream": False
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Voláme server kurim.ithope.eu
        response = requests.post(f"{base_url}/chat/completions", json=payload, headers=headers)
        result = response.json()
        
        # Vytáhneme text odpovědi z balíčku
        ai_message = result['choices'][0]['message']['content']
        return jsonify({"response": ai_message})
    except Exception as e:
        return jsonify({"response": f"Chyba AI: {str(e)}"})

if __name__ == '__main__':
    # Port 5000, přesně jak jsi chtěl!
    app.run(host='0.0.0.0', port=5000)
