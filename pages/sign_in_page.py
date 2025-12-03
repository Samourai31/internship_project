from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage

class SignInPage(BasePage):
    SIGN_IN_LINK = (By.CSS_SELECTOR, 'div[wized="signinButtonSignup"]')
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[wized*="loginButton"]')

    def open_sign_in_page(self):
        self.open_url('https://soft.reelly.io/sign-up')
        sleep(3)

    def click_sign_in_link(self):
        self.click_element(*self.SIGN_IN_LINK)
        sleep(3)

    def enter_email(self, text='ilyastest31@gmail.com'):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(text)

    def enter_password(self, text='Costco4991!'):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(text)

    def click_continue_button(self):
        self.click_element(*self.CONTINUE_BUTTON)
