from selenium.webdriver.common.by import By

from .BasePage import BasePage


class UpdatePageLocators(object):

    check_status_button = (By.XPATH, '//*[@id="main"]/div/div/p[2]/a')
    will_be_soon_message = (By.XPATH, '//*[@id="main"]/div/div/h2')


class UpdatePage(BasePage):

    URL = ""

    def click_status_button(self):
        self.get_element(UpdatePageLocators.check_status_button).click()

    def is_will_be_soon_message_visible(self):
        message = self.get_element(UpdatePageLocators.will_be_soon_message)
        return message.is_visible()





