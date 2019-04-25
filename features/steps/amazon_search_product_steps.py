from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox') # or SEARCH_INPUT = (By.NAME, 'field-keywords')
SEARCH_ICON = (By.XPATH, "//input[@type='submit' and @class='nav-input']")
RESULTS_INFO_BAR = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
# RESULTS_INFO_BAR = (By.XPATH, "//span[@data-component-type='s-result-info-bar']/div") # wrong xpath
SEARCH_FIRST_RESULT = (By.XPATH, "//div[@class='textContainer']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Input {search_word} into Amazon search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on Amazon search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then('Amazon product results for {search_world} are shown')
def verify_result_present(context, search_world):
    result_msg = context.driver.find_element(*RESULTS_INFO_BAR).text
    print(result_msg)
    assert search_world in result_msg, "Expected word '{}' in message, but got '{}' ".format(search_world, result_msg)


@then('Amazon first result contains {search_world}')
def verify_fount_first_result(context, search_world):
    first_result = context.driver.find_element(*SEARCH_FIRST_RESULT).text.lower()
    # print('\n{}'.format(first_result))
    assert search_world in first_result, \
        "Expected word '{}' in message, but got '{}' ".format(search_world, first_result)

