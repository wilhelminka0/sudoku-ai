Sudoku AI Assistant
Tento projekt je webová aplikace pro hraní Sudoku, která obsahuje inteligentního pomocníka využívajícího LLM model (Gemma) pro nápovědu v reálném čase.

Co projekt dělá
Aplikace umožňuje uživateli generovat a hrát Sudoku různé obtížnosti přímo v prohlížeči. Hlavní funkcí je tlačítko "AI Poradit s polem". Po kliknutí aplikace odešle aktuální stav mřížky a souřadnice vybraného pole na server, kde se dotáže umělé inteligence, která uživateli česky poradí optimální další krok.

Klíčové vlastnosti
Dynamické generování her: Možnost volby mezi lehkou, střední a těžkou obtížností.

AI Integrace: Propojení s modelem gemma3:27b přes API pro generování logických rad.

Sledování statistik: Aplikace ukládá celkový počet dotazů na AI do databáze, která je odolná vůči restartům serveru.

Kontejnerizace: Plně připraveno pro běh v Dockeru pomocí Docker Compose.

Použité technologie
Backend: Python 3 (Framework Flask)

Frontend: HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6)

Databáze: SQLite 3 (využití perzistentního úložiště ve složce /data)

AI: Ollama API / OpenAI kompatibilní rozhraní (Model: gemma3:27b)

Kontejnerizace: Docker & Docker Compose (definice více služeb)

Verzování: Git / GitHub

Jak se spouští (Návod)
Projekt je navržen pro běh na platformě iThope, ale lze jej spustit i lokálně:

Sestavení a spuštění pomocí Compose:

Bash
docker compose up -d --build
Přístup k aplikaci: Otevřete prohlížeč na adrese http://localhost:5000 (nebo na přidělené iThope URL).

Architektura projektu
Projekt splňuje požadavky na moderní webovou aplikaci:

Soubor compose.yml: Definuje dvě služby (aplikaci a databázový uzel).

Perzistence dat: Databázový soubor je uložen v adresáři /data, což zaručuje, že se statistiky dotazů nesmažou při redeployi aplikace.

Separace logiky: Frontend komunikuje s backendem asynchronně pomocí fetch API (JSON).
