from flask import Flask, request, jsonify
from emodji import emotionAnalysis

app = Flask(__name__)


@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    sentiment = emotionAnalysis(data.get("sentence"))

    return jsonify({"sentiment": sentiment})


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
