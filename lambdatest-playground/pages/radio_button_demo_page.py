from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RadioButtonDemoPage(BasePage):
    radio_button_demo_h1 = (By.CSS_SELECTOR, "div.container h1")

    radio_button_male_group1 = (By.XPATH, "//input[@name='optradio' and @value='Male']")
    radio_button_female_group1 = (By.XPATH, "//input[@name='optradio' and @value='Female']")
    get_value_button = (By.XPATH, "//button[@id='buttoncheck']")
    radio_button_checked_message = (
        By.XPATH, "//button[@id='buttoncheck']//following::p[contains(text(), 'Radio button')]")

    radio_button_male_group2 = (By.XPATH, "//input[@name='gender' and @value='Male']")
    radio_button_female_group2 = (By.XPATH, "//input[@name='gender' and @value='Female']")
    radio_button_other_group2 = (By.XPATH, "//input[@name='gender' and @value='Other']")
    radio_button_age_0to5 = (By.XPATH, "//input[@name='ageGroup' and @value = '0 - 5']")
    radio_button_age_5to15 = (By.XPATH, "//input[@name='ageGroup' and @value = '5 - 15']")
    radio_button_age_15to50 = (By.XPATH, "//input[@name='ageGroup' and @value = '15 - 50']")

    get_values_button = (By.XPATH, "//button[contains(text(), 'Get values')]")

    selected_value_gender = (By.XPATH, "//span[@class = 'genderbutton']")
    selected_value_age_range = (By.XPATH, "//span[@class = 'groupradiobutton']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_male_radio_button_group1(self):
        self.click_radio_button(self.radio_button_male_group1)

    def click_female_radio_button_group1(self):
        self.click_radio_button(self.radio_button_female_group1)

    def click_get_value_button(self):
        self.click(self.get_value_button)

    def check_radio_button_checked_message_contains(self, male_or_female):
        return self.get_text(self.radio_button_checked_message).__contains__(male_or_female)

    def click_radio_button_male_group2(self):
        self.click_radio_button(self.radio_button_male_group2)

    def click_radio_button_female_group2(self):
        self.click_radio_button(self.radio_button_female_group2)

    def click_radio_button_other_group2(self):
        self.click_radio_button(self.radio_button_other_group2)

    def click_radio_button_age_0to5(self):
        self.click_radio_button(self.radio_button_age_0to5)

    def click_radio_button_age_5to15(self):
        self.click_radio_button(self.radio_button_age_5to15)

    def click_radio_button_age_15to50(self):
        self.click_radio_button(self.radio_button_age_15to50)

    def click_get_values_button(self):
        self.click(self.get_values_button)

    def check_selected_value_gender_contains(self, selected_gender):
        return self.get_text(self.selected_value_gender).__contains__(selected_gender)

    def check_selected_value_age_range_contains(self, selected_age_range):
        return self.get_text(self.selected_value_age_range).__contains__(selected_age_range)