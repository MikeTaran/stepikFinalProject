from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_BUSKET_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")
    PRODUCT_NAME= (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p>strong")
    BASKET_PRICE1 = (By.CSS_SELECTOR, ".basket-mini")
    MESSAGE_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")


