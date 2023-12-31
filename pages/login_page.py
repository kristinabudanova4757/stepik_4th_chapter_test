from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def register_new_user(self, email: str, password: str):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Email field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS1), "Pass field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS2), "Confirm pass field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), "Register button not presented"

        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert LoginPageLocators.PART_URL in self.browser.current_url, "Current url is incorrect"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
