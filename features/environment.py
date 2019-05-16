from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context):
    """
    :param context: Behave context
    :param url: root url of the pages
    """
    context.driver = webdriver.Chrome('drivers/chromedriver')
    context.url = 'https://www.amazon.com'
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.driver.wait = WebDriverWait(context.driver, 10)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    context.driver.maximize_window()


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
