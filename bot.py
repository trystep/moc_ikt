from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request
from functions import *

# Идентификаторы кнопок
CALLBACK_BUTTON_NEXT = "CALLBACK_BUTTON_NEXT"
CALLBACK_BUTTON_BACK = "CALLBACK_BUTTON_BACK"
CALLBACK_BUTTON_LIST = "CALLBACK_BUTTON_LIST"

TITLES = {
    CALLBACK_BUTTON_NEXT: ">>",
    CALLBACK_BUTTON_BACK: "Назад",
    CALLBACK_BUTTON_LIST: "Список производителей электроники",
}


def get_base_inline_keyboard():
    """ Получить клавиатуру для сообщения
    """
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_LIST], callback_data=CALLBACK_BUTTON_LIST),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard2():
    """ Получить вторую страницу клавиатуры для сообщений
    """
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_NEXT], callback_data=CALLBACK_BUTTON_NEXT),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


@log_error
def keyboard_callback_handler(update: Update, context: CallbackContext):
    """ Обработчик ВСЕХ кнопок со ВСЕХ клавиатур
    """
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id

    if data == CALLBACK_BUTTON_NEXT:
        # Покажем новый текст и оставим ту же клавиатуру
        query.edit_message_text(
            text='\n'.join(list_page_2),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard2(),
        )

    elif data == CALLBACK_BUTTON_BACK:
        # Показать предыдущий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        query.edit_message_text(
            text=times_of_day(),
            reply_markup=get_base_inline_keyboard(),
        )
    elif data == CALLBACK_BUTTON_LIST:
        context.bot.send_message(
            chat_id=chat_id,
            text='\n'.join(list_page_1),
            reply_markup=get_keyboard2(),
        )


def do_start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=times_of_day(),
        reply_markup=get_base_inline_keyboard(),
    )


def do_help(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Привет! Я - диалоговый помощник (чат-бот) для мессенджера Telegram на языке программирования Python 3.\n\n"
             "Для начала диалога набери команду /start\n\n"
             "Чат-бот создан при выполнении тестового задания на позицию Junior Python Developer кандидата Алексеева М.С.",
        reply_markup=get_base_inline_keyboard(),
    )


def main():
    req = Request()
    bot = Bot(
        request=req,
        token='774955690:AAGEdLJSkvCeTzKBeVtainvEHxFAM3EMNmk',
        # Прокси, чтобы не блокировались запросы
        base_url='https://telegg.ru/orig/bot',
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    # Проверка, что бот корректно подключился к Telegram API
    # print(bot.get_me())

    # Навесить обработчики команд
    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(buttons_handler)

    # Начать бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
