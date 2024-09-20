from langdetect import detect
from googletrans import Translator

def detect_and_translate(text):
    language = detect(text)

    if language != 'en':
        translator = Translator()
        translated_text = translator.translate(text, dest='en').text
        return translated_text
    else:
        return text


