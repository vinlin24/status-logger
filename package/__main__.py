"""__main__.py

Package entry point.
"""

import sys

from .core import get_status
from .driver import get_driver
from .logger import log_exit_status, send_error_email
from .writer import log_status

# Don't log to files and send email
CONSOLE_ONLY = False

# Run the program windowed (debugging) if any args are supplied
headless = (len(sys.argv) == 1)

print(f"Running the status-logger package ({CONSOLE_ONLY=}, {headless=})...")

try:
    with get_driver(headless) as driver:
        emoji, text = get_status(driver)
    print(f"Extracted {emoji=} and {text=}.")
    # I almost never not have a status; this must mean scraping failed
    if not emoji and not text:
        raise Exception(
            "Status could not be extracted. If you really did not have a"
            "status set up for today, ignore this."
        )
except Exception as e:
    if not CONSOLE_ONLY:
        log_exit_status(e)
        send_error_email(e)
    print("Finished running the status-logger package: ERROR.")
    print(f"{type(e).__name__}: {e}")
else:
    if not CONSOLE_ONLY:
        log_status(emoji, text)
        log_exit_status(None)
    print("Finished running the status-logger package: SUCCESS.")
