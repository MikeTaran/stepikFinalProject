from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(
            BasketPageLocators.LIST_OF_PRODUCT), "The Busket is Not Empty!"

    def should_be_emptybasket_message(self):
        assert self.is_element_present(
            BasketPageLocators.EMPTY_PRODUCT_MESSAGE), "The Busket empty message is Not present!"
