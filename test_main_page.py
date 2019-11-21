import pytest
import time
from tests.final_test.pages.basket_page import BasketPage
from tests.final_test.pages.login_page import LoginPage
from tests.final_test.pages.main_page import MainPage
from tests.final_test.pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_log_in_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_log_in_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.should_be_view_the_basket_button()
    page.press_view_the_basket_button()
    page.should_be_empty_basket()
    page.check_the_basket_is_empty()


@pytest.mark.login
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_log_in_link()
        page.go_to_log_in_page()
        page.should_be_login_url()
        page.should_be_register_form()
        page.register_new_user(email=str(time.time()) + "@fakemail.org")


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()
        product_page.should_be_add_to_basket_button()
        product_page.press_button_add_to_basket()
        product_page.can_see_success_message_after_adding_product_to_basket()

    @pytest.mark.xfail
    def test_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()
        product_page.should_be_add_to_basket_button()
        product_page.press_button_add_to_basket()
        product_page.cant_see_success_message_after_adding_product_to_basket()


def test_search_product(browser):
    page = MainPage(browser, link)
    page.open()
    page.search_product()


# ????????
def test_language_change(browser):
    page = MainPage(browser, link)
    page.open()
    page.language_change()

def test_return_to_main_page_from_prod_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.return_to_main_page()

class TestBrowseStore():
    def test_all_products(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_browse_store()
        page.all_products()

    def test_offers(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_browse_store()
        page.offers()


