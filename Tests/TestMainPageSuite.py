import pytest

from Tests.BaseTestSuite import BaseTestSuite
from Pages.MainPage import MainPage, MainPageLocators, StepModalWindowLocators, StepModalWindow
from Pages.SignUpPage import SignUpPage
from Pages.SearchPage import SearchPage
from Toolboxes.MainToolbox import MainToolbox
from Pages.DeveloperTypesPages import WebDeveloperPage, MobileDeveloperPage, DesignerPage, WritingPage,\
    AdminSupportPage, CustomerServicePage, MarketingPage, AccountingPage
from Pages.LoginPage import LoginPage
from Pages.AllFreelancersCategoriesPage import AllFreelancersCategoriesPage
from Utils import wait_for_page_load


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
        assert main_page.wait_for_visible(MainPageLocators.matches_dropdown_menu)

    def test_matched_items_in_dropdown(self):
        main_page = self.get_main_page()
        main_page.enter_text_to_get_started_entry("selenium")
        assert main_page.get_elements_in_matches_drop_down()[0].text == "Qa & Testing"

    def test_navigate_to_all_categories_in_page_body(self):
        main_page = self.get_main_page()
        button = main_page.scroll_to_element(MainPageLocators.all_categories_button)
        main_page.scroll_page(-100)
        with wait_for_page_load(self.driver):
            button.click()
        assert self.driver.current_url == AllFreelancersCategoriesPage(self.driver).get_url()

    def test_modal_steps_window_appearance(self):
        main_page = self.get_main_page()
        main_page.press_get_started_button()
        assert main_page.get_element(StepModalWindowLocators.main_window).is_displayed()

    def test_steps_window_category_checkbox_checked(self):
        if self.driver.capabilities['browserName'] == "internet explorer":
            pytest.skip("IE bug")
        main_page = self.get_main_page()
        main_page.press_get_started_button()
        steps_window = StepModalWindow(self.driver)
        steps_window.press_next_button_in_first_window().select_checkbox_item("Web, Mobile & Software Dev")
        assert steps_window.is_category_radio_box_checked("Web, Mobile & Software Dev") is True

    def test_pass_steps_window_to_signup_form(self):
        if self.driver.capabilities['browserName'] == "internet explorer":
            pytest.skip("IE bug")
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

    def test_open_login_page(self):
        main_page = self.get_main_page()
        with wait_for_page_load(self.driver):
            main_page.toolbox.press_login_button()
        assert self.driver.current_url == LoginPage(self.driver).get_url()

    def test_open_signup_page_from_toolbox(self):
        main_page = self.get_main_page()
        with wait_for_page_load(self.driver):
            main_page.toolbox.press_signup_button()
        assert self.driver.current_url == SignUpPage(self.driver).get_url()

    @pytest.mark.parametrize("locator, expected_page",
                             [(MainToolbox.web_dev_link, WebDeveloperPage),
                              (MainToolbox.mobile_dev_link, MobileDeveloperPage),
                              (MainToolbox.design_link, DesignerPage),
                              (MainToolbox.writing_link, WritingPage),
                              (MainToolbox.admin_support_link, AdminSupportPage),
                              (MainToolbox.customer_support_link, CustomerServicePage),
                              (MainToolbox.marketing_support_link, MarketingPage),
                              (MainToolbox.accounting_link, AccountingPage)])
    def test_open_category(self, locator, expected_page):
        main_page = self.get_main_page()
        with wait_for_page_load(self.driver):
            main_page.toolbox.press_category_item(locator)
        assert self.driver.current_url == expected_page(self.driver).get_url()

    def test_toolbox_search_status(self):
        main_page = self.get_main_page()
        assert main_page.toolbox.get_search_current_placeholder() == "Find Freelancers"
        main_page.toolbox.choose_jobs_search_value()
        assert main_page.toolbox.get_search_current_placeholder() == "Find Jobs"
        main_page.toolbox.choose_freelancers_search_value()
        assert main_page.toolbox.get_search_current_placeholder() == "Find Freelancers"

    def test_jobs_search(self):
        main_page = self.get_main_page()
        search_page = SearchPage(self.driver)
        with wait_for_page_load(self.driver):
            main_page.toolbox.choose_jobs_search_value().create_search("Selenium")
        assert self.driver.current_url == search_page.get_url() + "?q=Selenium"
        assert search_page.get_count_of_found_items_on_page() == 10

