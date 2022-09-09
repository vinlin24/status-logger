"""driver.py

Initializes the web driver instance.
"""

import os
from collections.abc import Generator
from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

DRIVER_PATH = os.path.join(os.path.dirname(__file__),
                           "../bin/msedgedriver.exe")
"""Absolute path to Edge web driver executable."""

WAIT_TIMEOUT = 5.0
"""Time in seconds for driver to wait for pages to load."""


@contextmanager
def get_driver(headless: bool) -> Generator[webdriver.Edge, None, None]:
    """Initialize and return the Edge web driver instance to use."""
    service = Service(DRIVER_PATH)
    options = Options()
    options.headless = headless
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(WAIT_TIMEOUT)
    try:
        yield driver
    finally:
        driver.quit()
