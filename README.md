# sudoku-ai
# Sudoku AI Assistant

Tento projekt je webová aplikace pro hraní Sudoku, která obsahuje inteligentního pomocníka využívajícího lokální LLM model.

### Co projekt dělá
Aplikace umožňuje uživateli hrát Sudoku přímo v prohlížeči. Hlavní funkcí je tlačítko "AI Poradit", které odešle aktuální stav mřížky lokálnímu modelu AI, jenž uživateli česky poradí s dalším postupem.

### K čemu je určený
Projekt slouží jako ukázka integrace webové aplikace (Flask), kontejnerizace (Docker) a lokálního běhu umělé inteligence (Ollama). Je připraven jako podklad k maturitní zkoušce.

### Použité technologie
* **Backend:** Python 3 (Flask framework)
* **Frontend:** HTML5, CSS3, JavaScript
* **AI:** Ollama API (Model: gemma2:27b)
* **Kontejnerizace:** Docker
* **Verzování:** Git / GitHub

### Jak se spouští (Návod)
Projekt je plně kontejnerizován, takže stačí mít nainstalovaný Docker a běžící službu Ollama.

1. **Sestavení obrazu:**
   `docker build -t sudoku-web .`
2. **Spuštění kontejneru:**
   `docker run -d --network="host" --name sudoku-kontejner sudoku-web`
3. **Přístup k aplikaci:**
   Otevřete prohlížeč na adrese `http://localhost:5000` (nebo IP adresa serveru).

*Poznámka: Aplikace předpokládá, že na hostitelském stroji běží Ollama s modelem gemma2:27b na portu 11434.*
