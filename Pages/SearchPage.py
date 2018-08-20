from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SearchPageLocators(object):

    jobs_list = (By.CSS_SELECTOR, "div[class*=js-search-results]")
    job_item = (By.CSS_SELECTOR, "section[class*=job-tile-responsive]")


class SearchPage(BasePage):

    URL = "/o/jobs/browse/"  #may contain search value as q value, and page value

    def get_url(self):
        return super().get_url() + "?q=Selenium"

    def get_count_of_found_items_on_page(self):
        return len(self.get_elements_with_not_stale_waiting(lambda driver: driver.find_element
                (*SearchPageLocators.jobs_list).find_elements(*SearchPageLocators.job_item), timeout=20))
