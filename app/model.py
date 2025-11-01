import joblib
import os
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class Predictor:
    def __init__(self, model_path):
        if os.path.exists(model_path):
            self.pipe = joblib.load(model_path)
        else:
            self.pipe = make_pipeline(
                TfidfVectorizer(),
                LogisticRegression()
            )
            texts = ["good movie", "bad movie"]
            labels = ["positive", "negative"]
            self.pipe.fit(texts, labels)

    def predict(self, text):
        pred = self.pipe.predict([text])[0]
        if hasattr(self.pipe, 'predict_proba'):
            prob = max(self.pipe.predict_proba([text])[0])
        else:
            prob = 1.0
        return pred, prob
