from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*MainPageLocators.ADD_TO_BASKET), "Button 'Add to basket' is not presented"

    def press_button_add_to_basket(self):
        add_to_basket = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def check_add_to_basket(self):
        block_desc = self.browser.find_element(*MainPageLocators.DIV_PRODUCT)
        title = block_desc.find_element(*MainPageLocators.TITLE_PRODUCT).text
        price = block_desc.find_element(*MainPageLocators.PRICE_PRODUCT).text

        alertinners = self.browser.find_elements(*MainPageLocators.ALERT_INER)
        title_alert = alertinners[0].text
        assert title in title_alert, "the title doesn't match"

        assert self.is_element_present(*MainPageLocators.ALERT_INFO), "Message about price is not presented"
        price_alert = alertinners[2].text
        assert price in price_alert, "the price doesn't match"
