import telebot
import config
from yandex_translate import YandexTranslate

Token = config.Token
bot = telebot.TeleBot(Token)
lang_to = "en"
sess = {}


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Для  выбора языка используйте слудующие команды.\n" +
                     "\\lang_to - для  установки языка на которого переводить. По умолчанию будет   использоватся "
                     "английский язык ")


@bot.message_handler(commands=['lang_to'])
def handle_lang(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='C английского на русский', switch_inline_query="en-ru",
                                                  callback_data="en-ru"))
    markup.add(telebot.types.InlineKeyboardButton(text='С русского на английский', switch_inline_query="ru-en",
                                                  callback_data="ru-en"))
    bot.send_message(message.chat.id, "Выберите язык.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "en-ru":
            sess[call.message.chat.id] = 'en-ru'
        elif call.data == "ru-en":
            sess[call.message.chat.id] = 'ru-en'


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.reply_to(message, translate_to_en(message.text, message.chat.id))


def translate_to_en(text, user_id):
    translator = YandexTranslate(config.Yandex_api_key)

    if sess[user_id]:
        result = translator.translate(text, f"{sess[user_id]}")
        return result['text']
    elif not sess[user_id]:
        result = translator.translate(text, f"{sess[user_id]}")
        return result['text']


if __name__ == "__main__":
    bot.polling()
