# pages/home_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    DATASETS_BTN = (By.LINK_TEXT, "Datasets")

    def go_to_datasets(self):
        self.click(self.DATASETS_BTN)
