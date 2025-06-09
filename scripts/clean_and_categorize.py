import pandas as pd

CATEGORY_MAP = {
    'amazon|target|walmart': 'Shopping',
    'uber|lyft|taxi': 'Transportation',
    'starbucks|coffee|cafe': 'Food & Drink',
    'paypal|stripe|venmo': 'Payment Processing',
    'salary|freelance|contract': 'Income',
    'rent|mortgage': 'Housing',
    'electric|water|gas|utility': 'Utilities'
}

def categorize_transactions(df):
    """Categorize transactions using keyword mapping"""
    def _categorize(description):
        description = description.lower()
        for pattern, category in CATEGORY_MAP.items():
            if any(kw in description for kw in pattern.split('|')):
                return category
        return 'Other'
    
    df['Category'] = df['Description'].apply(_categorize)
    return df