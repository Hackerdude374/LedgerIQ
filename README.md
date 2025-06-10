# 📊 LedgerIQ: Full-Stack Accounting Automation Platform (v2)

**LedgerIQ** is an intelligent, multi-user accounting automation system built with Python, Flask, PostgreSQL, and Machine Learning. It streamlines financial workflows for freelancers, SMBs, and analysts through data ingestion, smart categorization, reporting, and dashboard integration (Power BI/Tableau).

---

## 🔍 Problem

Manual accounting is error-prone, slow, and stressful. Tools like Excel require too much upkeep. Many users lack the automation to track trends or report efficiently.

---

## ✅ Solution: LedgerIQ

Automates your entire workflow:

- 📥 Upload transactions from Excel/CSV
- 🔁 Sync real-time Stripe payments
- 🔐 User login/signup, per-user data
- 🧠 ML-based smart categorization
- 📊 Reports in Excel and PDF
- 📈 Visual charts (matplotlib/seaborn)
- 🧾 Export to Power BI `.pbix` and Tableau `.twbx`
- ☁️ Designed for cloud deployment via Render

---

## 🧱 Tech Stack

| Layer        | Tech/Tools                              |
|--------------|------------------------------------------|
| Backend      | Python, Flask, Flask-Login               |
| DB           | PostgreSQL (via SQLAlchemy)              |
| ML           | scikit-learn, TF-IDF, Naive Bayes        |
| Auth         | Flask-Login, bcrypt                      |
| Frontend     | HTML, Bootstrap (planned), Jinja2        |
| Charts       | Matplotlib, Seaborn                      |
| Reports      | openpyxl, FPDF                           |
| API Sync     | Stripe API, (QuickBooks: coming soon)    |
| BI Export    | Power BI `.pbix`, Tableau `.twbx`        |
| Deployment   | Render (planned)                         |

---

## 🚀 Features (By Phase)

### ✅ Core Upload & Processing
- Upload Excel/CSV → ML categorization → reports

### ✅ Stripe Sync
- Auto-fetch transactions using your Stripe API key

### ✅ Smart Categorization
- Trains on descriptions using TF-IDF + Naive Bayes
- You can improve accuracy by retraining

### ✅ PDF + Excel Output
- `monthly_report.pdf`, `monthly_report.xlsx`, and visual charts

### ✅ Power BI & Tableau Support
- Generates BI-ready `.csv`, `.pbix`, and `.twbx` output

### ✅ Charts with Python
- Pie/Bar charts grouped by category using seaborn

### 🔐 User Authentication (in progress)
- Email/password login/signup
- Per-user upload history
- Protected routes

### ☁️ Cloud Deployment (Render)
- Will use PostgreSQL cloud DB
- Auto-deployed Flask app for live uploads/reporting

---

## 📦 Setup Instructions

```bash
# Install dependencies
pip install -r requirements.txt

# Train the ML model
python scripts/train_model.py

# Run CLI version
python app.py --file data/transactions_sample.csv

# Run Flask Web UI
python app_web.py
```

---

## 🧠 ML Model Details

- `train_model.py`: Trains the category classifier
- Uses TF-IDF vectorizer + Naive Bayes classifier
- Saves `vectorizer.pkl` and `category_model.pkl`

---

## 📈 Example Output

- **PDF Report** with category totals
- **Excel Report** with full transactions + summary
- **Charts**: `bar_chart.png`, `pie_chart.png`
- **Power BI/ Tableau Ready**: `bi_output.csv`

---

## 🔐 Auth Example

Signup → Login → Upload → Get custom reports linked to your account (coming soon)

---

## 💡 Future Roadmap

- ✅ Multi-user PostgreSQL integration
- ✅ Power BI / Tableau native exports
- ✅ Stripe sync API
- ⏳ QuickBooks API integration
- ⏳ Scheduled email reports
- ⏳ OAuth Login
- ⏳ Admin dashboard

---

## 📄 License

MIT License

---

## 🧠 Author

Built by a CS student integrating **Finance + Automation**  
For real-world productivity, learning, and standout projects.

---