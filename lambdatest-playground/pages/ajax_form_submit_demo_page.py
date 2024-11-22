from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AjaxFormSubmitDemoPage(BasePage):
    form_submit_demo_h1 = (By.CSS_SELECTOR, "div.container h1")
    name_text = (By.XPATH, "//input[@name='title']")
    message_textarea = (By.XPATH, "//textarea[@name='description']")
    submit_button = (By.XPATH, "//input[@name='btn-submit']")
    request_processing = (By.XPATH, "//div[@id='submit-control']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_form_submit_demo_header(self):
        self.wait_for_element_located(self.form_submit_demo_h1)
        header_text = self.get_text(self.form_submit_demo_h1)
        return header_text

    def fill_name(self,name_text):
        self.set_text(
            self.name_text,
            text=name_text
        )

    def fill_message(self, message_text):
        self.set_text(
            self.message_textarea,
            text=message_text
        )

    def click_submit_button(self):
        self.click(self.submit_button)

    def get_text_of_request_processing(self):
        self.wait_for_element_located(self.request_processing)
        return self.get_text(self.request_processing)