from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Toolboxes.MainToolbox import MainToolbox


class DeveloperTypesPagesLocators(object):

    hero_section = (By.XPATH, '//section[@data-qa-section="hero"]')
    get_started_button = (By.XPATH, '//a[@data-qa="hero_cta"]')

    hiring_cases = (By.XPATH, '//section[@data-qa-section="hiring-cases"]')

    freelancers_section = (By.XPATH, '//section[@data-qa-section="freelancer-carousel"]')
    profile_element = (By.XPATH, '//div[@data-qa="profile"]')
    view_profile_button = (By.XPATH, '//a[@data-qa="view_profile"]')
    next_arrow_button = (By.CLASS_NAME, 'icon-next')
    prev_arrow_button = (By.CLASS_NAME, 'icon-prev')

    text_pros_section = (By.XPATH, '//section[@data-qa-section="text-blocks-6"]')
    pros_title = (By.XPATH, '//h2[@data-qa="title"]')

    @classmethod
    def get_pros_section_item_by_text(cls, text):
        return (By.XPATH, '//div[p[@data-qa="name" and text()="{}"]]/a[@data-qa="item_link"]'.format(text))

    how_it_works_section = (By.XPATH, '//section[@data-qa-section="text-blocks"]')

    sign_up_first_name_input = (By.ID, 'signup_bogus_form_firstName')
    sign_up_last_name_input = (By.ID, 'signup_bogus_form_lastName')
    sign_up_email_input = (By.ID, 'signup_bogus_form_email')
    sigh_up_button = (By.ID, 'signup_bogus_form_save')

    skills_links_list = (By.XPATH, '//section[@data-qa-section="links-list"]')

    @classmethod
    def get_skill_link(cls, text):
        return (By.XPATH, '//a[@data-qa="skills" and text()="{}"]'.format(text))

    @classmethod
    def get_link_by_name(cls, text):
        return (By.XPATH, '//a[text()="{}"]'.format(text))


class DeveloperTypesBasePage(BasePage):

    def __init__(self, driver):
        super(DeveloperTypesBasePage, self).__init__(driver)
        self.toolbox = MainToolbox(driver)

    def view_profile_by_index(self, index):
        profile_elements = self.get_elements(DeveloperTypesPagesLocators.profile_element)
        self.click(profile_elements[index])

    def profiles_count(self):
        return len(self.get_elements(DeveloperTypesPagesLocators.profile_element))

    def click_in_demand_pro(self, name):
        self.click(DeveloperTypesPagesLocators.get_pros_section_item_by_text(name))

    def sign_up_in_main_form(self, first_name, last_name, work_email):
        self.scroll_to_element(DeveloperTypesPagesLocators.sign_up_first_name_input)
        self.type_text(DeveloperTypesPagesLocators.sign_up_first_name_input, first_name)

        self.scroll_to_element(DeveloperTypesPagesLocators.sign_up_last_name_input)
        self.type_text(DeveloperTypesPagesLocators.sign_up_last_name_input, last_name)

        self.scroll_to_element(DeveloperTypesPagesLocators.sign_up_email_input)
        self.type_text(DeveloperTypesPagesLocators.sign_up_last_name_input, work_email)

        self.click(DeveloperTypesPagesLocators.sigh_up_button)


class WebDeveloperPage(DeveloperTypesBasePage):

    URL = "/cat/developers/"


class MobileDeveloperPage(DeveloperTypesBasePage):

    URL = "/cat/mobile-developers/"


class DesignerPage(DeveloperTypesBasePage):

    URL = "/cat/designers/"


class WritingPage(DeveloperTypesBasePage):

    URL = "/cat/writing/"


class AdminSupportPage(DeveloperTypesBasePage):

    URL = "/cat/administrative-support/"


class CustomerServicePage(DeveloperTypesBasePage):

    URL = "/cat/customer-service/"


class MarketingPage(DeveloperTypesBasePage):

    URL = "/cat/sales-marketing/"


class AccountingPage(DeveloperTypesBasePage):

    URL = "/cat/accounting-consulting/"

