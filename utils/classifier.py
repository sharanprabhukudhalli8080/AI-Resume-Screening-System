import joblib

model = joblib.load(
    "models/resume_classifier.pkl"
)

vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

def predict_category(text):

    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)

    return prediction[0]