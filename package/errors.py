"""errors.py

Handles actions taken when an error occurred in the program.
"""

import smtplib
from datetime import date
from email.message import EmailMessage

from .secrets import ERROR_EMAIL, ERROR_EMAIL_PASSWORD


def _generate_content(error: Exception) -> str:
    return "TODO"


def send_error_email(error: Exception) -> None:
    print("Error detected, preparing to send email...")
    content = _generate_content(error)

    # Construct email object
    message = EmailMessage()
    message.set_content(content)
    message["Subject"] = f"Error in status-logger program {date.today()}"
    message["From"] = ERROR_EMAIL
    message["To"] = ERROR_EMAIL

    # Send email to self through Outlook server
    # https://www.arclab.com/en/kb/email/list-of-smtp-and-imap-servers-mailserver-list.html
    host, port = "smtp-mail.outlook.com", 587
    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(user=ERROR_EMAIL, password=ERROR_EMAIL_PASSWORD)
        smtp.send_message(message)

    print("Email sent successfully.")
