import math

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    # будет ждать до тех пор, пока элемент не исчезнет
    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.find_element(BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            BasePageLocators.LOGIN_LINK), 'Login link is not presented!!!'

    def go_to_basket(self):
        basket_link = self.find_element(BasePageLocators.BASKET_LINK)
        basket_link.click()
