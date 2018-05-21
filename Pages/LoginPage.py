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

    URL = "ab/account-security/login?redir=/"

    def login(self, email, password):
        login_input = self.get_element(LoginPageLocators.login_name_input)
        login_input.clear()
        login_input.send_keys(email)
        self.get_element(LoginPageLocators.continue_button).click()

        pass_input = self.get_element(LoginPageLocators.login_password_input)
        pass_input.clear()
        pass_input.send_keys(password)

        self.get_element(LoginPageLocators.login_button).click()
        return self

    def get_login_name_value(self):
        login_input = self.get_element(LoginPageLocators.login_name_input)
        return login_input.value

    def go_to_main_page(self):
        self.get_element(LoginPageLocators.upwork_header_label).click()
        return self
