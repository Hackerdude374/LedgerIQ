import argparse
import os
from datetime import datetime
from scripts import (
    load_data,
    clean_and_categorize,
    export_excel,
    generate_pdf,
    email_report,
    database_save,
    powerbi_export,
    quickbooks_api,
    smart_categorizer
)

# Future imports
# from scripts.flask_ui import create_app

def main():
    parser = argparse.ArgumentParser(description='LedgerIQ Accounting Automation')
    parser.add_argument('--file', required=True, help='Input CSV/Excel file')
    parser.add_argument('--email', help='Email to send report')
    parser.add_argument('--quickbooks', action='store_true', help='Enable QuickBooks integration')
    parser.add_argument('--ml', action='store_true', help='Enable ML categorization')
    args = parser.parse_args()

    # Create output directories
    os.makedirs('outputs', exist_ok=True)
    os.makedirs('database', exist_ok=True)

    # Load data
    print("🔄 Loading transaction data...")
    df = load_data.load_transaction_data(args.file)
    
    # Clean and categorize
    print("🧹 Cleaning and categorizing transactions...")
    if args.ml:
        df = smart_categorizer.ml_categorize(df)
    else:
        df = clean_and_categorize.categorize_transactions(df)
    
    # QuickBooks integration
    if args.quickbooks:
        print("🔌 Syncing with QuickBooks...")
        df = quickbooks_api.sync_with_quickbooks(df)
    
    # Generate reports
    print("📊 Generating reports...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_path = f"outputs/report_{timestamp}.xlsx"
    pdf_path = f"outputs/report_{timestamp}.pdf"
    bi_path = f"outputs/bi_data_{timestamp}.csv"
    
    export_excel.generate_excel_report(df, excel_path)
    generate_pdf.generate_pdf_report(df, pdf_path)
    powerbi_export.export_for_bi(df, bi_path)
    
    # Save to database
    print("💾 Saving to database...")
    database_save.save_to_database(df, "database/accounting_data.sqlite")
    
    # Email reports
    if args.email:
        print(f"📧 Sending email to {args.email}...")
        email_report.send_report(args.email, [excel_path, pdf_path])
    
    print("✅ Processing complete!")
    print(f"Excel report: {excel_path}")
    print(f"PDF report: {pdf_path}")

if __name__ == "__main__":
    main()