import os
import threading
from telegram import Bot
from telegram.ext import Updater, CommandHandler
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
# اسم التوكن بالـ Environment Variable
TOKEN = os.environ.get("TELEGRAM_TOKEN")  # يجب أن يكون نفسه على Render

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# مثال لأمر بسيط
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Bot is running!")

dispatcher.add_handler(CommandHandler("start", start))

# ===== Threads =====
if __name__ == "__main__":
    # شغّل Flask server في Thread منفصل
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # شغّل Telegram bot
    updater.start_polling()
    updater.idle()





