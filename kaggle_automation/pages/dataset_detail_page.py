# pages/dataset_detail_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class DatasetDetailPage(BasePage):
    VIEWS = (By.XPATH, "//span[text()='Views']/following-sibling::span")
    DOWNLOADS = (By.XPATH, "//span[text()='Downloads']/following-sibling::span")
    ENGAGEMENT = (By.XPATH, "//span[text()='Engagement']/following-sibling::span")
    COMMENTS = (By.XPATH, "//span[text()='Comments']/following-sibling::span")
    DOWNLOADS_DROPDOWN = (By.XPATH, "//div[contains(text(),'Downloads')]//following-sibling::div//button")
    LAST_SIX_MONTHS_OPTION = (By.XPATH, "//button[contains(text(), 'Last six months')]")
    MARCH_7_POINT = (By.XPATH, "//div[contains(@aria-label, 'Mar 7, 2025')]")
    TOOLTIP = (By.CLASS_NAME, "hover-tooltip")  # Adjust based on actual tooltip selector

    def validate_activity_overview(self):
        return {
            "views": self.get_text(self.VIEWS),
            "downloads": self.get_text(self.DOWNLOADS),
            "engagement": self.get_text(self.ENGAGEMENT),
            "comments": self.get_text(self.COMMENTS),
        }

    def select_last_six_months(self):
        self.click(self.DOWNLOADS_DROPDOWN)
        self.click(self.LAST_SIX_MONTHS_OPTION)

    def get_downloads_for_date(self):
        self.hover(self.MARCH_7_POINT)
        return self.get_text(self.TOOLTIP)
