import pytest

from pages.selenium_playground_page import SeleniumPlaygroundPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class Test_SeleniumPlayground(BaseTest):
    def test_selenium_playground_header(self):
        seleniumPlaygroundPage = SeleniumPlaygroundPage(self.driver)
        seleniumPlaygroundPage.load_page(TestData.selenium_playground_url)
        actual_text = seleniumPlaygroundPage.get_selenium_playground_header()
        expected_text = "Selenium Playground"
        assert actual_text.__eq__(expected_text)

    def test_navigate_to_ajax_form_submit_demo_page(self):
        seleniumPlaygroundPage = SeleniumPlaygroundPage(self.driver)
        seleniumPlaygroundPage.load_page(TestData.selenium_playground_url)
        actual_text = seleniumPlaygroundPage.get_selenium_playground_header()
        ajaxFormSubmitDemoPage = seleniumPlaygroundPage.click_ajax_form_submit_link()
        actual_text = ajaxFormSubmitDemoPage.get_form_submit_demo_header()
        expected_text = "Form Submit Demo"
        assert expected_text == actual_text, "Form Submit Demo Header assert failed"

    def test_navigate_to_lambdatest_login_page(self):
        seleniumPlaygroundPage = SeleniumPlaygroundPage(self.driver)
        seleniumPlaygroundPage.load_page(TestData.selenium_playground_url)
        lambdatestLoginPage = seleniumPlaygroundPage.click_login_link()
        expected_title = "Log in"
        actual_title = lambdatestLoginPage.get_title(expected_title)
        assert actual_title == expected_title, "Assert failed for Login Page title verification"

    def test_navigate_to_book_a_demo_page(self):
        seleniumPlaygroundPage = SeleniumPlaygroundPage(self.driver)
        seleniumPlaygroundPage.load_page(TestData.selenium_playground_url)
        bookADemoPage = seleniumPlaygroundPage.click_book_a_demo_button()
        result = bookADemoPage.test_form_is_displayed()
        assert result is True