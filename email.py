from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

from email.message import EmailMessage
import aiosmtplib
import os
from dotenv import load_dotenv

load_dotenv()

async def send_confirmation_email(to_email: str, name: str):
    message = EmailMessage()
    message["From"] = os.getenv("EMAIL_USERNAME")
    message["To"] = to_email
    message["Subject"] = "Thanks for Contacting White Circle Groups"

    message.set_content(f"""
Hi {name},

Thanks for reaching out to us at White Circle Groups!

We’ve received your message and our team will get back to you within 24 hours.

Regards,
White Circle Groups Team
""")

    await aiosmtplib.send(
        message,
        hostname=os.getenv("EMAIL_HOST"),
        port=int(os.getenv("EMAIL_PORT")),
        start_tls=True,
        username=os.getenv("EMAIL_USERNAME"),
        password=os.getenv("EMAIL_PASSWORD")
    )
