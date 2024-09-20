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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
