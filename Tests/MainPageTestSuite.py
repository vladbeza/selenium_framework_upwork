import pytest
from Pages.MainPage import MainPage


@pytest.mark.usefixtures('driver')
class TestMainPage(object):

    def test_open_main_page(self):
        main_page = MainPage(self.driver)
        main_page.open_page()
        assert self.driver.current_url == "https://www.upwork.com/"

    def test_fill_form(self):
        main_page = MainPage(self.driver)
        main_page.open_page()
        main_page.sign_up_in_main_form("a", "b", "c")



