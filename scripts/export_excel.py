import pandas as pd
import os

def export_to_excel(df, summary):
    output_path = os.path.join('outputs', 'monthly_report.xlsx')
    with pd.ExcelWriter(output_path) as writer:
        df.to_excel(writer, sheet_name='Transactions', index=False)
        summary.to_excel(writer, sheet_name='Summary', index=False)
