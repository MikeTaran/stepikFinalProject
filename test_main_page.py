import pytest

from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage

url = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.go_to_login_page()
        # Инициализируем LoginPage в теле теста
        login_page = LoginPage(browser,
                               browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, url)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, url)
    basket_page.should_be_basket_empty()
    basket_page.should_be_emptybasket_message()
