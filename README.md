# 📊 LedgerIQ: Automated Accounting Assistant

**LedgerIQ** is an intelligent, end-to-end accounting automation tool built in Python. It streamlines the workflow for freelancers, small business owners, and contractors by importing raw financial transaction data (CSV/Excel), categorizing expenses, generating insightful reports (Excel, PDF), emailing summaries, and exporting to dashboards like Power BI or Tableau.

---

## 🔍 Real-World Problem

Manual bookkeeping is tedious, error-prone, and time-consuming. Many professionals use spreadsheets to manage income and expenses, which becomes overwhelming during tax season or monthly reviews.

---

## ✅ Solution

LedgerIQ automates the process by:

- 📥 Importing financial data from CSV or Excel
- 📂 Categorizing transactions with keyword-based rules
- 📊 Creating monthly financial summaries
- 📤 Exporting Excel + PDF reports
- 📧 Emailing reports to users
- 🗃️ Saving records in a local database
- 📈 Providing output for BI tools like Power BI and Tableau

---

## 🧰 Tech Stack

| Layer        | Tool/Library                |
|--------------|-----------------------------|
| Core Logic   | Python, pandas              |
| Export       | openpyxl, matplotlib, fpdf  |
| Email        | smtplib, email.message      |
| Database     | SQLite, SQLAlchemy          |
| Interface    | argparse (CLI), tkinter (GUI optional) |
| Dashboard    | Power BI / Tableau          |

---

## 📁 Features

- ✅ Read and clean CSV/Excel transactions
- ✅ Auto-categorize expenses and income
- ✅ Group by category, vendor, or month
- ✅ Generate Excel spreadsheets with charts
- ✅ Generate PDF summary reports
- ✅ Email reports to specified users
- ✅ Store processed data in SQLite database
- ✅ BI-ready export for dashboards

---

## 🚀 Getting Started

### 🔧 Prerequisites

```bash
pip install pandas openpyxl fpdf matplotlib sqlalchemy
```

### ▶️ Run the Tool

```bash
python app.py --file data/transactions_sample.csv
```

---

## 📸 Sample Output

- ✅ `monthly_report.xlsx` (Totals per category)
- ✅ `monthly_report.pdf` (Pie chart + summary)
- ✅ `accounting_data.sqlite` (Stores all records)

---

## 📈 Power BI / Tableau Integration

All Excel outputs are dashboard-ready. Import into Power BI or Tableau to create live graphs of:

- Category-wise monthly expenses
- Vendor spending trends
- Net income flow by period

---

## 🤖 Future Add-ons

- 🔌 Stripe/QuickBooks API Integration
- 🌐 Web UI (Flask/FastAPI)
- 🧠 ML-based Smart Categorization

---

## 📄 License

MIT License

---

## 🧠 Author

Built by a Computer Science grad bridging the gap between **Finance and Automation**.  
This project demonstrates strong Python skills, real-world problem solving, and tech-business synergy.
