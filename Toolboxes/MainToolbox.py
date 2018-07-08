from selenium.webdriver.common.by import By

from Toolboxes.AbstractToolbox import Toolbox

class AuthorizedToolbox(Toolbox):

    search_input = (By.NAME, "q")
    search_field_dropdown = (By.ID, "search-dropdown")
    search_field_expand_arrow = (By.CSS_SELECTOR, "span[class *= air-icon-arrow-expand]")
    search_freelancers_search_option = (By.CSS_SELECTOR, "li[data_label = Freelancers]")
    search_jobs_search_option = (By.CSS_SELECTOR, "li[data_label = Jobs]")


class MainToolbox(Toolbox):

    search_input = (By.ID, "q")
    search_field_expand_arrow = (By.CSS_SELECTOR, "div[class *= input-group-addon]")
    logo = (By.CSS_SELECTOR, 'a[data-qa=logo]')
    search_freelancers_search_option = (By.CSS_SELECTOR, 'a[data-qa=freelancer_value]')
    search_jobs_search_option = (By.CSS_SELECTOR, 'a[data-qa=client_value]')
    search_field_dropdown = (By.CSS_SELECTOR, 'a[data-qa=search_field_dropdown]')
    login_button = (By.CSS_SELECTOR, 'a[data-qa=login]')
    how_it_works = (By.CSS_SELECTOR, 'a[href="/i/how-it-works/client/"]')
    sign_up = (By.CSS_SELECTOR, 'a[data-qa=signup]')
    post_job_button = (By.CSS_SELECTOR, 'a[data-qa=cta_post_job]')
    web_dev_link = (By.CSS_SELECTOR, 'a[href="/cat/developers/"]')
    mobile_dev_link = (By.CSS_SELECTOR, 'a[href="/cat/mobile-developers/"]')
    design_link = (By.CSS_SELECTOR, 'a[href="/cat/designers/"]')
    writing_link = (By.CSS_SELECTOR, 'a[href="/cat/writing/"]')
    admin_support_link = (By.CSS_SELECTOR, 'a[href="/cat/administrative-support/"]')
    customer_support_link = (By.CSS_SELECTOR, 'a[href="/cat/customer-service/"]')
    marketing_support_link = (By.CSS_SELECTOR, 'a[href="/cat/sales-marketing/"]')
    accounting_link = (By.CSS_SELECTOR, 'a[href="/cat/accounting-consulting/"]')
    all_categories_link = (By.CSS_SELECTOR, 'a[href="/i/freelancer-categories-all/"]')
    primary_nav_bar = (By.CSS_SELECTOR, 'a[data-qa-section=primary-navbar]')

    def press_login_button(self):
        self.click(self.login_button)

    def press_signup_button(self):
        self.click(self.sign_up)

    def press_how_it_works_button(self):
        self.click(self.how_it_works)

    def press_category_item(self, locator):
        element = self.driver.find_elements(*locator)[1]
        self.click(element)
