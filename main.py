import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl

# Account details
sender_email = input("What's your email to send message? ")
password = input("What's your email password? ")
receiver_email = input("What's your receiver email? ")

