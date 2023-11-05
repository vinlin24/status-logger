"""__main__.py

Package entry point.
"""

import sys
from argparse import ArgumentParser
from pathlib import Path

from .core import get_status
from .driver import get_driver
from .logger import log_exit_status, send_error_email
from .writer import log_status

# Debugging options
parser = ArgumentParser(description="Run the status-logger program")
parser.add_argument("-c", "--console",
                    action="store_true",
                    help="Only output to the console, no logs or email")
parser.add_argument("-w", "--window",
                    action="store_true",
                    help="Run the scraper windowed instead of headlessly")
parser.add_argument("-p", "--path",
                    type=Path,
                    help="Custom path to web driver executable")
ns = parser.parse_args(sys.argv[1:])

console_only: bool = ns.console
headless: bool = not ns.window
path: Path | None = ns.path

print(
    "Running the status-logger package ("
    f"{console_only=}, {headless=}, {path=}"
    ")..."
)

try:
    with get_driver(headless, path) as driver:
        emoji, text = get_status(driver)
    print(f"Extracted {emoji=} and {text=}.")
    # I almost never not have a status; this must mean scraping failed
    if not emoji and not text:
        raise Exception(
            "Status could not be extracted. If you really did not have a "
            "status set up for today, ignore this. It is also possible that "
            "the page did not load in time. Check your connection."
        )
except Exception as e:
    if not console_only:
        log_exit_status(e)
        send_error_email(e)
    print("Finished running the status-logger package: ERROR.")
    print(f"{type(e).__name__}: {e}")
    sys.exit(1)
else:
    if not console_only:
        log_status(emoji, text)
        log_exit_status(None)
    print("Finished running the status-logger package: SUCCESS.")
