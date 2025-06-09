import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_report(email, attachments):
    """Send report via email"""
    msg = MIMEMultipart()
    msg['From'] = "ledgeriq@example.com"
    msg['To'] = email
    msg['Subject'] = "LedgerIQ Financial Report"
    
    body = """
    <h1>Your Financial Report</h1>
    <p>Attached are your latest financial reports from LedgerIQ.</p>
    <p>This is an automated message. Please do not reply.</p>
    """
    msg.attach(MIMEText(body, 'html'))
    
    for file_path in attachments:
        with open(file_path, 'rb') as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        msg.attach(part)
    
    # In production, use real SMTP credentials
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('user', 'password')
        server.send_message(msg)