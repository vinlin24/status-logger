"""__main__.py

Package entry point.
"""

import sys

from .core import get_status
from .driver import get_driver
from .logger import log_exit_status, send_error_email
from .writer import log_status

# Run the program windowed (debugging) if any args are supplied
headless = (len(sys.argv) == 1)

print(f"Running the status-logger package ({headless=})...")

try:
    with get_driver(headless) as driver:
        emoji, text = get_status(driver)
    log_status(emoji, text)
    log_exit_status(None)
    print("Finished running the status-logger package: SUCCESS.")
except Exception as e:
    # send_error_email(e)
    # log_exit_status(e)
    print("Finished running the status-logger package: ERROR.")
    print(f"{type(e).__name__}: {e}")
