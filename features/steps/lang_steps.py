from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


TITLE_HELP_CS = (By.CSS_SELECTOR, "a.cs-help-title")
HEADER_ABT_LANG = (By.CSS_SELECTOR, "p.lead")



@then("Language page is opened")
def verify_lang_page_open(context):
    context.driver.find_element(*TITLE_HELP_CS)


@then("Verify '{expected_text}' is presented in Lang page")
def verify_header_abt_lang_presented(context, expected_text):
    actual_text = context.driver.find_element(*HEADER_ABT_LANG).text
    assert expected_text == actual_text, "Expected text is {}, but the actual_text is {}".format(expected_text, actual_text)