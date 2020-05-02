import configparser
import telebot
import emoji
import regex
import config
from yandex_translate import YandexTranslate


Token = config.Token
bot = telebot.TeleBot(Token)
lang_to = "en"
sess = {}




@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Для  выбора языка используйте слудующие команды.\n" +
    "\\lang_to - для  установки языка на которого переводить. По умолчанию будет   использоватся английский язык ")


@bot.message_handler(commands=['lang_to'])
def handle_lang(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Анг', switch_inline_query="en", callback_data="en"))
    markup.add(telebot.types.InlineKeyboardButton(text='Ru', switch_inline_query="ru", callback_data="ru"))
    bot.send_message(message.chat.id, "Выберите язык.", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "en":
            sess[call.message.chat.id] = 'en'
        elif call.data == "ru":
            sess[call.message.chat.id] = 'ru'



@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.reply_to(message, translate_to_en(message.text, message.chat.id))

def translate_to_en(text, user_id):
    translator = YandexTranslate(config.Yandex_api_key)


    if sess[user_id]:
        result = translator.translate(text,  f"ru-en")
        return result['text']
    elif not sess[user_id]:
        result = translator.translate(text,  f"ru-en")
        return result['text']

if __name__ == "__main__":
    bot.polling()