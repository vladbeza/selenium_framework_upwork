from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage


class MainToolboxLocators(object):

    search_input = (By.ID, "q")
    search_field_expand_arrow = (By.CLASS_NAME, "glyphicon air-icon-arrow-expand")
    logo = (By.CSS_SELECTOR, 'a[data-qa=logo]')

    search_freelancers_search_option = (By.CSS_SELECTOR, 'a[data-qa=freelancer_value]')
    search_jobs_search_option = (By.CSS_SELECTOR, 'a[data-qa=client_value]')
    search_field_dropdown = (By.CSS_SELECTOR, 'a[data-qa=search_field_dropdown]')

    login_button = (By.CSS_SELECTOR, 'a[data-qa=login]')
    how_it_works = (By.CSS_SELECTOR, 'a[href="/i/how-it-works/client/"]')
    sign_up = (By.CSS_SELECTOR, 'a[data-qa=signup]')
    post_job_button = (By.CSS_SELECTOR, 'a[data-qa=cta_post_job]')

    web_dev_link = (By.CSS_SELECTOR, 'div.row:nth-child(2) a[href="/cat/developers/"]')
    mobile_dev_link = (By.CSS_SELECTOR, 'a[href="/cat/mobile-developers/"]')
    design_link = (By.CSS_SELECTOR, 'a[href="/cat/designers/"]')
    writing_link = (By.CSS_SELECTOR, 'a[href="/cat/writing/"]')
    admin_support_link = (By.CSS_SELECTOR, 'a[href="/cat/administrative-support/"]')
    customer_support_link = (By.CSS_SELECTOR, 'a[href="/cat/customer-service/"]')
    marketing_support_link = (By.CSS_SELECTOR, 'a[href="/cat/sales-marketing/"]')
    accounting_link = (By.CSS_SELECTOR, 'a[href="/cat/accounting-consulting/"]')
    all_categories_link = (By.CSS_SELECTOR, 'a[href="/i/freelancer-categories-all/"]')

    primary_nav_bar = (By.CSS_SELECTOR, 'a[data-qa-section=primary-navbar]')


class MainToolbox(BasePage):

    def choose_freelancers_search_value(self):
        if not self.is_exist(MainToolboxLocators.search_field_dropdown):
            self.get_element(MainToolboxLocators.search_field_expand_arrow).click()
        self.get_element(MainToolboxLocators.search_freelancers_search_option).click()
        return self

    def choose_jobs_search_value(self):
        if not self.is_exist(MainToolboxLocators.search_field_dropdown):
            self.get_element(MainToolboxLocators.search_field_expand_arrow).click()
        self.get_element(MainToolboxLocators.search_jobs_search_option).click()
        return self

    def create_search(self, text_for_search, should_submit=True):
        search = self.get_element(MainToolboxLocators.search_input)
        search.clear()
        search.send_keys(text_for_search)
        if should_submit:
            search.send_keys(Keys.RETURN)
        return self

    def press_login_button(self):
        self.click(MainToolboxLocators.login_button)

    def press_category_item(self, locator):
        self.click(locator)
