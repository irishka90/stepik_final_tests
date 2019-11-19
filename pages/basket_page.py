from tests.final_test.pages.locators import OtherLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_element_present(*OtherLocators.EMPTY_BASKET), "'Empty basket' is not presented"

    def check_the_basket_is_empty(self):
        assert len(self.browser.find_element(*OtherLocators.EMPTY_BASKET).text) > 0, "The basket is not empty"

    def check_the_basket_is_not_empty(self):
        assert self.is_not_element_present(*OtherLocators.EMPTY_BASKET), \
            "Empty basket message is presented, but should not be"