"""selectors.py

Stores CSS selectors of useful web elements as string constants.
"""

# Experimenting with CSS selectors instead of full xpaths

Selector = str
"""Type alias for hinting strings as CSS selectors."""

EMAIL_INPUT = Selector("#uid_8")
"""The <input> for email on the login page."""

PASSWORD_INPUT = Selector("#uid_11")
"""The <input> for password on the login page."""

EMOJI_IMG = Selector(".emoji.emoji-V71N2V.emoji-3iqL7b.emoji-11a5QE")
"""The <img> of the emoji part, if included."""

TEXT_SPAN = Selector(".customStatus-1UAQAK > span")
"""The <span> of the text part, if included."""


XPATH_EMAIL_INPUT = ("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/"
                     "form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
XPATH_PASSWORD_INPUT = ("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/"
                        "form/div/div/div[1]/div[2]/div[2]/div/input")
XPATH_EMOJI_IMG = ("/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/"
                   "div/div/div[1]/section/div[2]/div[1]/div[2]/div[2]/div/"
                   "div[2]/div/img")
XPATH_TEXT_SPAN = ("/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/"
                   "div/div/div[1]/section/div[2]/div[1]/div[2]/div[2]/div/"
                   "div[2]/div/span")
