"""__main__.py

Package entry point.
"""

from .core import get_status
from .driver import get_driver
from .errors import send_error_email
from .writer import log_status

print("Running the status-logger package...")

try:
    driver = get_driver()
    emoji, text = get_status(driver)
    log_status(emoji, text)
    print("Finished running the status-logger package: SUCCESS.")
except Exception as e:
    send_error_email(e)
    print("Finished running the status-logger package: ERROR.")
