import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import schedule
import time

# Simple email text
def send_email(
    sender_email, password, subject, body, to_email):
    # Email message
    msg = MIMEMultipart
    msg['From'] = sender_email
    msg['To'] = subject
    msg['Subject'] = to_email

    # Attach the email
    msg.attach(MIMEText(body, 'plain'))

    # Set up SSL for connection
    context = ssl.create_default_context()

    try:
        # Connect to server using TLS encryption
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, to_email, text)

        print("Email sent sucessfully!")
    except Exception as e:
        print(f"Error: {e}")

# Send email in HTML format
def send_html_email(
    sender_email, 
    password, 
    subject, 
    body, 
    to_email
):
    # Email message
    msg = MIMEMultipart ()
    msg['From'] = sender_email
    msg['To'] = subject
    msg['Subject'] = to_email

    # Attach the HTML body
    msg.attach(MIMEText(body, 'html'))

    # Set up SSL for connection
    context = ssl.create_default_context()

    try:
        # Connect to server using TLS encryption
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, to_email, text)

        print("Email sent sucessfully!")
    except Exception as e:
        print(f"Error: {e}")

def send_email_with_attachment(
    sender_email, 
    password, 
    subject, 
    body, 
    to_email, 
    attachment_file
):
    # Email message
    msg = MIMEMultipart ()
    msg['From'] = sender_email
    msg['To'] = subject
    msg['Subject'] = to_email

    # Attach the email
    msg.attach(MIMEText(body, 'plain'))

    # Open and attach the file
    with open(attachment_file, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={attachment_path.split('/')[-1]}",
            )
        msg.attach(part)
    
    context = ssl.create_default_context

    try:
        # Connect mail server and send mail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, to_email, text)

        print("Email with attachment sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def job():
    send_email("Reminder", "This is your scheduled email.", "recipient@example.com")

