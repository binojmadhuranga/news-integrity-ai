from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

from utils.text_cleaner import clean_text

app = Flask(__name__)
CORS(app)

# Load trained model and vectorizer
model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Fake News API running"}), 200


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Text field is required"}), 400

    raw_text = data["text"]
    cleaned_text = clean_text(raw_text)

    vectorized_text = vectorizer.transform([cleaned_text])

    prediction = model.predict(vectorized_text)[0]
    confidence = model.predict_proba(vectorized_text)[0].max()

    response = {
        "prediction": "REAL" if prediction == 1 else "FAKE",
        "confidence": round(float(confidence), 2)
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
