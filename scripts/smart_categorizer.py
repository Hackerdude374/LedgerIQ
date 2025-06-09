from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

MODEL_PATH = "ml_models/category_model.pkl"

def ml_categorize(df):
    """Categorize transactions using ML model"""
    try:
        # Load pre-trained model
        vectorizer, model = joblib.load(MODEL_PATH)
        X = vectorizer.transform(df['Description'])
        df['Category'] = model.predict(X)
        return df
    except:
        print("⚠️ ML model not available. Using rule-based categorization")
        from . import clean_and_categorize
        return clean_and_categorize.categorize_transactions(df)

def train_model(training_data_path):
    """Train ML categorization model (for future use)"""
    # Implementation would go here
    pass