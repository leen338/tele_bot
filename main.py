import os
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask

# ===== Flask server dummy =====
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# ===== Telegram Bot =====
TOKEN = os.environ.get("TELEGRAM_TOKEN")  # نفس الاسم في Environment

# الأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is running!")

# إعداد الـ Application
app_bot = ApplicationBuilder().token(TOKEN).build()
app_bot.add_handler(CommandHandler("start", start))

# ===== Threads =====
if __name__ == "__main__":
    # شغّل Flask server في Thread منفصل
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # شغّل Telegram bot
    app_bot.run_polling()







