from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import math

from tests.final_test.pages.locators import BasePageLocators, LoginPageLocators


class BasePage():

    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)

    def go_to_log_in_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_log_in_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout) \
                .until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

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

    def should_be_view_the_basket_button(self):
        assert self.is_element_present(*BasePageLocators.VIEW_THE_BASKET), "Button 'View the basket' is not presented"

    def press_view_the_basket_button(self):
        go_to_basket = self.browser.find_element(*BasePageLocators.VIEW_THE_BASKET)
        go_to_basket.click()

        #поиск товара
        #смена языка
