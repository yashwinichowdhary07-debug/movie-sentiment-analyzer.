from flask import Flask, request, render_template, jsonify
from app.model import Predictor

app = Flask(__name__, template_folder="templates", static_folder="static")
predictor = Predictor('models/sentiment_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    text = data['text']
    label, score = predictor.predict(text)
    return jsonify({'label': label, 'score': round(score, 3)})

if __name__ == '__main__':
    app.run(debug=True)
