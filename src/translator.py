from googletrans import Translator


def translate(text):
    # Create a translator
    translator = Translator()
    # Translate the text to English
    translated_text = translator.translate(text, dest="en").text

    return translated_text
