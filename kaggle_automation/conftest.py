# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def setup():
    # Configure Chrome options (optional)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Setup Chrome driver (auto downloads the correct driver)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    yield driver  # provide the driver to the test
    
    # Teardown: quit the browser after test finishes
    driver.quit()
