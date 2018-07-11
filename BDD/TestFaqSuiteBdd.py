from pytest_bdd import scenarios, given, when, then, parsers, scenario

from Pages.HowItWorksPage import HowItWorksFreelancerPage, HowItWorksClientPage
from Pages.MainPage import MainPage


@scenario('Features/open_freelance_faq_get_pain.feature', 'Navigating to freelancer about page')
def test_navigate_to_freelancer_faq(driver):
    pass


@scenario('Features/open_freelance_faq_get_pain.feature', 'Open client about page')
def test_navigate_to_client_faq(driver):
    pass


@given("I'm on how it works page")
def open_how_it_works_page(driver):
    freelancer_about_page = HowItWorksFreelancerPage(driver)
    freelancer_about_page.open_page()
    return freelancer_about_page


@given("I'm on main page")
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    return main_page


@when("I press the get paid button")
def press_get_paid(open_how_it_works_page):
    open_how_it_works_page.press_get_paid()


@then(parsers.parse("{header_text} header is visible"))
def get_paid_header_should_be_visible(open_how_it_works_page, header_text):
    header = open_how_it_works_page.get_paid_header_element()
    assert header.text == header_text
    assert header.is_displayed()


@when("I press how it works button")
def press_how_it_works_page(open_main_page):
    open_main_page.toolbox.press_how_it_works_button()


@then("Client faq page is opened")
def verify_client_faq_page_opened(driver):
    assert HowItWorksClientPage(driver).is_url_opened()
