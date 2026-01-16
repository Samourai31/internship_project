from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # Chrome options
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)

    # Local driver (kept as-is)
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()

    # ===== BrowserStack added (no if) =====
    bs_user = 'ilyas_xbhds4'
    bs_key = 'jjZpxJBD4Apx1ioUYKG4'

    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    bstack_options = {
        "os": "Windows",
        "osVersion": "11",
        "browserVersion": "latest",
        "sessionName": scenario_name,
    }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # Waits
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    # Initialize application
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
