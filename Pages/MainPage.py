from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Toolboxes.MainToolbox import MainToolbox
from Elements.BaseElement import BaseElement


class MainPageLocators(object):

    work_type_input = (By.XPATH, '//div[@class="ee-input-holder"]/input[contains(@class,"form-control")]')
    get_started_button = (By.XPATH, '//div[@class="ee-input-holder"]/input[contains(@class,"btn")]')
    matches_dropdown_menu = (By.XPATH, '//div[contains(@id,"typeahead-13")]/ul[@class="dropdown-menu"]')
    web_developers_category_item = (By.XPATH, '//ul[@class="__item" and @href="/cat/developers/"]')
    mob_developers_category_item = (By.XPATH, '//ul[@class="__item" and @href="/cat/mobile-developers/"]')
    designers_category_item = (By.XPATH, '//a[@class="__item" and @href="/cat/designers/"]')
    writers_category_item = (By.XPATH, '//a[@class="__item" and @href="/cat/writing/"]')
    virtual_assistant_item = (By.XPATH, '//a[@class="__item" and @href="/cat/administrative-support/"]')
    customer_agents_item = (By.XPATH, '//a[@class="__item" and @href="/cat/customer-service/"]')
    sales_and_marketing_item = (By.XPATH, '//a[@class="__item" and @href="/cat/sales-marketing/"]')
    accountants_item = (By.XPATH, '//a[@class="__item" and @href="/cat/accounting-consulting/"]')
    all_categories_button = (By.XPATH, '//section[contains(@class, "__tiles-section")]//a[contains(@class, "btn-default") and @href="/i/freelancer-categories-all/"]')


class StepModalWindowLocators(object):

    main_window = (By.XPATH, '//div[contains(@class,"step-content")]')
    close_button = (By.XPATH, '//div[@class="step-header"]/a[@class="icon-close"]')
    next_button_main = (By.XPATH, '//div[contains(@class,"step-content")]//button[contains(@class,"btn")]')
    back_button = (By.XPATH, '//div[contains(@class,"step-footer")]/div[@class="to-left"]/a')
    next_button = (By.XPATH, '//div[contains(@class,"step-footer")]/div[@class="to-right"]/button[contains(@class,"btn")]')
    skill_text_input = (By.XPATH, '//div[contains(@class,"step-content")]//div[@class="form-control"]/input')
    sign_up_first_name_input = (By.ID, 'signup_bogus_form_firstName')
    sign_up_last_name_input = (By.ID, 'signup_bogus_form_lastName')
    sign_up_email_input = (By.ID, 'signup_bogus_form_email')
    sigh_up_button = (By.ID, 'signup_bogus_form_save')

    @classmethod
    def checkbox_by_text(cls, text):
        return By.XPATH, '//div[@class="step-content"]//label[span[text() = "{}"]]'.format(text)

    @classmethod
    def job_category_checkbox_by_text(cls, text):
        return By.XPATH, cls.checkbox_by_text(text)[1] + '//input[@name="category_radio"]'


class StepModalWindow(BasePage):

    URL = ""

    def press_next_button_in_first_window(self):
        self.click(StepModalWindowLocators.next_button_main)
        return self

    def press_next_button(self):
        self.click(StepModalWindowLocators.next_button)
        return self

    def select_checkbox_item(self, text):
        self.click(StepModalWindowLocators.checkbox_by_text(text))
        return self

    def is_category_radio_box_checked(self, checkbox_text):
        return self.is_radio_checked(StepModalWindowLocators.job_category_checkbox_by_text(checkbox_text))


class MainPage(BasePage):

    URL = ""

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.toolbox = MainToolbox(driver)

    def get_elements_in_matches_drop_down(self):
        return self.get_element(MainPageLocators.matches_dropdown_menu).find_elements(By.XPATH, '/li[contains(@id, "typeahead")]')

    def get_back_span_by_category_item(self, item_locator):
        self.get_element(item_locator).find_element(By.XPATH, '/span[@class="__back"]')

    def press_category_item(self, item):
        element = self.scroll_to_element(item)
        self.click(element)
        return self

    def enter_text_to_get_started_entry(self, text):
        self.type_text(MainPageLocators.work_type_input, text)
        return self

    def press_get_started_button(self):
        self.click(MainPageLocators.get_started_button)
        return self
