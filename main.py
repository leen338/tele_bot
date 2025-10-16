from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

TOKEN = "8247936232:AAFxRxvgu5NjbwBjIIEfmqu4XGL48xCYSyk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 البوت شغال!")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 جاري تشغيل البوت...")
    await app.run_polling()

if name == "main":
    while True:
        try:
            asyncio.run(main())
        except Exception as e:
            print(f"⚠️ خطأ: {e}")
            print("🔁 إعادة التشغيل بعد 10 ثوانٍ...")
            asyncio.sleep(10)




