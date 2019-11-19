import pytest
from tests.final_test.pages.basket_page import BasketPage
from tests.final_test.pages.login_page import LoginPage
from tests.final_test.pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_log_in_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_log_in_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page (browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_view_the_basket_button()
    page.press_view_the_basket_button()
    page.should_be_empty_basket()
    page.check_the_basket_is_empty()

