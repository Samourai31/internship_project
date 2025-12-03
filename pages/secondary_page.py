from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage

class SecondaryPage(BasePage):
    SECONDARY_TAB = (By.ID, 'w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b')
    FILTER_BUTTON = (By.CSS_SELECTOR, '.filter-button')
    WANT_TO_SELL_FILTER = (By.CSS_SELECTOR, '[w-el-onclick-0-0="8719b271-6a8b-431b-b597-dd0d49af99f3-0-0"]')
    CLOSE_FILTER = (By.CSS_SELECTOR, 'img[src*="648fa2581719cb17514ece18"]')

    def click_secondary_tab(self):
        self.click_element(*self.SECONDARY_TAB)
        sleep(3)

    def click_filter_button(self):
        self.click_element(*self.FILTER_BUTTON)
        sleep(3)

    def click_want_to_sell_filter(self):
        self.click_element(*self.WANT_TO_SELL_FILTER)
        sleep(3)

    def click_close_filter(self):
        self.click_element(*self.CLOSE_FILTER)
        sleep(3)

    def verify_for_sale_tag(self):
        cards = self.driver.find_elements(By.CSS_SELECTOR, 'div[wized="listingCardMLS"]')
        for_sale_cards = [card for card in cards if "For sale" in card.text]
        print(f'\033[32mAll {len(for_sale_cards)} cards have a “for sale” tag\033[0m')