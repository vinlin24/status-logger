"""core.py

Webscraping sequences to obtain the current Discord cusom status.
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from .secrets import DISCORD_EMAIL, DISCORD_PASSWORD
from .xpaths import (XPATH_EMAIL_INPUT, XPATH_EMOJI_IMG, XPATH_PASSWORD_INPUT,
                     XPATH_TEXT_SPAN)

# ==================== SCRAPING SUBROUTINES ==================== #


def _login(driver: webdriver.Edge) -> None:
    """Handle authentication landing page.

    Copied directly from my counters/update_discord.py.

    Args:
        driver (webdriver.Edge): Edge web driver instance.
    """
    # Find elements
    email_input = driver.find_element(
        "xpath",
        XPATH_EMAIL_INPUT
    )
    password_input = driver.find_element(
        "xpath",
        XPATH_PASSWORD_INPUT
    )

    # Enter credentials
    email_input.clear()
    email_input.send_keys(DISCORD_EMAIL)
    password_input.clear()
    password_input.send_keys(DISCORD_PASSWORD + "\n")


def _extract_emoji(driver: webdriver.Edge) -> str | None:
    """Extract the emoji part of the custom status."""
    # An emoji was used: this img element should be present
    try:
        emoji_img = driver.find_element(
            "xpath",
            XPATH_EMOJI_IMG
        )
    # An emoji wasn't used
    except NoSuchElementException:
        return None

    return emoji_img.get_attribute("alt")


def _extract_text(driver: webdriver.Edge) -> str:
    """Extract the text part of the custom status."""
    # Get the <span> element that contains the text part
    try:
        status_input = driver.find_element(
            "xpath",
            XPATH_TEXT_SPAN
        )
    # <span> element doesn't exist if text is blank
    except NoSuchElementException:
        return ""

    return status_input.text


# ==================== INTERFACE FUNCTION ==================== #


def get_status(driver: webdriver.Edge) -> tuple[str | None, str]:
    """Extract the current Discord custom status.

    Args:
        driver (webdriver.Edge): Initialized web driver instance.

    Returns:
        tuple[str | None, str]: A 2-tuple containing:
            0: The emoji part as a Unicode character
            1: The text part.
    """
    # Scraping sequences here
    driver.get("https://discord.com/login")
    _login(driver)
    emoji = _extract_emoji(driver)
    text = _extract_text(driver)
    return (emoji, text)
