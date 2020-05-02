
import telebot
from googletrans import *
import config

#print(googletrans.LANGUAGES)
bot = telebot.TeleBot("1297569871:AAEWP51O-YhcOr9KMUh0ZEDYAfaqCXnkE6Q")
translator = Translator()


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	pass

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.reply_to(message, translate_to_en(message.text))

def translate_to_en(text):
    translator = Translator()
    result = translator.translate(text,  dest='en')
    return result.text

if __name__ == "__main__":
    bot.polling()

