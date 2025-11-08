        # bot.py
        # Telegram AI Bot using OpenAI (via HTTP request) and python-telegram-bot
        # Edit the .env file to add your real BOT_TOKEN and OPENAI_API_KEY before running.
        import os
        import requests
        from dotenv import load_dotenv
        from telegram import Update
        from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

        load_dotenv()
        BOT_TOKEN = os.getenv('7686902618:AAG9XouZcvEB11aUk-0xq6Zlpj8EOpZKGAc')
        OPENAI_API_KEY = os.getenv('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')

        if not BOT_TOKEN:
            raise SystemExit("Error: TELEGRAM_BOT_TOKEN not set. Edit .env and add your token.")

        if not OPENAI_API_KEY:
            print("Warning: OPENAI_API_KEY not set. The bot will reply with a placeholder message.")

        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await update.message.reply_text(
                "👋 হ্যালো! আমি তোমার AI বট।
"
                "টোকেন এবং API কি সঠিকভাবে সেট করলে আমি ChatGPT-এর মতো উত্তর দেব।"
            )

        async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
            user_text = update.message.text or ''
            # Inform user if no OpenAI key configured
            if not OPENAI_API_KEY:
                await update.message.reply_text("OpenAI API key configured না থাকায় আমি এখন উত্তর দিতে পারছি না. .env ফাইল চেক করো.")
                return

            # Show a typing placeholder
            await update.message.chat_action(action='typing')

            try:
                # Call OpenAI Chat Completions (HTTP API)
                url = "https://api.openai.com/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json",
                }
                payload = {
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant that replies in Bengali when user writes in Bengali."},
                        {"role": "user", "content": user_text}
                    ],
                    "max_tokens": 500,
                    "temperature": 0.7
                }
                resp = requests.post(url, headers=headers, json=payload, timeout=30)
                if resp.status_code == 200:
                    data = resp.json()
                    reply = data['choices'][0]['message']['content'].strip()
                else:
                    reply = f"OpenAI API error: {resp.status_code} - {resp.text[:200]}"
            except Exception as e:
                reply = f"Error while contacting OpenAI: {e}"

            await update.message.reply_text(reply)

        def main():
            app = ApplicationBuilder().token(BOT_TOKEN).build()
            app.add_handler(CommandHandler('start', start))
            app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
            print("Bot is running. Send /start in Telegram to test.")
            app.run_polling()

        if __name__ == '__main__':
            main()
