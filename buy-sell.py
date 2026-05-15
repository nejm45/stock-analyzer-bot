import smtplib
import os
from email.mime.text import MIMEText

def send_email(msg_text):
    sender_email = os.environ.get("EMAILUSER")
    receiver_email = sender_email
    password = os.environ.get("EMAIL_PASS")

    msg = MIMEText(msg_text)
    msg["Subject"] = "Test Email"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    send_email("Hello from Binance Bot ✅")
