from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# ضع التوكن مباشرة هنا
TOKEN = "8247936232:AAFtIiF8pFcTfSEDdgrDy6qVyZwp_iqxC1s"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("بوت شغال!")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()


