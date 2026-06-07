import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# تفعيل سجلات الأخطاء لمراقبة البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# إعدادات البوت والقروب الخاصة بك
TOKEN = "8855546720:AAFmdwj5vo5zB3Q43Uohedu1kHDLnIo-07M"
GROUP_ID = -1003884459149

async def forward_to_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == "private":
        user = update.effective_user
        username = f"@{user.username}" if user.username else "بدون يوزرنيم"
        user_info = f"👤 من: {user.full_name} ({username}) [ID: {user.id}]\n\n"
        
        try:
            # تحويل الرسائل النصية
            if update.message.text:
                full_message = f"{user_info}📝 الرسالة:\n{update.message.text}"
                await context.bot.send_message(chat_id=GROUP_ID, text=full_message)
                
            # تحويل الصور والفيديوهات والملفات
            else:
                await context.bot.send_message(chat_id=GROUP_ID, text=f"{user_info}👇 أرسل الميديا التالية:")
                await update.message.forward(chat_id=GROUP_ID)
                
            # الرد التلقائي على المستخدم
            await update.message.reply_text("شكراً لك! تم استلام بياناتك بنجاح وحفظها.")
            
        except Exception as e:
            logging.error(f"خطأ أثناء تحويل البيانات: {e}")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE, forward_to_group))
    print("البوت الجديد يعمل الآن ومستعد لجمع البيانات...")
    application.run_polling()

if __name__ == '__main__':
    main()
