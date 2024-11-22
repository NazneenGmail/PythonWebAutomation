from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def wait_for_page_load(self):
        # Wait for the page to be fully loaded (using JavaScript)
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.execute_script("return document.readyState == 'complete'"))

    def wait_for_element_located(self, *locator):
        element = (WebDriverWait(self.driver, 10)
                   .until(EC.presence_of_element_located(*locator)))

    def find(self, *locator):
        element = (WebDriverWait(self.driver, 10)
         .until(EC.element_to_be_clickable(*locator)))
        return element

    def click(self, *locator):
        self.find(*locator).click()

    def click_link(self, *link_text_locator):
        element = self.find(*link_text_locator)
        element.click()
        self.wait_for_page_load()

    def set_text(self, *locator, text):
        self.find(*locator).clear()
        self.find(*locator).send_keys(text)

    def get_text(self, *locator):
        return self.find(*locator).text

    def wait_until_title_contains(self, expected_title):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains(expected_title))

    def wait_until_url_contains(self, expected_partial_url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains(expected_partial_url))

    def get_title(self, expected_title):
        self.wait_until_title_contains(expected_title)
        return self.driver.title

    def displayed(self, *locator):
        return self.find(*locator).is_displayed()

    def click_radio_button(self, *locator):
        if self.displayed(*locator):
            self.click(*locator)
