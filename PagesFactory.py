from Pages import AllFreelancersCategoriesPage
from Pages import DeveloperTypesPages
from Pages import HowItWorksPage
from Pages import LoginPage
from Pages import MainPage
from Pages import SearchPage
from Pages import SignUpPage
from Pages import UpdatePage
from Pages import FindWorkPageAuthorized


class PagesFactory(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def main(self):
        return MainPage.MainPage(self.driver)

    @property
    def all_freelance_categories(self):
        return AllFreelancersCategoriesPage.AllFreelancersCategoriesPage(self.driver)

    @property
    def web_developers(self):
        return DeveloperTypesPages.WebDeveloperPage(self.driver)

    @property
    def mobile_developers(self):
        return DeveloperTypesPages.MobileDeveloperPage(self.driver)

    @property
    def designers(self):
        return DeveloperTypesPages.DesignerPage(self.driver)

    @property
    def writers(self):
        return DeveloperTypesPages.WritingPage(self.driver)

    @property
    def admins(self):
        return DeveloperTypesPages.AdminSupportPage(self.driver)

    @property
    def customers_service(self):
        return DeveloperTypesPages.CustomerServicePage(self.driver)

    @property
    def about(self):
        return HowItWorksPage.HowItWorksAboutPage(self.driver)

    @property
    def about_freelancers(self):
        return HowItWorksPage.HowItWorksFreelancerPage(self.driver)

    @property
    def about_clients(self):
        return HowItWorksPage.HowItWorksClientPage(self.driver)

    @property
    def login(self):
        return LoginPage.LoginPage(self.driver)

    @property
    def search(self):
        return SearchPage.SearchPage(self.driver)

    @property
    def sign_up(self):
        return SignUpPage.SignUpPage(self.driver)

    @property
    def update(self):
        return UpdatePage.UpdatePage(self.driver)

    @property
    def find_work_authorized(self):
        return FindWorkPageAuthorized.FindWorkPageAuthorized(self.driver)
