import smtplib
import os
from typing import Optional

def send_notification(message: str) -> None:
    email: Optional[str] = os.environ.get('EMAIL_USER')
    password: Optional[str] = os.environ.get('EMAIL_PASS')
    recipient: Optional[str] = os.environ.get('EMAIL_RECIPIENT')
    if not email or not password or not recipient:
        print("Email credentials not set in environment variables.")
        return
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, recipient, message)
    server.quit()
