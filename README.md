# Telegram AI Bot (ready-to-run)

This project is a minimal Telegram + OpenAI chat bot. It uses the OpenAI HTTP API (no `openai` Python package required), so installation is lightweight.

## Files
- `bot.py` – main bot code
- `requirements.txt` – Python dependencies
- `.env.example` – example env file (rename to `.env` and fill your keys)

## Setup (Termux / Linux / Windows)

1. Copy the ZIP contents to your device and `cd` into the folder.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Termux/macOS
   venv\Scripts\activate    # Windows (PowerShell)
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file from the example:
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and replace the placeholders:
   ```text
   TELEGRAM_BOT_TOKEN=1234567890:ABC...   # from @BotFather
   OPENAI_API_KEY=sk-...                  # create at https://platform.openai.com/account/api-keys
   ```
   **Important:** If a key ever leaks, revoke it immediately on the provider's dashboard.
5. Run the bot:
   ```bash
   python bot.py
   ```
6. In Telegram, send `/start` to your bot and then send messages.

## Notes & Troubleshooting
- If you get `InvalidToken` from the Telegram library, verify your `TELEGRAM_BOT_TOKEN` value is correct and has no extra spaces or quotes.
- If OpenAI calls fail, check your `OPENAI_API_KEY` and internet connectivity.
- On Termux, if package installation fails for some libraries, try using the exact versions in `requirements.txt` or use pip's `--prefer-binary` flag.

## Security
- Never commit real API keys to public GitHub repositories.
- Use `.env` for local development and deployment secret stores for production.
