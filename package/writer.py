"""writer.py

Logs the extracted status to the destination file.
"""

import csv
import os
from datetime import datetime

DESTINATION_PATH = os.path.join(os.path.expanduser("~"),
                                ".config/status-logger/statuses.csv")


def _ensure_file() -> None:
    """Ensure the existence of the CSV file.

    Postcondition:
        Does nothing if the file already exists. Otherwise, creates the
        file and its directory if necessary.
    """
    if not os.path.exists(DESTINATION_PATH):
        # Attempt to make the directory if it exists
        try:
            os.mkdir(os.path.dirname(DESTINATION_PATH))
        except FileExistsError:
            pass
        # Make the file
        with open(DESTINATION_PATH):
            pass


def log_status(emoji: str | None, text: str) -> None:
    """Log the status to the CSV file.

    Args:
        emoji (str | None): The emoji part of the status in :colon:
        form. None if the status did not use an emoji.
        text (str): The text part of the status.

    Postcondition:
        The CSV file exists at the destination path.
    """
    _ensure_file()

    # Ideally, I'll have a status per day, so the date should be enough
    # The time part is included for potential debugging purposes
    timestamp = datetime.now()
    date = timestamp.date()
    time = timestamp.time()

    # According to: https://docs.python.org/3/library/csv.html#csv.writer
    # File objects should use newline=""
    with open(DESTINATION_PATH, "at", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow([date, time, emoji, text])
