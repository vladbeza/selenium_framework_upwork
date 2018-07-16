import allure

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SignUpLocators(object):

    first_name_entry = (By.CSS_SELECTOR, "input[name=firstName]")
    last_name_entry = (By.CSS_SELECTOR, "input[name=lastName]")
    email_entry = (By.CSS_SELECTOR, "input[name=email]")
    get_started_button = (By.CSS_SELECTOR, "div.text-center button:first-child")


class SignUpPage(BasePage):

    URL = "/signup/?dest=home"

    @allure.step("Fill sign up form with First name {1}, Last name {2}, email {3}")
    def fill_form_with_data(self, first_name, last_name, email):
        self.type_text(SignUpLocators.first_name_entry, first_name)
        self.type_text(SignUpLocators.last_name_entry, last_name)
        self.type_text(SignUpLocators.email_entry, email)

    @allure.step("Submit sign up form")
    def submit_form(self):
        self.click(SignUpLocators.get_started_button)
