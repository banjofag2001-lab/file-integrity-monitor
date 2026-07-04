import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


def send_email_alert(alerts):

    sender_email = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv("EMAIL_PASSWORD")

    receiver_email = sender_email


    message = EmailMessage()

    message["Subject"] = "Security Alert - File Integrity Monitor"
    message["From"] = sender_email
    message["To"] = receiver_email


    body = "Security changes detected:\n\n"

    for alert in alerts:
        body += alert + "\n"


    message.set_content(body)


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(message)