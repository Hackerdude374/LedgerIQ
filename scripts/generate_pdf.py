
from fpdf import FPDF
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'LedgerIQ Financial Report', 0, 1, 'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf_report(df, output_path):
    """Generate PDF report with charts and tables"""
    # Create summary
    summary = df.groupby('Category')['Amount'].sum().reset_index()
    
    # Generate plot
    plt.figure(figsize=(8, 5))
    summary.set_index('Category')['Amount'].plot(kind='bar')
    plt.title('Spending by Category')
    plt.tight_layout()
    
    # Save plot to buffer
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    plt.close()
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.read()).decode('utf-8')
    
    # Create PDF
    pdf = PDFReport()
    pdf.add_page()
    
    # Add image
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Financial Summary', 0, 1)
    pdf.image(img_buffer, x=50, w=100)
    
    # Add table
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Transaction Summary', 0, 1)
    pdf.set_font('Arial', '', 10)
    
    # Table headers
    pdf.cell(60, 10, 'Category', 1)
    pdf.cell(40, 10, 'Amount', 1, 1)
    
    # Table rows
    for _, row in summary.iterrows():
        pdf.cell(60, 10, row['Category'], 1)
        pdf.cell(40, 10, f"${row['Amount']:.2f}", 1, 1)
    
    # Add transaction details
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Transaction Details', 0, 1)
    
    # Transaction table headers
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(40, 10, 'Date', 1)
    pdf.cell(80, 10, 'Description', 1)
    pdf.cell(30, 10, 'Amount', 1)
    pdf.cell(40, 10, 'Category', 1, 1)
    
    # Transaction rows
    pdf.set_font('Arial', '', 10)
    for _, row in df.iterrows():
        pdf.cell(40, 10, str(row['Date'].date()), 1)
        pdf.cell(80, 10, row['Description'][:50], 1)
        pdf.cell(30, 10, f"${row['Amount']:.2f}", 1)
        pdf.cell(40, 10, row['Category'], 1, 1)
    
    pdf.output(output_path)