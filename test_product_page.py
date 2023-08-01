import time

import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage

# url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
url_base = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.parametrize('promo', ["?promo=offer0",
                                   "?promo=offer1",
                                   "?promo=offer2",
                                   "?promo=offer3",
                                   "?promo=offer4",
                                   "?promo=offer5",
                                   "?promo=offer6",
                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                   "?promo=offer8",
                                   "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    url = url_base + promo
    page = MainPage(browser, url)
    page.open()
    # Инициализируем ProductPage в теле теста
    product_page = ProductPage(browser,
                               browser.current_url)
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    # Asserts
    product_page.should_be_add_product()
