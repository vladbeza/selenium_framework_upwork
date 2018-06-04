from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SearchPageLocators(object):

    jobs_list = (By.ID, "jobs-list")


class SearchPage(BasePage):

    URL = "/o/jobs/browse/"  #may contain search value as q value, and page value

    def get_count_of_found_items_on_page(self):
        return len(self.get_element(SearchPageLocators.jobs_list).find_elements(By.CSS_SELECTOR, "section.job-tile"))
