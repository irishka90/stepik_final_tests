from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    DIV_PRODUCT = (By.CLASS_NAME, "product_main")
    TITLE_PRODUCT = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    ALERT_INER = (By.CLASS_NAME, "alertinner")
    ALERT_INFO = (By.CLASS_NAME, "alert-info")




class LoginPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
