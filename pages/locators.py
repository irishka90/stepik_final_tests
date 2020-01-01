from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")
    BROWSE_STORE = (By.ID, "browse")
    ALL_PRODUCTS = (By.XPATH, "//*[@id='browse']/li/ul/li[1]/a")
    HEADER_ALL_PRODUCTS = (By.CLASS_NAME, "action")
    OFFERS = (By.XPATH, "//*[@id='browse']/li/ul/li[6]/a")
    OSCAR = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[1]/a")
    DROP_DOWN_MENU= (By.CLASS_NAME, "dropdown-menu")
    HEADER_OFFERS = (By.CLASS_NAME, "action")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    DIV_PRODUCT = (By.CLASS_NAME, "product_main")
    TITLE_PRODUCT = (By.TAG_NAME, "h1")
    PRICE_STRONG = (By.TAG_NAME, "strong")
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    ALERT_INER = (By.CLASS_NAME, "alertinner")
    ALERT_INFO = (By.CLASS_NAME, "alert-info")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_INPUT = (By.NAME, "registration-email")
    PASSWORD_1_INPUT = (By.ID, "id_registration-password1")
    PASSWORD_2_INPUT = (By.ID, "id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_THE_BASKET = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CLASS_NAME, "icon-user")
    SEARCH = (By.ID, "id_q")
    BUTTON_SEARCH = (By.XPATH, "//*[@id='default']/header/div[2]/div/div[2]/form/input")
    PAGE_HEADER = (By.XPATH, "//*[@id='default']/div[2]/div/div/div/div[1]")
    BOOK_TITLE = (By.XPATH, "//*[@id='default']/div[2]/div/div/div/section/div/ol/li/article/h3/a")
    LANGUAGE = (By.NAME, "language")
    RU_LANG = (By.XPATH, "//*[@id='language_selector']/div/select/option[18]")
    LANGUAGE_BUTTON = (By.XPATH, "//*[@id='language_selector']/button")


class OtherLocators():
    EMPTY_BASKET = (By.ID, "content_inner")
