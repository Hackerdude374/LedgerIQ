import smtplib
from email.message import EmailMessage
import os

def send_email_report(recipient_email):
    msg = EmailMessage()
    msg['Subject'] = 'Your Monthly Financial Report'
    msg['From'] = 'your_email@example.com'
    msg['To'] = recipient_email
    msg.set_content('Attached is your monthly report.')

    with open('outputs/monthly_report.pdf', 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='monthly_report.pdf')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_password')
        smtp.send_message(msg)
