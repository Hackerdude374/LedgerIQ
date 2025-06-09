import argparse
from scripts.load_data import load_transaction_data
from scripts.clean_and_categorize import clean_and_categorize
from scripts.export_excel import export_to_excel
from scripts.generate_pdf import generate_pdf_report
from scripts.email_report import send_email_report
from scripts.database_save import save_to_database
from scripts.powerbi_export import prepare_bi_output

# Optional future features
# from scripts.quickbooks_api import sync_with_quickbooks
# from scripts.flask_ui import run_web_ui
# from scripts.smart_categorizer import ml_categorize

def main():
    parser = argparse.ArgumentParser(description="LedgerIQ: Accounting Automation Tool")
    parser.add_argument('--file', required=True, help='Path to the transactions CSV file')
    parser.add_argument('--email', help='Send report to this email')
    # parser.add_argument('--web', action='store_true', help='Run web interface')
    args = parser.parse_args()

    df = load_transaction_data(args.file)
    categorized_df, summary = clean_and_categorize(df)
    export_to_excel(categorized_df, summary)
    generate_pdf_report(summary)
    if args.email:
        send_email_report(args.email)
    save_to_database(categorized_df)
    prepare_bi_output(categorized_df)

    # Future hooks:
    # sync_with_quickbooks(categorized_df)
    # ml_categorize(categorized_df)
    # if args.web:
    #     run_web_ui()

if __name__ == "__main__":
    main()
