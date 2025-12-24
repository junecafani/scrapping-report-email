import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import schedule
import time
from organizer.core import (
    send_email,
    send_html_email,
    send_email_with_attachment,
    job
)

# Account details
sender_email = input("What's your email to send message? ")
password = input("What's your email password? ")
receiver_email = input("What's your receiver email? ")

print(type(sender_email, password, receiver_email))

"""send_email(sender_email, password, "Hello World", "This my first email i sent", receiver_email)"""

# Scheduled every 10:00 AM
"""schedule.every().day.at("10:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(60)"""