import pandas as pd

def load_transaction_data(file_path):
    """Load transaction data from CSV or Excel file"""
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")
    
    # Basic cleaning
    df['Date'] = pd.to_datetime(df['Date'])
    df['Amount'] = pd.to_numeric(df['Amount'])
    df['Description'] = df['Description'].str.strip()
    
    return df