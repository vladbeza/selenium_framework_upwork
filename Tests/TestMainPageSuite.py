import pytest

from Elements.MainToolbox import MainToolbox
from Pages.DeveloperTypesPages import WebDeveloperPage, MobileDeveloperPage, DesignerPage, WritingPage, \
    AdminSupportPage, CustomerServicePage, MarketingPage, AccountingPage
from Tests.BaseTestSuite import BaseTestSuite
from PagesFactory import PagesFactory
from Pages.MainPage import MainPageLocators


class TestMainPage(BaseTestSuite):

    def get_main_page(self):
        return PagesFactory(self.driver).main.open_page()

    def test_open_main_page(self):
        assert self.get_main_page().is_url_opened()

    def test_matches_dropdown_appearance(self):
        main_page = self.get_main_page()
        main_page.enter_text_to_get_started_entry("selenium")
        assert main_page.wait_for_visible(MainPageLocators.matches_dropdown_menu, raise_on_fail=False)

    def test_matched_items_in_dropdown(self):
        main_page = self.get_main_page()
        main_page.enter_text_to_get_started_entry("selenium")
        assert main_page.get_elements_in_matches_drop_down()[0].text == "Qa & Testing"

    def test_navigate_to_all_categories_in_page_body(self):
        main_page = self.get_main_page()
        all_freelancers_page = main_page.scroll_to_element(MainPageLocators.all_categories_button).scroll_page(-100)\
            .press_all_categories_button()
        assert all_freelancers_page.is_url_opened()

    def test_modal_steps_window_appearance(self):
        main_page = self.get_main_page()
        main_page.press_get_started_button()
        assert main_page.get_element(main_page.step_modal_window.main_window).is_displayed()

    def test_steps_window_category_checkbox_checked(self):
        if self.driver.capabilities['browserName'] == "internet explorer":
            pytest.skip("IE bug")
        steps_window = self.get_main_page().press_get_started_button()
        steps_window.press_next_button_in_first_window().select_checkbox_item("Web, Mobile & Software Dev")
        assert steps_window.is_category_radio_box_checked("Web, Mobile & Software Dev") is True

    def test_pass_steps_window_to_signup_form(self):
        if self.driver.capabilities['browserName'] == "internet explorer":
            pytest.skip("IE bug")
        steps_window = self.get_main_page().press_get_started_button()
        steps_window.press_next_button_in_first_window().select_checkbox_item("Web, Mobile & Software Dev").\
            press_next_button().select_checkbox_item("QA & Testing").press_next_button().\
            select_checkbox_item("Web Testing").select_checkbox_item("Automated Testing").\
            select_checkbox_item("Selenium").press_next_button().select_checkbox_item("More than 6 months").\
            press_next_button().select_checkbox_item("More than 30 hrs/week").press_next_button().\
            select_checkbox_item("Expert - Willing to pay the highest rates for the most experience").press_next_button()
        assert steps_window.get_element(steps_window.sigh_up_button).is_displayed()

    def test_open_login_page(self):
        login_page = self.get_main_page().toolbox.press_login_button()
        assert login_page.is_url_opened()

    def test_open_signup_page_from_toolbox(self):
        signup_page = self.get_main_page().toolbox.press_signup_button()
        assert signup_page.is_url_opened()

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
        self.get_main_page().toolbox.press_category_item(locator)
        assert expected_page(self.driver).is_url_opened()

    def test_toolbox_search_status(self):
        main_page = self.get_main_page()
        assert main_page.toolbox.get_search_current_placeholder() == "Find Freelancers"
        main_page.toolbox.choose_jobs_search_value()
        assert main_page.toolbox.get_search_current_placeholder() == "Find Jobs"
        main_page.toolbox.choose_freelancers_search_value()
        assert main_page.toolbox.get_search_current_placeholder() == "Find Freelancers"

    def test_jobs_search(self):
        search_page = self.get_main_page().toolbox.choose_jobs_search_value().create_search("Selenium")
        assert search_page.is_url_opened()
        assert search_page.get_count_of_found_items_on_page() == 10

