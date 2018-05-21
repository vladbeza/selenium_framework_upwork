from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Toolboxes.MainToolbox import MainToolbox
from Elements.BaseElement import BaseElement


class MainPageLocators(object):

    work_type_input = (By.XPATH, '//div[@class="ee-input-holder"]/input[@class="form-control"]')
    get_started_button = (By.XPATH, '//div[@class="ee-input-holder"]/input[@class="btn"]')


class StepModalWindowLocators(object):

    close_button = (By.XPATH, '//div[@class="step-header"]/a[@class="icon-close"]')
    main_div = (By.XPATH, '//div[@class="step-content"]')
    next_button_main = (By.XPATH, '//div[@class="step-content"]/button[@class="btn"]')
    back_button = (By.XPATH, '//div[@class="step-footer"]/div[@class="to-left"]/a')
    next_button = (By.XPATH, '//div[@class="step-footer"]/div[@class="to-right"]/button[@class="btn"]')

    def job_category_item_locator_by_text(self, text):
        return (By.XPATH, '//div[@class="step-content"]//label[span[text() = "{}"]/input[@name="category_radio"]'.format(text))

    def job_sub_category_locator_by_text(self, text):
        return (
        By.XPATH, '//div[@class="step-content"]//label[span[text() = "{}"]/input[@name="subcategory_radios"]'.format(text))

    def skill_type_add_item_by_text(self, text):
        return (By.XPATH, '//div[@class="step-content"]//label[span[text() = "{}"]/input[@name="skillCheckboxes"]'.format(text))

    def project_duration_locator_by_text(self, text):
        return (
        By.XPATH, '//div[@class="step-content"]//label[span[text() = "{}"]/input[@name="duration_radios"]'.format(text))

    def title_commitment_radio_by_text(self, text):
        return (
            By.XPATH,
            '//div[@class="step-content"]//label[span[text() = "{}"]/input[@name="time_radios"]'.format(text))

    def experience_radio_by_text(self, text):
        return (
            By.XPATH,
            '//div[@class="step-content"]//label[span[text() = "{}"]/input[@name="experience_radios"]'.format(text))

    skill_text_input = (By.XPATH, '//div[@class="step-content"]//div[@class="form-control"]/input')





class MainPage(BasePage):

    URL = ""

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.toolbox = MainToolbox(driver)

