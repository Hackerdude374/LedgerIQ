def clean_and_categorize(df):
    rules = {
        'amazon': 'Shopping',
        'uber': 'Transport',
        'starbucks': 'Food',
        'paypal': 'Income',
        'freelance': 'Income'
    }
    df['Category'] = df['Description'].str.lower().apply(
        lambda desc: next((cat for key, cat in rules.items() if key in desc), 'Other')
    )
    summary = df.groupby('Category')['Amount'].sum().reset_index()
    return df, summary
