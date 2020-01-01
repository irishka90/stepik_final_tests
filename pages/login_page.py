import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", \
            "link is not correct "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password="zxc123asd123qwe123"):
        # self.browser.implicitly_wait(5)
        time.sleep(2)
        assert self.is_element_present_with_wait(*LoginPageLocators.LOGIN_INPUT), "Not found email input"
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT)
        email_input.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_1_INPUT), "Not found password1 input"
        password_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_1_INPUT)
        password_1.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_2_INPUT), "Not found password2 input"
        password_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_2_INPUT)
        password_2.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REG_SUBMIT), "Not found button registration"
        button_submit = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        print(email)
        button_submit.click()
