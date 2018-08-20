import allure
from selenium.webdriver.common.by import By

from Utils import wait_for_page_load_context_manager
from Elements.MainToolbox import MainToolbox
from Pages.BasePage import BasePage
from Pages.AllFreelancersCategoriesPage import AllFreelancersCategoriesPage


class MainPageLocators(object):

    work_type_input = (By.CSS_SELECTOR, 'div.ee-input-holder input[class*=form-control]')
    get_started_button = (By.CSS_SELECTOR, 'div.ee-input-holder > input[class*=btn]')
    matches_dropdown_menu = (By.CSS_SELECTOR, 'div[id*=typeahead-13] ul.dropdown-menu')
    web_developers_category_item = (By.XPATH, '//ul[@class="__item" and @href="/cat/developers/"]')
    mob_developers_category_item = (By.XPATH, '//ul[@class="__item" and @href="/cat/mobile-developers/"]')
    designers_category_item = (By.XPATH, '//a[@class="__item" and @href="/cat/designers/"]')
    writers_category_item = (By.XPATH, '//a[@class="__item" and @href="/cat/writing/"]')
    virtual_assistant_item = (By.XPATH, '//a[@class="__item" and @href="/cat/administrative-support/"]')
    customer_agents_item = (By.XPATH, '//a[@class="__item" and @href="/cat/customer-service/"]')
    sales_and_marketing_item = (By.XPATH, '//a[@class="__item" and @href="/cat/sales-marketing/"]')
    accountants_item = (By.XPATH, '//a[@class="__item" and @href="/cat/accounting-consulting/"]')
    all_categories_button = (By.CSS_SELECTOR, 'section[class*="__tiles-section"] a[class*="btn-default"][href="/i/freelancer-categories-all/"]')


class StepModalWindow(BasePage):

    URL = "/"

    main_window = (By.CSS_SELECTOR, 'div.modal-dialog div.steps')
    close_button = (By.XPATH, '//div[@class="step-header"]/a[@class="icon-close"]')
    next_button_main = (By.CSS_SELECTOR, 'div[class*=step-content] button[class*=btn]')
    back_button = (By.XPATH, '//div[contains(@class,"step-footer")]/div[@class="to-left"]/a')
    next_button = (By.CSS_SELECTOR, 'div[class*=step-footer] > div.to-right > button[class*=btn]')
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

    @allure.step("Press next button")
    def press_next_button_in_first_window(self):
        self.click(self.next_button_main)
        return self

    @allure.step("Press next button")
    def press_next_button(self):
        self.click(self.next_button)
        return self

    @allure.step("Select checkbox {0}")
    def select_checkbox_item(self, text):
        self.click(self.checkbox_by_text(text))
        return self

    def is_category_radio_box_checked(self, checkbox_text):
        return self.is_radio_checked(self.job_category_checkbox_by_text(checkbox_text))


class MainPage(BasePage):

    URL = "/"

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.toolbox = MainToolbox(driver)
        self.step_modal_window = StepModalWindow(self.driver)

    def get_elements_in_matches_drop_down(self):
        return self.get_element(MainPageLocators.matches_dropdown_menu).find_elements(By.CSS_SELECTOR, 'li[id*=typeahead] > a')

    def get_back_span_by_category_item(self, item_locator):
        self.get_element(item_locator).find_element(By.XPATH, '/span[@class="__back"]')

    @allure.step("Press category {1}")
    def press_category_item(self, item):
        element = self.scroll_to_element(item)
        self.click(element)
        return self

    @allure.step("Enter '{1}' to get started entry")
    def enter_text_to_get_started_entry(self, text):
        self.type_text(MainPageLocators.work_type_input, text)
        return self

    @allure.step("Press get started button")
    def press_get_started_button(self):
        self.click(MainPageLocators.get_started_button)
        self.wait_for_visible(self.step_modal_window.main_window)
        return self.step_modal_window

    @allure.step("Press all categories button")
    def press_all_categories_button(self):
        with self.wait_for_page_loaded():
            self.click(MainPageLocators.all_categories_button)
        return self.pages.all_freelance_categories
