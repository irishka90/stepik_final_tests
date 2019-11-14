import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_add_to_basket()


@pytest.mark.parametrize('offer', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                   "?promo=offer5", "?promo=offer6", "?promo=offer7", "?promo=offer8", "?promo=offer9",
                                   ])
def test_guest_can_add_product_to_basket(browser, offer):
    page = MainPage(browser, link + offer)
    page.open()
    page.should_be_add_to_basket_button()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_add_to_basket()
