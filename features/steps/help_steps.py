from selenium.webdriver.common.by import By
from behave import given, when, then


HELP_SEARCH_INPUT = (By.ID, "helpsearch")
HELP_SEARCH_GO = (By.ID, 'helpSearchSubmit')
SEARCH_RESULT_HEADER = (By.XPATH, "//div[@class='help-content']/h1")


@when('Input {search_phrase} into search help field')
def input_search(context, search_phrase):
    search = context.driver.find_element(*HELP_SEARCH_INPUT)
    search.clear()
    search.send_keys(search_phrase)


@when('Click Go button')
def click_go_btn(context):
    context.driver.find_element(*HELP_SEARCH_GO).click()


@then('Result contains {expected_result}')
def verify_help_search_result(context, expected_result):
    assert expected_result in context.driver.find_element(*SEARCH_RESULT_HEADER).text
  # assert expected_result == context.driver.find_element(*SEARCH_RESULT_HEADER).text