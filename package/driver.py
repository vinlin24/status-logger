"""driver.py

Initializes the web driver instance.
"""

import os

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

DRIVER_PATH = os.path.join(os.path.dirname(__file__),
                           "../bin/msedgedriver.exe")
"""Absolute path to Edge web driver executable."""

WAIT_TIMEOUT = 5.0
"""Time in seconds for driver to wait for pages to load."""


def get_driver() -> webdriver.Edge:
    """Initialize and return the Edge web driver instance to use."""
    service = Service(DRIVER_PATH)
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(WAIT_TIMEOUT)
    return driver
