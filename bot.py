import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Настройки логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Основная логика бота
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "цена" in text or "քմ" in text or "стоимость" in text:
        await update.message.reply_text("1քմ-ի արժեքը 425,000 դրամ է։")
    elif "ипотека" in text or "հիփոթեք" in text:
        await update.message.reply_text("Այո, գործում է եկամտահարկի վերադարձի օրենքը։")
    elif "площадь" in text or "քմ" in text:
        await update.message.reply_text("Մենք ունենք բնակարաններ՝ 1 սենյականոց (27քմ), 2 սենյականոց (45քմ) և 3 սենյականոց (70քմ)։")
    elif "номер" in text or "հեռախոս" in text:
        await update.message.reply_text("Թողեք ձեր հեռախոսահամարը՝ վաճառքի մասնագետը կկապվի Ձեզ հետ։")
    else:
        await update.message.reply_text("Շնորհակալություն, հարցը փոխանցվեց մասնագետին։ Կարող եք թողնել հեռախոսահամար 📞")

# Асинхронная функция запуска
async def main():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

    if not TELEGRAM_TOKEN:
        raise Exception("TELEGRAM_TOKEN отсутствует в переменных окружения")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен")
    await app.run_polling()

# Запуск бота без asyncio.run()
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
