from tests.final_test.pages.base_page import BasePage
from tests.final_test.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button 'Add to basket' is not presented"

    def press_button_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def check_add_to_basket(self):
        block_desc = self.browser.find_element(*ProductPageLocators.DIV_PRODUCT)
        title = block_desc.find_element(*ProductPageLocators.TITLE_PRODUCT).text
        price = block_desc.find_element(*ProductPageLocators.PRICE_PRODUCT).text

        alertinners = self.browser.find_elements(*ProductPageLocators.ALERT_INER)
        title_alert = alertinners[0].text
        assert title in title_alert, "the title doesn't match"

        assert self.is_element_present(*ProductPageLocators.ALERT_INFO), "Message about price is not presented"
        price_alert = alertinners[2].text
        assert price in price_alert, "the price doesn't match"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_INER), \
            "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_INER), \
            "Success message is presented, but should not be"