from pages.selenium_playground_page import SeleniumPlaygroundPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class Test_AjaxFormDemo(BaseTest):
    def test_ajax_form_submit(self):
        seleniumPlaygroundPage = SeleniumPlaygroundPage(self.driver)
        seleniumPlaygroundPage.load_page(TestData.selenium_playground_url)
        ajaxFormSubmitDemoPage = seleniumPlaygroundPage.click_ajax_form_submit_link()
        actual_text = ajaxFormSubmitDemoPage.get_form_submit_demo_header()
        ajaxFormSubmitDemoPage.fill_name("Name")
        ajaxFormSubmitDemoPage.fill_message("Test Message")
        ajaxFormSubmitDemoPage.click_submit_button()
        request_processing_message = ajaxFormSubmitDemoPage.get_text_of_request_processing()
        assert request_processing_message.strip() == "Ajax Request is Processing!"