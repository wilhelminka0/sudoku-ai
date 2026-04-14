import os, requests, sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- DATABÁZE (SQLite - ukládá dotazy do souboru stats.db) ---
def log_ai_request():
    with sqlite3.connect('stats.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS logs (count INTEGER)')
        if not conn.execute('SELECT count FROM logs').fetchone():
            conn.execute('INSERT INTO logs VALUES (0)')
        conn.execute('UPDATE logs SET count = count + 1')

def get_ai_count():
    with sqlite3.connect('stats.db') as conn:
        res = conn.execute('SELECT count FROM logs').fetchone()
        return res[0] if res else 0

# --- CESTY (ROUTES) ---
@app.route('/')
def index():
    pocet = get_ai_count()
    return render_template('index.html', dotazy=pocet)

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    log_ai_request() # Tady se to započítá do DB
    
    data = request.json
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    
    payload = {
        "model": "gemma3:27b",
        "messages": [
            {"role": "system", "content": "Jsi expert na Sudoku. Odpovídej krátce česky."},
            {"role": "user", "content": f"Stav Sudoku: {data['board']}. Dej mi jednu radu."}
        ]
    }
    
    response = requests.post(f"{base_url}/chat/completions", 
                             headers={"Authorization": f"Bearer {api_key}"}, 
                             json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
