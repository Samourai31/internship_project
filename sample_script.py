from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

options = Options()
options.add_argument('headless')
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://soft.reelly.io/sign-up')

driver.find_element(By.CSS_SELECTOR, 'div[wized="signinButtonSignup"]').click()

driver.find_element(By.ID, 'email-2').send_keys('ilyastest31@gmail.com')
driver.find_element(By.ID, 'field').send_keys('Costco4991!')
driver.find_element(By.CSS_SELECTOR, 'a[wized*="loginButton"]').click()

element = wait.until(
    EC.element_to_be_clickable((By.ID, 'w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b'))
)

element.click()

driver.find_element(By.CSS_SELECTOR, '.filter-button').click()

driver.find_element(By.CSS_SELECTOR, '[w-el-onclick-0-0="8719b271-6a8b-431b-b597-dd0d49af99f3-0-0"]').click()

driver.find_element(By.CSS_SELECTOR, 'img[src*="648fa2581719cb17514ece18"]').click()


cards = driver.find_elements(By.CSS_SELECTOR, 'div[wized="listingCardMLS"]')

for_sale_cards = [card for card in cards if "For sale" in card.text]

print("Cards with 'For sale':", len(for_sale_cards))

