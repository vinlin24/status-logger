"""driver.py

Initializes the web driver instance.
"""

from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

WAIT_TIMEOUT = 15.0
"""Time in seconds for driver to wait for pages to load."""


@contextmanager
def get_driver(headless: bool, path: Path | None
               ) -> Generator[webdriver.Edge, None, None]:
    """Initialize and return the Edge web driver instance to use."""
    if path is None:
        driver_path = EdgeChromiumDriverManager().install()
    else:
        driver_path = str(path)
    service = Service(executable_path=driver_path)
    options = Options()
    options.headless = headless
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(WAIT_TIMEOUT)
    try:
        yield driver
    finally:
        driver.quit()
