from fpdf import FPDF
import os

def generate_pdf_report(summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Monthly Summary Report", ln=True, align='C')
    pdf.ln(10)
    for _, row in summary.iterrows():
        pdf.cell(200, 10, txt=f"{row['Category']}: ${row['Amount']:.2f}", ln=True)
    pdf.output(os.path.join("outputs", "monthly_report.pdf"))
