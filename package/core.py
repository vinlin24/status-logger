"""core.py

Webscraping sequences to obtain the current Discord cusom status.
"""

from selenium import webdriver


def get_status(driver: webdriver.Edge) -> tuple[str | None, str]:
    """Extract the current Discord custom status.

    Args:
        driver (webdriver.Edge): Initialized web driver instance.

    Returns:
        tuple[str | None, str]: A 2-tuple containing:
            0: The emoji part, if used, in :colon: form.
            1: The text part.
    """
    # Scraping sequences here
    return (None, "FIX THIS LATER")
