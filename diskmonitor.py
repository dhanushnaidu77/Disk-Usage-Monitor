#!/usr/bin/env python3
import shutil
import smtplib
from email.mime.text import MIMEText


THRESHOLD = 80

# Email settings
SENDER_EMAIL = "dhan1@gmail.com"
RECEIVER_EMAIL = "dhan2@gmail.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your-smtp-username"
SMTP_PASS = "your-smtp-password"

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    usage_percentage = (used / total) * 100
    return usage_percentage

def send_alert(usage):
    msg = MIMEText(f"Warning: Disk usage exceeded threshold. Current usage: {usage}%")
    msg["Subject"] = "Disk Space Alert"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

def main():
    usage = check_disk_usage()
    if usage > THRESHOLD:
        send_alert(usage)

if __name__ == "__main__":
    main()
