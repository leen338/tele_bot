from telegram.ext import Application, CommandHandler
import time

TOKEN = "8247936232:AAFtIiF8pFcTfSEDdgrDy6qVyZwp_iqxC1s"

async def start(update, context):
    await update.message.reply_text("🎉 البوت شغال!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("جاري التشغيل...")

# محاولات إعادة التشغيل التلقائي
while True:
    try:
        app.run_polling()
    except Exception as e:
        print(f"خطأ: {e}")
        print("إعادة التشغيل خلال 10 ثواني...")
        time.sleep(10)



