from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from translator import detect_and_translate

def emotionAnalysis(text):
    text = detect_and_translate(text)

    # Simple logic for emotion analysis
    analyzer = SentimentIntensityAnalyzer()

    # Scores are between -1 and 1 for negative, neutral and positive
    scores = analyzer.polarity_scores(text)

    return scores

print(emotionAnalysis("I love programming in Python!"))
print(emotionAnalysis("Я люблю програмування на Python!"))