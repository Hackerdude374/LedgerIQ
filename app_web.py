from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
from scripts.load_data import load_transaction_data
from scripts.clean_and_categorize import clean_and_categorize
from scripts.export_excel import export_to_excel
from scripts.generate_pdf import generate_pdf_report

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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
    categorized_df, summary = clean_and_categorize(df)
    export_to_excel(categorized_df, summary)
    generate_pdf_report(summary)

    return redirect(url_for('download'))

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/get/<filename>')
def get_file(filename):
    return send_from_directory('outputs', filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
