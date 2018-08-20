from enum import Enum

import allure
from selenium.webdriver.common.by import By

from Elements.MainToolbox import MainToolbox
from Pages.BasePage import BasePage


class FaqType(Enum):

    CLIENT = 1
    FREELANCER = 2
    ABOUT = 3


class HowItWorksBasePage(BasePage):

    client_faq = (By.CSS_SELECTOR, "li#faq-1[role=menuitem]")
    freelancer_faq = (By.CSS_SELECTOR, "li#faq-2[role=menuitem]")
    faqs = (By.CSS_SELECTOR, "li#faq-3[role=menuitem]")

    URL = "/i/how-it-works/"

    def __init__(self, driver):
        super(HowItWorksBasePage, self).__init__(driver)
        self.toolbox = MainToolbox(driver)
        self.faq_type = ""

    def get_url(self):
        base = super().get_url()
        if self.faq_type == FaqType.CLIENT:
            ending = "client/"
        elif self.faq_type == FaqType.FREELANCER:
            ending = "freelancer/"
        else:
            ending = "faq/"
        return base + ending

    @allure.step("Open client faq")
    def open_client_faq(self):
        self.click(self.client_faq)
        self.faq_type = FaqType.CLIENT
        return self

    @allure.step("Open freelancer faq")
    def open_freelancer_faq(self):
        self.click(self.freelancer_faq)
        self.faq_type = FaqType.FREELANCER
        return self

    @allure.step("Open about faq")
    def open_faqs(self):
        self.click(self.faqs)
        self.faq_type = FaqType.ABOUT
        return self


class HowItWorksClientPage(HowItWorksBasePage):

    def __init__(self, driver):
        super(HowItWorksClientPage, self).__init__(driver)
        self.faq_type = FaqType.CLIENT


class HowItWorksFreelancerPage(HowItWorksBasePage):

    get_paid_button = (By.CSS_SELECTOR, 'a[data-qa=list_link][href="#get-paid"]')
    get_paid_header = (By.CSS_SELECTOR, 'div#get-paid + section h2')

    def __init__(self, driver):
        super(HowItWorksFreelancerPage, self).__init__(driver)
        self.faq_type = FaqType.FREELANCER

    @allure.step("Press get paid button")
    def press_get_paid(self):
        self.click(self.get_paid_button)
        return self

    def get_paid_header_element(self):
        return self.get_element(self.get_paid_header)


class HowItWorksAboutPage(HowItWorksBasePage):

    def __init__(self, driver):
        super(HowItWorksAboutPage, self).__init__(driver)
        self.faq_type = FaqType.ABOUT