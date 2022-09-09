"""secrets.py

Loads and stores sensitive values as constants.
"""

import os

import dotenv

# Load if .env file is set up
dotenv.load_dotenv(override=True)

DISCORD_EMAIL = os.environ["DISCORD_EMAIL"]
"""Email address associated with my Discord account."""

DISCORD_PASSWORD = os.environ["DISCORD_PASSWORD"]
"""Password to my Discord account."""

ERROR_EMAIL = os.environ["ERROR_EMAIL"]
"""Email to send and receive error reports."""

ERROR_EMAIL_PASSWORD = os.environ["ERROR_EMAIL_PASSWORD"]
"""Password to the email used to send and receive error reports."""
