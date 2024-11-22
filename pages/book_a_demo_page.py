from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BookADemoPage(BasePage):
    form = (By.XPATH, "//div[@id='m_class']//form[@id='demoForm']")

    def __init__(self, driver):
        super().__init__(driver)

    def test_form_is_displayed(self):
        return self.displayed(self.form)
