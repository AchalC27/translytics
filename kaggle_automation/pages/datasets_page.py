# pages/datasets_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class DatasetsPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search datasets']")
    FIRST_RESULT = (By.XPATH, "//a[contains(@href, '/datasets/') and contains(text(), 'Huge Stock Market Dataset')]")

    def search_dataset(self, query):
        self.send_keys(self.SEARCH_INPUT, query)
        from time import sleep
        sleep(2)  # Let search load results (replace with proper wait if needed)
        self.click(self.FIRST_RESULT)
