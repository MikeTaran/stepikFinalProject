from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_path = self.browser.current_url
        print('\n current url:', login_path)
        assert "login" in login_path, 'Login URL is not present'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), 'Login form is not presented!!!'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM), 'Registration form is not presented!!!'
