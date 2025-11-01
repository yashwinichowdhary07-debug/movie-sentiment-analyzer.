import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--data', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()

os.makedirs(os.path.dirname(args.output), exist_ok=True)
df = pd.read_csv(args.data)
X, y = df['text'], df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = make_pipeline(TfidfVectorizer(max_features=5000), LogisticRegression(max_iter=200))
pipe.fit(X_train, y_train)

preds = pipe.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))

joblib.dump(pipe, args.output)
print(f"Model saved to {args.output}")
