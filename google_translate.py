
import telebot
from googletrans import *
import config

#print(googletrans.LANGUAGES)
bot = telebot.TeleBot("1297569871:AAEWP51O-YhcOr9KMUh0ZEDYAfaqCXnkE6Q")
translator = Translator()
lang_from = "ru"
lang_to = "en"
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Для  выбора языка используйте слудующие команды.\n" + 
    "\\lang_from  - для  установки языка с которого переводить. По умолчанию будет   использоватся русский язык.\n " +
    "\\lang_to - для  установки языка на которого переводить. По умолчанию будет   использоватся английский язык ")


@bot.message_handler(commands=['lang_from'])
def handle_lang(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Анг', switch_inline_query="en"))
    markup.add(telebot.types.InlineKeyboardButton(text='Ru', switch_inline_query="ru"))
    bot.send_message(message.chat.id, "Выберите язык.", reply_markup=markup)
    # bot.answer_callback_query(message.chat.id, show_alert='en', text="Дата выбрана")

@bot.message_handler(commands=['lang_to'])
def handle_lang(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Анг', switch_inline_query="en"))
    markup.add(telebot.types.InlineKeyboardButton(text='Ru', switch_inline_query="ru"))
    bot.send_message(message.chat.id, "Выберите язык.", reply_markup=markup)
    # bot.answer_callback_query(message.chat.id, show_alert='en', text="Дата выбрана")


@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.reply_to(message, translate_to_en(message.text))

def translate_to_en(text):
    translator = Translator()
    result = translator.translate(text, src=f"{lang_from}",  dest=f"{lang_to}")
    return result.text

if __name__ == "__main__":
    bot.polling()
    
