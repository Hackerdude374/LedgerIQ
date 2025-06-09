import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

MODEL_PATH = os.path.join("scripts", "category_model.pkl")
VECTORIZER_PATH = os.path.join("scripts", "vectorizer.pkl")

def train_model(training_df):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(training_df['Description'])
    y = training_df['Category']

    model = MultinomialNB()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

def ml_categorize(df):
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        print("No trained model found. Please train it first.")
        return df

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    X_new = vectorizer.transform(df['Description'])
    df['Category'] = model.predict(X_new)

    return df
