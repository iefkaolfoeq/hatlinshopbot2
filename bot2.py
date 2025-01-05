from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ответ на команду /start."""
    welcome_message = (
        "Привет! Я HatlinBot, помощник в продаже.\n"
        "Я могу помочь вам с покупкой:\n"
        "- Голда в игре Standoff 2\n"
        "- UC в PUBG MOBILE\n"
        "- Игры в Steam\n\n"
        "Или присоединиться к нашему каналу: @hatlinshop\n"
        "Чтобы купить голду нажми на кнопку Купить голду🍯\n"
        "Продажа UC и игр пока в разработке."
    )

    keyboard = [
        [InlineKeyboardButton("Купить голду🍯", callback_data="buy_gold")],
        [InlineKeyboardButton("Поддержка", url="https://t.me/rollershow")],
        [InlineKeyboardButton("Новости", url="https://t.me/hatlinshop")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ответ на команду /gold."""
    gold_message = (
        "Выберите количество голды для покупки:\n\n"
        "После успешной оплаты оставьте ID своего аккаунта в Standoff 2 "
        "и ожидайте 5-10 минут."
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "100 голды 🍯",
                url="https://yoomoney.ru/quickpay/shop-widget?receiver=4100118505105584&quickpay=shop&paymentType=AC&sum=90"
            )
        ],
        [
            InlineKeyboardButton(
                "1000 голды 🍯",
                url="https://yoomoney.ru/quickpay/shop-widget?receiver=4100118505105584&quickpay=shop&paymentType=AC&sum=800"
            )
        ],
        [
            InlineKeyboardButton(
                "3000 голды 🍯",
                url="https://yoomoney.ru/quickpay/shop-widget?receiver=4100118505105584&quickpay=shop&paymentType=AC&sum=1980"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(gold_message, reply_markup=reply_markup)
    else:
        await update.message.reply_text(gold_message, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик нажатия кнопок."""
    query = update.callback_query
    if query.data == "buy_gold":
        await gold(update, context)

def main() -> None:
    """Запуск бота."""
    # Замените 'YOUR_TOKEN_HERE' на токен вашего бота
    application = Application.builder().token("7759495399:AAE0WacZzSdc-fiIjrFCUlNVigAkHKkGcO0").build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("gold", gold))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()





bot.polling(none_stop=True)