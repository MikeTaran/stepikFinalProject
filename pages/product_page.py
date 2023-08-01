from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.find_element(ProductPageLocators.ADD_BUSKET_BUTTON)
        add_button.click()

    def should_be_equal_name(self):
        prod_name = self.find_element(ProductPageLocators.PRODUCT_NAME).text
        message_name = self.find_element(ProductPageLocators.MESSAGE_NAME).text
        print('\n message prod name:', message_name, '\n', prod_name)
        assert message_name == prod_name, 'Product name is not correct'

    def should_be_equal_price(self):
        prod_price = self.find_element(ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.find_element(ProductPageLocators.BASKET_PRICE).text

        print('\n Product price:', basket_price, '\n', prod_price)
        assert prod_price == basket_price, 'Product price is not correct'

    def should_be_add_product(self):
        self.should_be_equal_name()
        self.should_be_equal_price()
