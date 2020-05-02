from googletrans import *

#print(googletrans.LANGUAGES)
translator = Translator()

while True:
    translator = Translator()
    to_translate = input(">>")
    result = translator.translate(to_translate, src = 'ru' ,dest='en')
    print(result.text, end="\n")