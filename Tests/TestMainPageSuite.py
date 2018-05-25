import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseTestSuite import BaseTestSuite
from Pages.MainPage import MainPage, MainPageLocators, StepModalWindow, StepModalWindowLocators
from Pages.AllFreelancersCategoriesPage import AllFreelancersCategoriesPage


class TestMainPage(BaseTestSuite):

    def get_main_page(self):
        main_page = MainPage(self.driver)
        main_page.open_page()
        return main_page

    def test_open_main_page(self):
        self.get_main_page()
        assert self.driver.current_url == "https://www.upwork.com/"

    def test_matches_dropdown_appearance(self):
        main_page = self.get_main_page()
        main_page.enter_text_to_get_started_entry("selenium")
        assert main_page.get_element(MainPageLocators.matches_dropdown_menu).is_displayed()

    def test_navigate_to_all_categories(self):
        main_page = self.get_main_page()
        button = main_page.scroll_to_element(MainPageLocators.all_categories_button)
        main_page.scroll_page(-100)
        button.click()
        assert self.driver.current_url == AllFreelancersCategoriesPage(self.driver).get_url()

    def test_modal_steps_window_appearance(self):
        main_page = self.get_main_page()
        main_page.press_get_started_button()
        assert main_page.get_element(StepModalWindowLocators.main_window).is_displayed()

    def test_steps_window_category_checkbox_checked(self):
        main_page = self.get_main_page()
        main_page.press_get_started_button()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(StepModalWindowLocators.main_window))
        steps_window = StepModalWindow(self.driver)
        steps_window.press_next_button_in_first_window().select_checkbox_item("Web, Mobile & Software Dev")
        assert steps_window.is_category_radio_box_checked("Web, Mobile & Software Dev") is True

    def test_pass_steps_window_to_signup_form(self):
        main_page = self.get_main_page()
        main_page.press_get_started_button()
        steps_window = StepModalWindow(self.driver)
        steps_window.press_next_button_in_first_window().select_checkbox_item("Web, Mobile & Software Dev").press_next_button()
        steps_window.select_checkbox_item("QA & Testing").press_next_button()
        steps_window.select_checkbox_item("Web Testing").select_checkbox_item("Automated Testing").\
            select_checkbox_item("Selenium").press_next_button()
        steps_window.select_checkbox_item("More than 6 months").press_next_button()
        steps_window.select_checkbox_item("More than 30 hrs/week").press_next_button()
        steps_window.select_checkbox_item("Expert - Willing to pay the highest rates for the most experience").press_next_button()
        assert steps_window.get_element(StepModalWindowLocators.sigh_up_button).is_displayed()