from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage


class Toolbox(BasePage):

    search_field_dropdown = None
    search_field_expand_arrow = None
    search_freelancers_search_option = None
    search_jobs_search_option = None
    search_input = None

    def choose_freelancers_search_value(self):
        if not self.is_exist(self.search_field_dropdown):
            self.click(self.search_field_expand_arrow)
        self.click(self.search_freelancers_search_option)
        return self

    def choose_jobs_search_value(self):
        if not self.is_exist(self.search_field_dropdown):
            self.click(self.search_field_expand_arrow)
        self.click(self.search_jobs_search_option)
        return self

    def get_search_current_placeholder(self):
        return self.get_element(self.search_input).get_attribute("placeholder")

    def get_search_current_text(self):
        return self.get_element(self.search_input).text

    def create_search(self, text_for_search, should_submit=True):
        search = self.type_text(self.search_input, text_for_search)
        if should_submit:
            search.send_keys(Keys.RETURN)
        return self
