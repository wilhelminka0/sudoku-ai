# 🧩 Sudoku AI Assistant

Tento projekt je moderní webová aplikace pro hraní Sudoku, která integruje **umělou inteligenci** pro poskytování rad v reálném čase. Aplikace je navržena pro snadné nasazení pomocí **Dockeru** a využívá perzistentní databázi pro sledování statistik.

---

## 🚀 Co projekt dělá?

Aplikace umožňuje uživatelům generovat a řešit Sudoku různé obtížnosti. Hlavním lákadlem je **AI nápověda**:
* Po kliknutí na tlačítko **"AI Poradit s polem"** odešle aplikace aktuální stav mřížky serveru.
* Server komunikuje s LLM modelem, který analyzuje situaci a vrátí konkrétní logickou radu v češtině.

---

## ✨ Klíčové vlastnosti

* **Dynamická obtížnost:** Volba mezi lehkou, střední a těžkou hrou.
* **Inteligentní rádce:** Integrace s modelem `gemma3:27b` přes API.
* **Perzistentní statistiky:** Počítadlo rad se ukládá do databáze, která přežije restart serveru.
* **Plná kontejnerizace:** Snadné spuštění kdekoli díky Docker Compose.

---

## 🛠 Použité technologie

| Část | Technologie |
| :--- | :--- |
| **Backend** | Python 3 (Flask Framework) |
| **Frontend** | HTML5, CSS3, JavaScript (ES6) |
| **Databáze** | SQLite 3 (Ukládání v `/data`) |
| **Kontejnerizace** | Docker & Docker Compose |
| **AI Model** | Gemma 3 (přes OpenAI API rozhraní) |

---

## 📂 Architektura a Perzistence

Projekt je postaven tak, aby splňoval náročné požadavky na moderní vývoj:
* **Docker Compose:** Soubor `compose.yml` definuje dvě služby — **aplikaci** a **databázový uzel**.
* **Složka `/data`:** Veškerá uživatelská data (SQLite databáze `vlasak.db`) jsou ukládána do tohoto adresáře. To zaručuje, že o své statistiky nepřijdete ani při aktualizaci aplikace.

---

## 🚦 Jak se spouští (Návod)

1. **Spuštění pomocí Docker Compose:**
   ```bash
   docker compose up -d --build
