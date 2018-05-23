from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Toolboxes.MainToolbox import MainToolbox
from Elements.BaseElement import BaseElement


class MainPageLocators(object):

    work_type_input = (By.XPATH, '//div[@class="ee-input-holder"]/input[@class="form-control"]')
    get_started_button = (By.XPATH, '//div[@class="ee-input-holder"]/input[@class="btn"]')
    matches_dropdown_menu = (By.XPATH, '//div[@id="typeahead-13-3320"]/ul[@class="dropdown-menu"]')


class StepModalWindowLocators(object):

    main_window = (By.XPATH, '//div[@class="step-content"]')
    close_button = (By.XPATH, '//div[@class="step-header"]/a[@class="icon-close"]')
    next_button_main = (By.XPATH, '//div[@class="step-content"]/button[@class="btn"]')
    back_button = (By.XPATH, '//div[@class="step-footer"]/div[@class="to-left"]/a')
    next_button = (By.XPATH, '//div[@class="step-footer"]/div[@class="to-right"]/button[@class="btn"]')
    skill_text_input = (By.XPATH, '//div[@class="step-content"]//div[@class="form-control"]/input')
    sign_up_first_name_input = (By.ID, 'signup_bogus_form_firstName')
    sign_up_last_name_input = (By.ID, 'signup_bogus_form_lastName')
    sign_up_email_input = (By.ID, 'signup_bogus_form_email')
    sigh_up_button = (By.ID, 'signup_bogus_form_save')

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


class MainPage(BasePage):

    URL = ""

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.toolbox = MainToolbox(driver)

    def get_checkbox_span_in_step_modal_by_input_locator(self, locator):
        return self.get_element(locator).find_element(By.XPATH, 'following-sibling::span[@class="checkbox-replacement-helper"]')

    def get_elements_in_matches_drop_down(self):
        return self.get_element(MainPageLocators.matches_dropdown_menu).find_elements(By.XPATH, '/li[contains(@id,"typeahead")]')

    def enter_text_to_get_started_entry(self, text):
        input = self.get_element(MainPageLocators.work_type_input)
        input.clear()
        input.send_keys(text)

    def press_get_started_button(self):
        self.get_element(MainPageLocators.get_started_button).click()

