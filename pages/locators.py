from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'header .basket-mini a.btn-default')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_BUSKET_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p>strong")
    BASKET_PRICE1 = (By.CSS_SELECTOR, ".basket-mini")
    MESSAGE_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']//div[1]//div[1]")


class BasketPageLocators:
    LIST_OF_PRODUCT = (By.CSS_SELECTOR, "#basket_formset>div")
    EMPTY_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".page_inner #messages")
