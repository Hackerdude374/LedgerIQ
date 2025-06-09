import pandas as pd
from smart_categorizer import train_model

train_data = pd.DataFrame({
    "Description": [
        "Uber Ride", "Amazon Purchase", "Starbucks Coffee",
        "PayPal Payment", "Freelance Client Work"
    ],
    "Category": ["Transport", "Shopping", "Food", "Income", "Income"]
})

train_model(train_data)
print("✅ ML model trained and saved!")
