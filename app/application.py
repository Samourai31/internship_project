from pages.base_page import BasePage
from pages.sign_in_page import SignInPage
from pages.secondary_page import SecondaryPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = BasePage(driver)
        self.sign_in_page = SignInPage(driver)
        self.secondary_page = SecondaryPage(driver)