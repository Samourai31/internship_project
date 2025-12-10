from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    # Chrome options
    options = Options()
    options.add_argument("--headless")  # Headless mode
    options.add_argument("--window-size=1920,1080")

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)

    # Create driver with options
    context.driver = webdriver.Chrome(service=service, options=options)

    # Implicit and explicit waits
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    # Initialize application
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()