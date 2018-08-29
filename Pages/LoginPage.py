import allure

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.FindWorkPageAuthorized import FindWorkPageAuthorized


class LoginPageLocators(object):

    upwork_header_label = (By.CLASS_NAME, 'navbar-brand')
    login_name_input = (By.ID, 'login_username')
    login_password_input = (By.ID, 'login_password')
    keep_logged_check = (By.ID, 'login_rememberme')
    continue_button = (By.XPATH, '//button[text()="Continue"]')
    login_button = (By.XPATH, '//button[text()="Log In"]')
    sigh_up_button = (By.LINK_TEXT, '/signup/create-account')
    forgot_pass = (By.LINK_TEXT, '/ab/account-security/reset-password?redir=/')
    not_you_link = (By.XPATH, '//button[text()="Not you?"]')


class LoginPage(BasePage):

    URL = "/ab/account-security/login"

    @allure.step("Fill login fields with email {1}, password {2}")
    def login(self, email, password):
        self.type_text(LoginPageLocators.login_name_input, email)
        self.click(LoginPageLocators.continue_button)

        self.wait_for_visible(LoginPageLocators.login_password_input)
        self.type_text(LoginPageLocators.login_password_input, password)
        with self.wait_for_page_loaded():
            self.click(LoginPageLocators.login_button)
        return self.pages.find_work_authorized

    def get_login_name_value(self):
        return self.get_element(LoginPageLocators.login_name_input).value

    def go_to_main_page(self):
        self.click(LoginPageLocators.upwork_header_label)
        return self
