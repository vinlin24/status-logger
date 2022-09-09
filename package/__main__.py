"""__main__.py

Package entry point.
"""

from .core import get_status
from .driver import get_driver
from .logger import log_exit_status, send_error_email
from .writer import log_status

print("Running the status-logger package...")

try:
    driver = get_driver()
    emoji, text = get_status(driver)
    log_status(emoji, text)
    log_exit_status(None)
    print("Finished running the status-logger package: SUCCESS.")
except Exception as e:
    send_error_email(e)
    log_exit_status(e)
    print("Finished running the status-logger package: ERROR.")
