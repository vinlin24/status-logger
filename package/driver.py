"""driver.py

Initializes the web driver instance.
"""

from collections.abc import Generator
from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

WAIT_TIMEOUT = 15.0
"""Time in seconds for driver to wait for pages to load."""


@contextmanager
def get_driver(headless: bool) -> Generator[webdriver.Edge, None, None]:
    """Initialize and return the Edge web driver instance to use."""
    service = Service(EdgeChromiumDriverManager().install())
    options = Options()
    options.headless = headless
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(WAIT_TIMEOUT)
    try:
        yield driver
    finally:
        driver.quit()
