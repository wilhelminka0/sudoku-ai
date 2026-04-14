import os, requests, psycopg2
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'tajny_klic_alesko' # Potřebujeme pro pamatování přihlášení

# --- DATABÁZE (To, co chce učitel v zadání) ---
def get_db():
    # Připojí se k databázi 'db', kterou máš v compose.yml
    return psycopg2.connect(os.getenv("DATABASE_URL"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user, pwd = request.form['username'], generate_password_hash(request.form['password'])
        conn = get_db(); cur = conn.cursor()
        cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (user, pwd))
        conn.commit(); cur.close(); conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user, pwd = request.form['username'], request.form['password']
        conn = get_db(); cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s', (user,))
        u = cur.fetchone(); cur.close(); conn.close()
        if u and check_password_hash(u[2], pwd):
            session['user'] = user
            return redirect(url_for('index'))
    return render_template('login.html')

# --- TVOJE PŮVODNÍ FUNKCE (Jen s kontrolou přihlášení) ---

@app.route('/')
def index():
    # Pokud uživatel není v 'session' (není přihlášen), pošli ho na login
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    if 'user' not in session: return jsonify({"response": "Nepřihlášen!"})
    
    user_data = request.json.get('question')
    # Tyto údaje si server iThope doplní sám z políček na webu
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    # Formát zprávy pro AI (OpenAI standard)
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
        ai_message = response.json()['choices'][0]['message']['content']
        return jsonify({"response": ai_message})
    except Exception as e:
        return jsonify({"response": f"Chyba AI: {str(e)}"})

if __name__ == '__main__':
    # Nejdřív vytvoříme tabulku v DB, pokud neexistuje
    try:
        c = get_db(); cur = c.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, username varchar UNIQUE, password varchar);')
        c.commit(); cur.close(); c.close()
    except: print("DB ještě neběží")
    
    app.run(host='0.0.0.0', port=5000)
