import pytest

from tests.final_test.pages.basket_page import BasketPage
from tests.final_test.pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_add_to_basket()


@pytest.mark.parametrize('offer', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                   "?promo=offer5", "?promo=offer6", "?promo=offer7", "?promo=offer8", "?promo=offer9",
                                   ])
def test_guest_can_add_product_to_basket(browser, offer):
    page = ProductPage(browser, link + offer)
    page.open()
    page.should_be_add_to_basket_button()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_add_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.press_button_add_to_basket()

    page.guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.press_button_add_to_basket()
    page.message_disappeared_after_adding_product_to_basket()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.should_be_view_the_basket_button()
    page.press_view_the_basket_button()
    page.should_be_empty_basket()
    page.check_the_basket_is_empty()
   # page.check_the_basket_is_not_empty()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_log_in_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_log_in_page()


