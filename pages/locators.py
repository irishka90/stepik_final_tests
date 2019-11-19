from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")
    BROWSE_STORE = (By.ID, "browse")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    DIV_PRODUCT = (By.CLASS_NAME, "product_main")
    TITLE_PRODUCT = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    ALERT_INER = (By.CLASS_NAME, "alertinner")
    ALERT_INFO = (By.CLASS_NAME, "alert-info")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_THE_BASKET = (By.CLASS_NAME, "btn-group")


class OtherLocators():
    EMPTY_BASKET = (By.ID, "content_inner")
