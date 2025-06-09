# Create stripe_integration.py that fetches transactions from Stripe and saves as CSV

import os

scripts_dir = "/mnt/data/LedgerIQ/scripts"
os.makedirs(scripts_dir, exist_ok=True)

stripe_code = """import stripe
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

def fetch_stripe_transactions(limit=10):
    load_dotenv()
    stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    charges = stripe.Charge.list(limit=limit)
    data = []

    for charge in charges.auto_paging_iter():
        description = charge.description or "Stripe Charge"
        amount = charge.amount / 100  # Stripe uses cents
        created = datetime.fromtimestamp(charge.created).strftime('%Y-%m-%d')
        data.append({
            "Date": created,
            "Description": description,
            "Amount": amount
        })

    df = pd.DataFrame(data)
    output_path = os.path.join("data", "stripe_transactions.csv")
    df.to_csv(output_path, index=False)
    print(f"✅ Stripe data saved to {output_path}")
    return df
"""

# Save the script
stripe_path = os.path.join(scripts_dir, "stripe_integration.py")
with open(stripe_path, "w") as f:
    f.write(stripe_code)

stripe_path
