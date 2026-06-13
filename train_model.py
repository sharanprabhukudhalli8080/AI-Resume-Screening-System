import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import joblib

df = pd.read_csv("data/resume_dataset.csv")

X = df["resume_text"]
y = df["category"]

vectorizer = TfidfVectorizer()

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()

model.fit(X_vec, y)

joblib.dump(model, "models/resume_classifier.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("Model Saved Successfully")