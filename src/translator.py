from langdetect import detect
from googletrans import Translator


def detect_and_translate(text):
    language = detect(text)

    if language != "en":
        # Create a translator
        translator = Translator()
        # Translate the text to English
        translated_text = translator.translate(text, dest="en").text
        return translated_text

    # If the text is already in English, return it as it is
    return text
