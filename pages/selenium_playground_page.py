from selenium.webdriver.common.by import By

from pages.ajax_form_submit_demo_page import AjaxFormSubmitDemoPage
from pages.base_page import BasePage
from pages.book_a_demo_page import BookADemoPage
from pages.lambdatest_login import LambdaTestLogin


class SeleniumPlaygroundPage(BasePage):
    selenium_playground_header = (By.TAG_NAME, "h1")

    login_link = (By.XPATH, '//a[contains(text(),"Login")]')
    book_a_demo_button = (By.XPATH, "//button[contains(text(),'Book a Demo')]")
    get_started_free_button = (By.XPATH, "//a[contains(text(),'Get Started Free')]")

    ajax_form_submit_link = (By.PARTIAL_LINK_TEXT, "Ajax Form Submit")
        # (By.XPATH, '//a[contains(text(),"Ajax Form Submit")]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_selenium_playground_header(self):
        return self.get_text(self.selenium_playground_header)

    def click_login_link(self):
        self.click(self.login_link)
        return LambdaTestLogin(self.driver)

    def click_book_a_demo_button(self):
        self.click(self.book_a_demo_button)
        return BookADemoPage(self.driver)

    def click_ajax_form_submit_link(self):
        # self.click(self.ajax_form_submit_link)
        self.wait_for_element_located(self.ajax_form_submit_link)
        self.click_link(self.ajax_form_submit_link)
        self.wait_until_url_contains("ajax-form-submit-demo")
        return AjaxFormSubmitDemoPage(self.driver)

