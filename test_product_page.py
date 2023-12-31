import pytest

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

url_base = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
# range(10)
links = [pytest.param((url_base + str(i)), marks=pytest.mark.xfail(i == 7, reason='')) for i in range(1)]


@pytest.mark.parametrize('url', links)
class TestProductPage:
    # @pytest.mark.skip
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, url):
        page = ProductPage(browser, url)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_add_product()

    @pytest.mark.xfail
    # @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, url):
        page = ProductPage(browser, url)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    # @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser, url):
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    # @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser, url):
        page = ProductPage(browser, url)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser, url):
        page = ProductPage(browser, url)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, url):
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser,
                               browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, url):
        page = BasketPage(browser, url)
        page.open()
        page.go_to_basket()
        page.should_be_basket_empty()
        page.should_be_emptybasket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, url)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_add_product()
