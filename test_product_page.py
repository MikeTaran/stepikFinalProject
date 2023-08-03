import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.product_page import ProductPage

# url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
url_base = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [pytest.param((url_base + str(i)), marks=pytest.mark.xfail(i == 7, reason='')) for i in range(1)]


@pytest.mark.parametrize('url', links)
class TestProductPage:
    # @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self, browser, url):
        page = BasePage(browser, url)
        page.open()
        product_page = ProductPage(browser, url)
        product_page.add_to_basket()
        page.solve_quiz_and_get_code()
        product_page.should_be_add_product()

    @pytest.mark.xfail
    # @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, url):
        page = BasePage(browser, url)
        page.open()
        product_page = ProductPage(browser, url)
        product_page.add_to_basket()
        page.solve_quiz_and_get_code()
        product_page.should_not_be_success_message()

    # @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser, url):
        page = BasePage(browser, url)
        page.open()
        product_page = ProductPage(browser, url)
        product_page.should_not_be_success_message()

    @pytest.mark.xfail
    # @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser, url):
        page = BasePage(browser, url)
        page.open()
        product_page = ProductPage(browser, url)
        product_page.add_to_basket()
        page.solve_quiz_and_get_code()
        product_page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser, url):
        # url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser, url):
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser,
                               browser.current_url)
        login_page.should_be_login_page()
        # time.sleep(5)

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, url):
        page = ProductPage(browser, url)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, url)
        basket_page.should_be_basket_empty()
        basket_page.should_be_emptybasket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        pass


    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = BasePage(browser, url)
        product_page = ProductPage(browser, url)
        page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = BasePage(browser, url)
        page.open()
        product_page = ProductPage(browser, url)
        product_page.add_to_basket()
        page.solve_quiz_and_get_code()
        product_page.should_be_add_product()
