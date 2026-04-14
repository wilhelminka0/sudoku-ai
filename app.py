import os, requests, sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_PATH = '/tmp/stats_vlasak.db'

def init_db():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, count INTEGER)')
            if not conn.execute('SELECT count FROM logs WHERE id = 1').fetchone():
                conn.execute('INSERT INTO logs (id, count) VALUES (1, 0)')
            conn.commit()
    except: pass

init_db()

@app.route('/')
def index():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            res = conn.execute('SELECT count FROM logs WHERE id = 1').fetchone()
            pocet = res[0] if res else 0
    except: pocet = 0
    return render_template('index.html', dotazy=pocet)

@app.route('/ask', methods=['POST'])
def ask_ai():
    # 1. Zápis do statistik
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('UPDATE logs SET count = count + 1 WHERE id = 1')
            conn.commit()
    except: pass

    # 2. Příprava dat pro AI
    data = request.json
    board_data = data.get('board') or data.get('grid') or "neznámé"
    
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv('OPENAI_BASE_URL')
    
    payload = {
        "model": "gemma3:27b",
        "messages": [
            {"role": "system", "content": "Jsi expert na Sudoku. Odpovídej velmi krátce česky."},
            {"role": "user", "content": f"Stav Sudoku: {board_data}. Dej mi jednu konkrétní radu."}
        ]
    }
    
    # 3. Volání AI
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        url = f"{base_url}/chat/completions"
        
        r = requests.post(url, headers=headers, json=payload, timeout=25)
        return jsonify(r.json())
            
    except Exception as e:
        return jsonify({"error": "AI je dočasně nedostupná."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
