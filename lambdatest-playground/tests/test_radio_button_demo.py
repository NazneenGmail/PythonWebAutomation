import pytest
from urllib3 import request

from pages.radio_button_demo_page import RadioButtonDemoPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class Test_RadioButtonDemo(BaseTest):
    #enhance tests to use parameterization - Male and Female
    @pytest.fixture(params=['Male', 'Female'])
    def male_female_radio_button_in_gruop1(self, request):
        return request.param

    def test_Male_or_Female_selected_value(self,male_female_radio_button_in_gruop1):
        radioButtonDemoPage = RadioButtonDemoPage(self.driver)
        radioButtonDemoPage.load_page(TestData.radiobutton_demo_url)
        if male_female_radio_button_in_gruop1 == 'Male':
            radioButtonDemoPage.click_male_radio_button_group1()
            radioButtonDemoPage.click_get_value_button()
            assert radioButtonDemoPage.check_radio_button_checked_message_contains('Male')
        elif male_female_radio_button_in_gruop1 == 'Female':
            radioButtonDemoPage.click_female_radio_button_group1()
            radioButtonDemoPage.click_get_value_button()
            assert radioButtonDemoPage.check_radio_button_checked_message_contains('Female')

    @pytest.fixture(
        params = [
            ('Male', '0 - 5'),
            ('Male', '5 - 15'),
            ('Male', '15 - 50'),
            ('Female', '0 - 5'),
            ('Female', '5 - 15'),
            ('Female', '15 - 50'),
            ('Other', '0 - 5'),
            ('Other', '5 - 15'),
            ('Other', '15 - 50'),
        ]
    )
    def gender_and_age_range_radio_button_in_group2(self, request):
        return request.param

    def test_get_selected_gender_and_age_value(self, gender_and_age_range_radio_button_in_group2):
        gender, age_range = gender_and_age_range_radio_button_in_group2
        radioButtonDemoPage = RadioButtonDemoPage(self.driver)
        radioButtonDemoPage.load_page(TestData.radiobutton_demo_url)

        # select gender
        if gender == 'Male':
            radioButtonDemoPage.click_radio_button_male_group2()
        elif gender == 'Female':
            radioButtonDemoPage.click_radio_button_female_group2()
        elif gender == 'Other':
            radioButtonDemoPage.click_radio_button_other_group2()

        # select age
        if age_range == '0 - 5':
            radioButtonDemoPage.click_radio_button_age_0to5()
        elif age_range == '5 - 15':
            radioButtonDemoPage.click_radio_button_age_5to15()
        elif age_range == '15 - 50':
            radioButtonDemoPage.click_radio_button_age_15to50()

        # click Get Values button
        radioButtonDemoPage.click_get_values_button()

        # assert
        assert radioButtonDemoPage.check_selected_value_gender_contains(gender)
        assert radioButtonDemoPage.check_selected_value_age_range_contains(age_range)
