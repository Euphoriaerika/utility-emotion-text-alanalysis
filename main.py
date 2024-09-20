from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    sentence = data.get("sentence")

    # Проста логіка для аналізу емоцій
    if "!" in sentence or "дуже подобається" in sentence:
        sentiment = "Позитивне"
    elif "?" in sentence:
        sentiment = "Питальне"
    else:
        sentiment = "Нейтральне"

    return jsonify({"sentiment": sentiment})


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Отримує порт із середовища або використовує 5000
    app.run(host='0.0.0.0', port=port)
