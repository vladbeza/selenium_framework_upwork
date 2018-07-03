from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


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

    def login(self, email, password):
        self.type_text(LoginPageLocators.login_name_input, email)
        self.click(LoginPageLocators.continue_button)

        self.wait_for_visible(LoginPageLocators.login_password_input, raise_on_fail=True)
        self.type_text(LoginPageLocators.login_password_input, password)
        self.click(LoginPageLocators.login_button)
        return self

    def get_login_name_value(self):
        return self.get_element(LoginPageLocators.login_name_input).value

    def go_to_main_page(self):
        self.click(LoginPageLocators.upwork_header_label)
        return self
