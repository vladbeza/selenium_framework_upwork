from Toolboxes.AbstractToolbox import Toolbox
from selenium.webdriver.common.by import By

from Utils import wait_for_page_load

class AuthorizedToolbox(Toolbox):

    search_input = (By.NAME, "q")
    search_field_dropdown = (By.ID, "search-dropdown")
    search_field_expand_arrow = (By.CSS_SELECTOR, "span[class *= air-icon-arrow-expand]")
    search_freelancers_search_option = (By.CSS_SELECTOR, "li[data_label = Freelancers]")
    search_jobs_search_option = (By.CSS_SELECTOR, "li[data_label = Jobs]")

    account_name = (By.CSS_SELECTOR, "div#layout div.media-body span[class*=account-name]")
    profile_settigns_button = (By.CSS_SELECTOR, "div#layout a[href=/UserSettings/profile]")
    logout_button = (By.XPATH, ".//div[@id='layout']//a[form[@id='nav-logout']]")

    def logout(self):
        self.wait_for_visible(self.account_name)
        self.click(self.account_name)
        with wait_for_page_load(self.driver):
            self.click(self.logout_button)