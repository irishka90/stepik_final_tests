from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators, OtherLocators

class MainPage(BasePage):

    def should_be_browse_store(self):
        assert self.is_element_present(*MainPageLocators.BROWSE_STORE), "Browse store link is not presented"

    def all_products(self):
        assert self.is_element_present(*MainPageLocators.ALL_PRODUCTS), "All products link is not presented"
        all_prod = self.browser.find_element(*MainPageLocators.ALL_PRODUCTS)
        text = all_prod.text()
        all_prod.click()
        page_title = self.browser.find_element(*MainPageLocators.HEADER_ALL_PRODUCTS)
        title = page_title.text()
        assert text in title, "the page title is not 'all books'"







