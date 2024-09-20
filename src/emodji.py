def emotionAnalysis(text):
    # Simple logic for emotion analysis
    if "!" in text or "дуже подобається" in text:
        return "Позитивне"
    elif "?" in text:
        return "Питальне"
    else:
        return "Нейтральне"
