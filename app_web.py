from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
from scripts.load_data import load_transaction_data
from scripts.smart_categorizer import ml_categorize
from scripts.export_excel import export_to_excel
from scripts.generate_pdf import generate_pdf_report
from scripts.generate_charts import generate_category_charts
from scripts.stripe_integration import fetch_stripe_transactions
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from scripts.auth import get_user, validate_login, User



app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    file = request.files['file']
    if not file:
        return "No file uploaded", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    df = load_transaction_data(filepath)
    categorized_df = ml_categorize(df)
    summary = categorized_df.groupby("Category")["Amount"].sum().reset_index()
    export_to_excel(categorized_df, summary)
    generate_pdf_report(summary)
    generate_category_charts(categorized_df)
    return redirect(url_for('download'))

@app.route('/stripe')
def stripe_route():
    df = fetch_stripe_transactions(limit=5)
    categorized_df = ml_categorize(df)
    summary = categorized_df.groupby("Category")["Amount"].sum().reset_index()
    export_to_excel(categorized_df, summary)
    generate_pdf_report(summary)
    generate_category_charts(categorized_df)
    return redirect(url_for('download'))

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/get/<filename>')
def get_file(filename):
    return send_from_directory('outputs', filename, as_attachment=True)

@app.route('/get/charts/<filename>')
def get_chart(filename):
    return send_from_directory('outputs/charts', filename)

#LOGIN ROUTE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if validate_login(user, pwd):
            login_user(User(user))
            return redirect(url_for('index'))
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)

if __name__ == "__main__":
    app.run(debug=True)
