import time

from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators, OtherLocators


class MainPage(BasePage):

    def should_be_browse_store(self):
        assert self.is_element_present(*MainPageLocators.BROWSE_STORE), "Browse store link is not presented"

    def all_products(self):
        assert self.is_element_present(*MainPageLocators.ALL_PRODUCTS), "All products link is not presented"
        text = self.browser.find_element(*MainPageLocators.ALL_PRODUCTS).get_attribute("innerHTML")
        all_prod = self.browser.find_element(*MainPageLocators.ALL_PRODUCTS)
        all_prod.click()
        page_title = self.browser.find_element(*MainPageLocators.HEADER_ALL_PRODUCTS)
        title = page_title.get_attribute("innerHTML")
        time.sleep(3)
        assert text in title, "the page title is not 'all books'"

    def offers(self):
        assert self.is_element_present(*MainPageLocators.OFFERS), "Offers link is not presented"
        text = self.browser.find_element(*MainPageLocators.OFFERS).get_attribute("innerHTML")
        offers = self.browser.find_element(*MainPageLocators.OFFERS)
        offers.click()
        page_title = self.browser.find_element(*MainPageLocators.HEADER_OFFERS)
        title = page_title.get_attribute("innerHTML")
        time.sleep(3)
        assert text in title, "the page title is not 'offers'"

    def return_to_main_page(self):
        assert self.is_element_present(*MainPageLocators.OSCAR), "Oscar link is not presented"
        self.browser.find_element(*MainPageLocators.OSCAR).click()
        assert self.is_element_present(*MainPageLocators.DROP_DOWN_MENU), "drop-down menu is not presented"
