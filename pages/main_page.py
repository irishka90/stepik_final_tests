from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators, OtherLocators

class MainPage(BasePage):

    def should_be_browse_store(self):
        assert self.is_element_present(*MainPageLocators.BROWSE_STORE), "Browse store link is not presented"






