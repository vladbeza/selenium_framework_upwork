import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.BaseTestSuite import BaseTestSuite
from Pages.MainPage import MainPage
from Toolboxes.MainToolbox import MainToolboxLocators
from Pages.DeveloperTypesPages import WebDeveloperPage, MobileDeveloperPage, DesignerPage, WritingPage,\
    AdminSupportPage, CustomerServicePage, MarketingPage, AccountingPage
from Pages.LoginPage import LoginPage
from Pages.AllFreelancersCategoriesPage import AllFreelancersCategoriesPage


class TestMainPage(BaseTestSuite):

    def get_main_page(self):
        main_page = MainPage(self.driver)
        main_page.open_page()
        return main_page

    # def test_open_main_page(self):
    #     self.get_main_page()
    #     assert self.driver.current_url == "https://www.upwork.com/"
    #
    # def test_matches_dropdown_appearance(self):
    #     main_page = self.get_main_page()
    #     main_page.enter_text_to_get_started_entry("selenium")
    #     assert main_page.get_element(MainPageLocators.matches_dropdown_menu).is_displayed()

    # def test_matched_items_in_dropdown(self):
    #     main_page = self.get_main_page()
    #     main_page.enter_text_to_get_started_entry("selenium")
    #     assert main_page.get_elements_in_matches_drop_down()[0].text == "Qa & Testing"

    # def test_navigate_to_all_categories_in_page_body(self):
    #     main_page = self.get_main_page()
    #     button = main_page.scroll_to_element(MainPageLocators.all_categories_button)
    #     main_page.scroll_page(-100)
    #     button.click()
    #     assert self.driver.current_url == AllFreelancersCategoriesPage(self.driver).get_url()
    #
    # def test_modal_steps_window_appearance(self):
    #     main_page = self.get_main_page()
    #     main_page.press_get_started_button()
    #     assert main_page.get_element(StepModalWindowLocators.main_window).is_displayed()
    #
    # def test_steps_window_category_checkbox_checked(self):
    #     main_page = self.get_main_page()
    #     main_page.press_get_started_button()
    #     WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(StepModalWindowLocators.main_window))
    #     steps_window = StepModalWindow(self.driver)
    #     steps_window.press_next_button_in_first_window().select_checkbox_item("Web, Mobile & Software Dev")
    #     assert steps_window.is_category_radio_box_checked("Web, Mobile & Software Dev") is True
    #
    # def test_pass_steps_window_to_signup_form(self):
    #     main_page = self.get_main_page()
    #     main_page.press_get_started_button()
    #     steps_window = StepModalWindow(self.driver)
    #     steps_window.press_next_button_in_first_window().select_checkbox_item("Web, Mobile & Software Dev").press_next_button()
    #     steps_window.select_checkbox_item("QA & Testing").press_next_button()
    #     steps_window.select_checkbox_item("Web Testing").select_checkbox_item("Automated Testing").\
    #         select_checkbox_item("Selenium").press_next_button()
    #     steps_window.select_checkbox_item("More than 6 months").press_next_button()
    #     steps_window.select_checkbox_item("More than 30 hrs/week").press_next_button()
    #     steps_window.select_checkbox_item("Expert - Willing to pay the highest rates for the most experience").press_next_button()
    #     assert steps_window.get_element(StepModalWindowLocators.sigh_up_button).is_displayed()

    # def test_open_login_page(self):
    #     main_page = self.get_main_page()
    #     main_page.toolbox.press_login_button()
    #     assert self.driver.current_url == LoginPage(self.driver).get_url()

    @pytest.mark.parametrize("locator, expected_page",
                             [(MainToolboxLocators.web_dev_link, WebDeveloperPage),
                              (MainToolboxLocators.mobile_dev_link, MobileDeveloperPage),
                              (MainToolboxLocators.design_link, DesignerPage),
                              (MainToolboxLocators.writing_link, WritingPage),
                              (MainToolboxLocators.admin_support_link, AdminSupportPage),
                              (MainToolboxLocators.customer_support_link, CustomerServicePage),
                              (MainToolboxLocators.marketing_support_link, MarketingPage),
                              (MainToolboxLocators.accounting_link, AccountingPage)])
    def test_open_category(self, locator, expected_page):
        main_page = self.get_main_page()
        main_page.toolbox.press_category_item(locator)
        assert self.driver.current_url == expected_page(self.driver).get_url()